# /// script
# requires-python = ">=3.11"
# ///
"""翻譯流程的機械檢查工具。只檢查「結構與完成度」，不評判譯文品質。

用法：
  uv run tools/check.py status                 各章在各階段的進度
  uv run tools/check.py chapter N [N ...]      檢查第 N 章譯文的結構（ERROR 會讓 exit code = 1）
  uv run tools/check.py pair N [--from I] [--to J]
                                               英中逐段對照輸出（第二階段 QA 用）
  uv run tools/check.py terms [--chapter N]    依 glossary／characters／worldbuilding 的表格掃描術語一致性
  uv run tools/check.py find REGEX [--en] [--chapter N]
                                               在譯文（或 --en 原文）中搜尋，輸出對照段落

段落對齊規則：原文與譯文都以「空行」切段，段數必須一致，第 i 段對第 i 段。
"""

import argparse
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EN = ROOT / "source" / "en"
ZH = ROOT / "zh-tw"
TR = ROOT / "translation"
NOTES = TR / "notes"
QA = TR / "qa"
CONSISTENCY = TR / "consistency"
BIBLE = [TR / "glossary.md", TR / "characters.md", TR / "worldbuilding.md"]

CJK = re.compile(r"[㐀-鿿豈-﫿]")
LATIN = re.compile(r"[A-Za-z]")
TAG = re.compile(r"<[^>]+>")

# 只有簡體會用、繁體幾乎不會出現的字。出現即視為錯誤。
SIMPLIFIED = set(
    "这们说为个时会来对没过还发现样么应该经问题开关门见觉让给认识语话请谁读车东长马鸟鱼网"
    "电脑软间机构听计设备数图书买卖钱银头脸场厅号码级线组织务业专产亲爱欢观视历区医药饮饭"
    "馆脚轻轮转运进远连选达迟边闭题实现帮总结须虽随从难"
)
# 中國大陸用語，出現時給 WARN（有少數語境可能合理，交給人判斷）。
MAINLAND = [
    "信息", "視頻", "屏幕", "鼠標", "軟件", "網絡", "賬戶", "賬號", "登錄", "默認",
    "服務器", "內存", "硬盤", "人工智能", "設置", "芯片", "激光", "短信", "打印",
    "水平線以上", "沖他", "沖她", "高鐵站台", "質量很好", "視屏",
]
PLACEHOLDER = re.compile(r"TODO|TBD|待譯|<!--\s*CONTINUE|\[\[|\]\]|XXX")


# ---------------------------------------------------------------- 基本工具

def en_path(n: int) -> Path:
    return EN / f"chapter-{n:02d}.md"


def zh_path(n: int) -> Path:
    return ZH / f"chapter-{n:02d}.md"


def chapters() -> list[int]:
    return sorted(int(re.search(r"\d+", p.stem).group()) for p in EN.glob("chapter-*.md"))


def blocks(text: str) -> list[str]:
    return [b for b in re.split(r"\n[ \t]*\n", text.strip()) if b.strip()]


def kind(b: str) -> str:
    s = b.lstrip()
    if s.startswith("<"):
        return "html"
    if s.startswith("#"):
        return "heading"
    if re.fullmatch(r"[-*_]{3,}", s.strip()):
        return "hr"
    if s.startswith(">"):
        return "quote"
    if re.match(r"([-*+]|\d+\.)\s", s):
        return "list"
    return "prose"


