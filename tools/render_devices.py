# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright", "pillow"]
# ///
"""把譯文裡的裝置畫面（class="device-view" 的 HTML 區塊）轉成圖片，讓一般 Markdown viewer 也能看到原站的樣子。

GitHub 等 Markdown viewer 會拿掉 <style>、<input>、<button>、inline SVG，裝置畫面因此和原站差很多。
做法：
- 譯好的 HTML 原稿存在 zh-tw/devices/chNN-KK.html（KK 為本章第幾個裝置畫面），這是唯一要編輯的地方。
- 章節檔裡的區塊換成置中的 <img>，alt 是畫面的全部文字（可搜尋、可朗讀）。
- 圖片用原站 original/html/chapter-1.html 的 CSS、以系統 Chrome 渲染，存在 assets/devices/chNN-KK.png（2 倍解析度）。
- 含 SVG 動畫（<animate>）的畫面輸出成循環 GIF（chNN-KK.gif）：在每個 keyTimes 變化點暫停截一格，
  所以重跑結果固定，不會隨截圖時機變動。發布平台只收圖片，動態 GIF 仍算圖片。
- check.py 比對錨點時會改讀 devices/ 的原稿，所以 HTML 標籤仍須與原文一字不差。

用法：
  uv run tools/render_devices.py N [N ...]    第一次：抽出本章裝置畫面的 HTML、換成圖片；之後：依原稿重新產圖與 alt
"""

import html
import importlib.util
import io
import re
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("check", ROOT / "tools" / "check.py")
check = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check)

IMG_DIR = ROOT / "assets" / "devices"
EXTRA_CSS = """
.device-view, .device-view button { font-family: 'Courier New', 'PingFang TC', 'Noto Sans TC', 'Heiti TC', monospace; }
body { background: transparent; display: block; }
.document-page { background: transparent; box-shadow: none; padding: 0; min-height: 0; }
/* 原站的 overflow-wrap: anywhere 會讓表格自動排版把窄欄壓到一字寬，數字（60259、10%）被切斷；break-word 只在真的放不下時才斷 */
.device-view th, .device-view td { overflow-wrap: break-word; }
/* 中文表頭與按鈕字（寄件者、級別、了解更多）在窄欄會被拆成一字一行；英文原文是單字不會斷。
   表頭用 keep-all：中文詞不從中間斷，有空格處（MUN GUI 1842）照樣可換行；按鈕字短，直接不換行 */
.device-view th { word-break: keep-all; }
.device-view button { white-space: nowrap; }
"""


def site_css() -> str:
    text = (ROOT / "original" / "html" / "chapter-1.html").read_text(encoding="utf-8")
    return re.search(r"<style>(.*?)</style>", text, re.S).group(1) + EXTRA_CSS


def img_block(did: str, ext: str, alt: str, width: int) -> str:
    return (f'<p align="center"><img src="../assets/devices/{did}.{ext}" '
            f'alt="{html.escape(alt, quote=True)}" width="{width}"></p>')


def change_times(src: str) -> tuple[list[float], float]:
    """SVG 動畫（calcMode="discrete"）的所有變化時間點（秒）與循環長度。只支援全部 <animate> 同一個 dur。"""
    durs = set(re.findall(r'dur="([\d.]+)s"', src))
    if len(durs) != 1:
        raise SystemExit(f"不支援的動畫：dur 不一致 {sorted(durs)}")
    dur = float(durs.pop())
    keys = {0.0}
    for kt in re.findall(r'keytimes="([^"]*)"', src, re.I):
        keys.update(float(x) for x in kt.split(";"))
    return sorted(k * dur for k in keys if k < 1), dur


def save_gif(el, src: str, path: Path) -> None:
    times, dur = change_times(src)
    frames = []
    for t in times:
        # 停在變化點之後一點點，discrete 動畫才會顯示新的那一格
        el.evaluate(f"e => {{ const s = e.querySelector('svg'); s.pauseAnimations(); s.setCurrentTime({t + 0.001}); }}")
        frames.append(Image.open(io.BytesIO(el.screenshot(omit_background=True))).convert("RGBA"))
    durations = [round((b - a) * 1000) for a, b in zip(times, times[1:] + [dur])]
    # 共用 32 色調色盤、不抖色：每格各自量化會讓檔案大好幾倍（2 MB → 約 0.3 MB），格線也會閃
    n = 32
    pal = frames[0].convert("RGB").quantize(colors=n, dither=Image.Dither.NONE)
    out = []
    for f in frames:
        p = f.convert("RGB").quantize(palette=pal, dither=Image.Dither.NONE)
        p.paste(n, mask=f.getchannel("A").point(lambda v: 255 if v < 128 else 0))  # 圓角外透明
        out.append(p)
    out[0].save(path, save_all=True, append_images=out[1:], duration=durations, loop=0,
                transparency=n, disposal=1, optimize=True)


def render(n: int, page, css: str) -> int:
    path = check.zh_path(n)
    bs = check.blocks(path.read_text(encoding="utf-8"))
    check.DEVICES.mkdir(parents=True, exist_ok=True)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    k = 0
    for i, b in enumerate(bs):
        m = check.DEVICE_IMG.search(b)
        if m:
            did = m.group(1)
            src = (check.DEVICES / f"{did}.html").read_text(encoding="utf-8").strip()
        elif check.kind(b) == "html" and 'class="device-view' in b:
            did = f"ch{n:02d}-{k + 1:02d}"
            src = b.strip()
            (check.DEVICES / f"{did}.html").write_text(src + "\n", encoding="utf-8")
        else:
            continue
        k += 1
        page.set_content(f"<html><head><meta charset='utf-8'><style>{css}</style></head>"
                         f"<body><div class='document-page'>{src}</div></body></html>")
        el = page.locator(".device-view").first
        ext = "gif" if "<animate" in src else "png"
        if ext == "gif":
            save_gif(el, src, IMG_DIR / f"{did}.gif")
        else:
            el.screenshot(path=str(IMG_DIR / f"{did}.png"), omit_background=True)
        (IMG_DIR / f"{did}.{'png' if ext == 'gif' else 'gif'}").unlink(missing_ok=True)
        width = round(el.bounding_box()["width"])
        bs[i] = img_block(did, ext, check.plain(src), width)
    path.write_text("\n\n".join(bs) + "\n", encoding="utf-8")
    return k


def main() -> int:
    ns = [int(x) for x in sys.argv[1:]]
    if not ns:
        print(__doc__)
        return 1
    css = site_css()
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        # 寬度 1200 才會套用原站桌面版規則（窄裝置畫面占版面一半）
        page = browser.new_page(device_scale_factor=2, viewport={"width": 1200, "height": 800})
        for n in ns:
            print(f"第 {n} 章：{render(n, page, css)} 個裝置畫面")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