def plain(b: str) -> str:
    """去掉標籤，只留可讀文字（html 區塊用）。"""
    t = TAG.sub(" ", b)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def en_words(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9']+", s))


def cjk_count(s: str) -> int:
    return len(CJK.findall(s))


# ---------------------------------------------------------------- chapter

def check_chapter(n: int) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warns: list[str] = []
    stats: dict = {}
    zp = zh_path(n)
    if not zp.exists():
        return [f"譯文不存在：{zp.relative_to(ROOT)}"], [], stats
    en_b = blocks(en_path(n).read_text(encoding="utf-8"))
    zh_text = zp.read_text(encoding="utf-8")
    zh_b = blocks(zh_text)
    stats["en_blocks"], stats["zh_blocks"] = len(en_b), len(zh_b)

    for m in PLACEHOLDER.finditer(zh_text):
        line = zh_text.count("\n", 0, m.start()) + 1
        errors.append(f"第 {line} 行有未完成標記：{m.group()!r}")

    bad = sorted({c for c in zh_text if c in SIMPLIFIED})
    if bad:
        errors.append(f"出現簡體字：{''.join(bad)}")

    if len(en_b) != len(zh_b):
        errors.append(f"段數不符：原文 {len(en_b)} 段，譯文 {len(zh_b)} 段（必須逐段對應，不可合併或拆分段落）")
        # 找出第一個種類不一致的位置，方便定位；錯位之後逐段比對沒有意義，直接回報
        for i, (e, z) in enumerate(zip(en_b, zh_b), 1):
            if kind(e) != kind(z) or TAG.findall(e) != TAG.findall(z):
                errors.append(f"  第一個對不上的位置約在第 {i} 段：EN「{plain(e)[:60]}」／ZH「{plain(z)[:40]}」")
                break
        return errors, warns, stats

    total_en = total_zh = 0
    for i, (e, z) in enumerate(zip(en_b, zh_b), 1):
        ke, kz = kind(e), kind(z)
        if ke != kz:
            errors.append(f"第 {i} 段類型不同：原文是 {ke}，譯文是 {kz}")
            continue
        te, tz = TAG.findall(e), TAG.findall(z)
        if te != tz:
            for j, (a, b) in enumerate(zip(te, tz)):
                if a != b:
                    errors.append(f"第 {i} 段 HTML 標籤被改動（第 {j + 1} 個標籤）：{a!r} → {b!r}")
                    break
            else:
                errors.append(f"第 {i} 段 HTML 標籤數量不同：{len(te)} → {len(tz)}")
        if ke == "hr":
            continue

        pe, pz = plain(e), plain(z)
        we, cz = en_words(pe), cjk_count(pz)
        total_en += we
        total_zh += cz
        latin = len(LATIN.findall(pz))
        if latin >= 30 and latin > 0.35 * (latin + cz):
            warns.append(f"第 {i} 段英文字母偏多（{latin} 個），可能有未翻譯的內容")
        if ke in {"prose", "quote", "list"} and we >= 25:
            ratio = cz / we
            if ratio < 0.9:
                warns.append(f"第 {i} 段譯文偏短（{cz} 字 / 原文 {we} 詞，比例 {ratio:.2f}），請確認沒有漏譯")
            elif ratio > 3.2:
                warns.append(f"第 {i} 段譯文偏長（{cz} 字 / 原文 {we} 詞，比例 {ratio:.2f}），請確認沒有增譯")
        if ke != "html":
            body = z
            if '"' in body or "“" in body or "”" in body:
                warns.append(f"第 {i} 段有英文引號，對話請用「」、引號內引號用『』")
            if re.search(r"[㐀-鿿][,?!:;]|[,?!:;][㐀-鿿]", body):
                warns.append(f"第 {i} 段在中文旁用了半形標點")
            if "..." in body:
                warns.append(f"第 {i} 段用了 ...，請改成……")
            if re.search(r"[㐀-鿿] - [㐀-鿿]|[㐀-鿿]--[㐀-鿿]", body):
                warns.append(f"第 {i} 段用了英文破折號，請改成——")
        for w in MAINLAND:
            if w in pz:
                warns.append(f"第 {i} 段出現中國大陸用語「{w}」")

    stats["en_words"], stats["zh_chars"] = total_en, total_zh
    if total_en:
        stats["ratio"] = total_zh / total_en
    return errors, warns, stats


def cmd_chapter(args) -> int:
    rc = 0
    for n in args.n:
        errors, warns, stats = check_chapter(n)
        verdict = "ERROR" if errors else ("PASS（有 WARN）" if warns else "PASS")
        ratio = f"，字詞比 {stats['ratio']:.2f}" if "ratio" in stats else ""
        print(f"== 第 {n} 章：{verdict}  段數 {stats.get('en_blocks', '?')}/{stats.get('zh_blocks', '?')}{ratio}")
        for e in errors:
            print(f"  ERROR {e}")
        for w in warns[: args.max_warn]:
            print(f"  WARN  {w}")
        if len(warns) > args.max_warn:
            print(f"  WARN  …另有 {len(warns) - args.max_warn} 則")
        if errors:
            rc = 1
    return rc


# ---------------------------------------------------------------- status

def cmd_status(args) -> int:
    rows = []
    next1 = next2 = None
    for n in chapters():
        w = en_words(en_path(n).read_text(encoding="utf-8"))
        if zh_path(n).exists():
            errors, warns, _ = check_chapter(n)
            s1 = "ERROR" if errors else (f"PASS/{len(warns)}w" if warns else "PASS")
        else:
            s1 = "-"
        notes = "✓" if (NOTES / f"chapter-{n:02d}.md").exists() else "-"
        s2 = "✓" if (QA / f"chapter-{n:02d}.md").exists() else "-"
        if next1 is None and not (s1.startswith("PASS") and notes == "✓"):
            next1 = n
        if next2 is None and s2 == "-":
            next2 = n
        rows.append((n, w, s1, notes, s2))
    print("章  英文詞數  階段一譯文   筆記  階段二QA")
    for n, w, s1, notes, s2 in rows:
        print(f"{n:>2}  {w:>8}  {s1:<11} {notes:^4}  {s2:^6}")
    done3 = sorted(p.stem for p in CONSISTENCY.glob("*.md")) if CONSISTENCY.exists() else []
    bible = {p.name: ("✓" if p.exists() else "-") for p in [TR / "synopsis.md", TR / "open-questions.md", *BIBLE]}
    print()
    print("階段零 bible：" + "  ".join(f"{k} {v}" for k, v in bible.items()))
    print(f"階段一下一章：{next1 or '全部完成'}")
    print(f"階段二下一章：{next2 or '全部完成'}")
    print(f"階段三已完成：{', '.join(done3) or '無'}")
    return 0


# ---------------------------------------------------------------- pair / find

def show_pair(n: int, i: int, e: str, z: str | None):
    k = kind(e)
    if k == "hr":
        return
    tag = " [html，只顯示文字]" if k == "html" else ""
    print(f"[{n}:{i}]{tag}")
    print(f"EN: {plain(e) if k == 'html' else e}")
    if z is not None:
        print(f"ZH: {plain(z) if k == 'html' else z}")
    print()


def cmd_pair(args) -> int:
    n = args.n
    en_b = blocks(en_path(n).read_text(encoding="utf-8"))
    zh_b = blocks(zh_path(n).read_text(encoding="utf-8")) if zh_path(n).exists() else []
    lo = args.start or 1
    hi = args.end or len(en_b)
    if zh_b and len(zh_b) != len(en_b):
        print(f"!! 段數不符（{len(en_b)}/{len(zh_b)}），對照可能錯位", file=sys.stderr)
    for i in range(lo, min(hi, len(en_b)) + 1):
        show_pair(n, i, en_b[i - 1], zh_b[i - 1] if i - 1 < len(zh_b) else "（缺）")
    return 0


def cmd_find(args) -> int:
    rx = re.compile(args.regex)
    hits = 0
    for n in ([args.chapter] if args.chapter else chapters()):
        if not zh_path(n).exists() and not args.en:
            continue
        en_b = blocks(en_path(n).read_text(encoding="utf-8"))
        zh_b = blocks(zh_path(n).read_text(encoding="utf-8")) if zh_path(n).exists() else []
        target = en_b if args.en else zh_b
        for i, b in enumerate(target, 1):
            if rx.search(b):
                hits += 1
                if hits > args.limit:
                    continue
                show_pair(n, i, en_b[i - 1] if i - 1 < len(en_b) else "（缺）",
                          zh_b[i - 1] if i - 1 < len(zh_b) else None)
    if hits > args.limit:
        print(f"…共 {hits} 筆，只顯示前 {args.limit} 筆（用 --limit 調整）")
    else:
        print(f"共 {hits} 筆")
    return 0


# ---------------------------------------------------------------- terms

def parse_tables() -> list[dict]:
    """讀 bible 檔中所有表頭含「English」與「譯名」的 Markdown 表格。"""
    entries = []
    for f in BIBLE:
        if not f.exists():
            continue
        header = None
        for line in f.read_text(encoding="utf-8").splitlines():
            if not line.strip().startswith("|"):
                header = None
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if header is None:
                if "English" in cells and "譯名" in cells:
                    header = cells
                continue
            if all(re.fullmatch(r":?-+:?", c) for c in cells if c):
                continue
            row = dict(zip(header, cells))
            en = row.get("English", "").strip("` ")
            zh = row.get("譯名", "").strip("` ")
            if not en or not zh or zh.startswith("（"):
                continue
            entries.append({
                "file": f.name,
                "en": en,
                "zh": [z.strip() for z in re.split(r"[／/]", zh) if z.strip()],
                "avoid": [a.strip() for a in re.split(r"[、,，]", row.get("避免", "")) if a.strip() and a.strip() != "-"],
            })
    return entries


def en_regex(term: str) -> re.Pattern:
    flags = 0 if term[:1].isupper() else re.IGNORECASE
    return re.compile(r"(?<![A-Za-z])" + re.escape(term) + r"(?![a-z])", flags)


def cmd_terms(args) -> int:
    entries = parse_tables()
    if not entries:
        print("bible 裡還沒有可解析的術語表（表頭需含 English、譯名）")
        return 0
    chs = [args.chapter] if args.chapter else [n for n in chapters() if zh_path(n).exists()]
    texts = {n: (en_path(n).read_text(encoding="utf-8"), zh_path(n).read_text(encoding="utf-8")) for n in chs}
    problems = 0
    for ent in entries:
        rx = en_regex(ent["en"])
        # 較長的詞條若包含本詞（例如 Min 與 Hun Min），先從原文遮掉，避免誤判
        longer = [en_regex(o["en"]) for o in entries
                  if o["en"] != ent["en"] and rx.search(o["en"])]
        missing, avoided = [], []
        for n, (en, zh) in texts.items():
            for lr in longer:
                en = lr.sub(" ", en)
            if ent["avoid"]:
                for a in ent["avoid"]:
                    c = zh.count(a)
                    if c:
                        avoided.append(f"{n}章×{c}「{a}」")
            if rx.search(en) and not any(z in zh for z in ent["zh"]):
                missing.append(str(n))
        if missing or avoided:
            problems += 1
            print(f"- {ent['en']} → {'／'.join(ent['zh'])}  （{ent['file']}）")
            if avoided:
                print(f"    出現應避免的譯法：{', '.join(avoided)}")
            if missing:
                print(f"    原文有此詞、譯文卻找不到譯名的章節：{', '.join(missing)}")
    print(f"\n共 {len(entries)} 個詞條，{problems} 個需要檢查")
    return 0


# ---------------------------------------------------------------- main

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    c = sub.add_parser("chapter")
    c.add_argument("n", type=int, nargs="+")
    c.add_argument("--max-warn", type=int, default=30)
    pr = sub.add_parser("pair")
    pr.add_argument("n", type=int)
    pr.add_argument("--from", dest="start", type=int)
    pr.add_argument("--to", dest="end", type=int)
    t = sub.add_parser("terms")
    t.add_argument("--chapter", type=int)
    f = sub.add_parser("find")
    f.add_argument("regex")
    f.add_argument("--en", action="store_true")
    f.add_argument("--chapter", type=int)
    f.add_argument("--limit", type=int, default=40)
    args = p.parse_args()
    return {"status": cmd_status, "chapter": cmd_chapter, "pair": cmd_pair,
            "terms": cmd_terms, "find": cmd_find}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
