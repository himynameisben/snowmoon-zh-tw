# /// script
# requires-python = ">=3.11"
# ///
"""第二輪文學編輯（translation/literary-edit/WORKFLOW.md）的資料包產生、驗證與套用工具。

以「錨點對齊」切單位：錨點＝標題、HTML 區塊、分隔線、> 引言、清單；兩個錨點之間的散文段為一個段群。
可編輯單位＝段群（ID：chNN-pAAA~pBBB，原文起訖段號）與 > 引言（ID：chNN-pAAA）。

用法：
  uv run tools/literary_edit.py terms N            列出本章原文出現的 bible 譯名（含避免欄），供撰寫 bible 摘錄
  uv run tools/literary_edit.py plan N [--target 1500]
  uv run tools/literary_edit.py packet N --chunk K --out DIR [--target 1500] [--note 文字] [--bible 檔案] [--no-draft]
                                                  --no-draft：不附初譯，editor 直接從英文寫（reviewer 仍用完整資料包）
  uv run tools/literary_edit.py validate N FILE [--bible 檔案] [--report 輸出檔]
                                                  檢查 editor 輸出（<edited> 區塊）。ERROR 為結構問題；
                                                  WARN 為用詞漂移（bible 譯名消失、避免用語出現、初譯常用詞消失），
                                                  --report 把 WARN 寫成給 reviewer 的「用詞差異表」
  uv run tools/literary_edit.py apply N FILE        驗證通過後寫回 zh-tw/chapter-NN.md
"""

import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("check", ROOT / "tools" / "check.py")
check = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check)


def load(n: int):
    en_b = check.blocks(check.en_path(n).read_text(encoding="utf-8"))
    zh_b = check.blocks(check.zh_path(n).read_text(encoding="utf-8"))
    _, units = check.align(en_b, zh_b, force_anchor=True)
    if not units:
        sys.exit(f"第 {n} 章錨點對不上，先跑 check.py chapter {n} 修好結構")
    out = []
    for u in units:
        if u["kind"] == "prose":
            m = re.search(r"原文第 (\d+)–(\d+) 段", u["label"])
            lo, hi = int(m.group(1)), int(m.group(2))
            u["id"] = f"ch{n:02d}-p{lo:03d}~p{hi:03d}"
            u["last"] = hi
        else:
            u["id"] = f"ch{n:02d}-p{u['first']:03d}"
            u["last"] = u["first"]
        u["editable"] = u["kind"] in {"prose", "quote"}
        out.append(u)
    return en_b, zh_b, out


def chunks(units, target: int):
    res, cur, size = [], [], 0
    for idx, u in enumerate(units):
        if u["kind"] == "hr" and cur:  # 分隔線是場景切換，一律在此切 chunk
            res.append(cur)
            cur, size = [], 0
            continue
        if not u["editable"]:
            if cur:
                cur.append(idx)
            continue
        c = check.cjk_count(u["zh"])
        if cur and size + c > target:
            res.append(cur)
            cur, size = [], 0
        cur.append(idx)
        size += c
    if cur:
        res.append(cur)
    # 去掉尾端的非編輯單位
    return [[i for i in ch if units[i]["editable"] or any(units[j]["editable"] for j in ch[ch.index(i):])] for ch in res]


def cmd_terms(a):
    en = check.en_path(a.n).read_text(encoding="utf-8")
    zh = check.zh_path(a.n).read_text(encoding="utf-8")
    seen = set()
    for e in check.parse_tables():
        if e["en"] in seen or not check.en_regex(e["en"]).search(en):
            continue
        seen.add(e["en"])
        used = [z for z in e["zh"] if z in zh]
        avoid = f"；避免：{'、'.join(e['avoid'])}" if e["avoid"] else ""
        note = "" if used else "（本章譯文未出現，請確認）"
        print(f"- {e['en']} → {'／'.join(e['zh'])}{avoid}{note}")


def cmd_plan(a):
    _, _, units = load(a.n)
    for k, ch in enumerate(chunks(units, a.target), 1):
        ed = [units[i] for i in ch if units[i]["editable"]]
        size = sum(check.cjk_count(u["zh"]) for u in ed)
        print(f"chunk {k:02d}: {ed[0]['id']} … {ed[-1]['id']}，{len(ed)} 個單位，{size} 字")


def short(s: str) -> str:
    return s if len(s) < 2500 else "（長 SVG 圖表，省略）"


def cmd_packet(a):
    en_b, zh_b, units = load(a.n)
    ch = chunks(units, a.target)[a.chunk - 1]
    ed = [units[i] for i in ch if units[i]["editable"]]
    fixed = [units[i] for i in ch if not units[i]["editable"]]
    lo, hi = units[ch[0]]["first"], units[ch[-1]]["last"]
    parts = [f"章節：chapter-{a.n:02d}\n目標範圍：原文第 {lo}–{hi} 段之間的段群與引言（只有 <draft> 列出的單位可以改）"]
    if a.note:
        parts.append(f"<note>\n{a.note}\n</note>")
    parts.append("<unit_map>\n" + "\n".join(
        f"{u['id']} = " + ("段群（散文）" if u["kind"] == "prose" else "> 引言錨點") for u in ed) + "\n</unit_map>")
    parts.append("<source>\n" + "\n".join(f"--- {u['id']} ---\n{u['en']}" for u in ed) + "\n</source>")
    if a.no_draft:
        parts.append("<draft>\n（本資料包刻意不附初譯。請直接從 <source> 寫出繁中版本，輸出時沿用 <source> 的定位標記與順序；"
                     "固定譯名、稱謂與單位以 <relevant_bible> 為準。）\n</draft>")
    else:
        parts.append("<draft>\n" + "\n".join(f"--- {u['id']} ---\n{u['zh']}" for u in ed) + "\n</draft>")
    if fixed:
        parts.append("<fixed_in_range>\n範圍內的 HTML 區塊、分隔線、標題；只供理解，不可改、不要輸出：\n" + "\n\n".join(
            f"[{u['id']}]\nEN: {short(u['en'])}\nZH: {short(u['zh'])}" for u in fixed) + "\n</fixed_in_range>")
    def ctx(rng):
        return "\n\n".join(f"[ch{a.n:02d}-p{i:03d}]\nEN: {short(en_b[i - 1])}" for i in rng)
    parts.append("<context_before>\n只供理解，不可改（原文；譯文請看前一個 chunk）\n" + ctx(range(max(1, lo - 2), lo)) + "\n</context_before>")
    parts.append("<context_after>\n只供理解，不可改（原文）\n" + ctx(range(hi + 1, min(len(en_b), hi + 2) + 1)) + "\n</context_after>")
    if a.bible:
        parts.append("<relevant_bible>\n" + Path(a.bible).read_text(encoding="utf-8") + "\n</relevant_bible>")
    out = Path(a.out) / f"chunk-{a.chunk:02d}{'.nodraft' if a.no_draft else ''}.packet.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n\n".join(parts) + "\n", encoding="utf-8")
    print(f"wrote {out}（{len(ed)} 個單位：{ed[0]['id']} … {ed[-1]['id']}）")


def parse_edited(path: str) -> dict[str, str]:
    text = Path(path).read_text(encoding="utf-8")
    m = re.search(r"<edited>(.*?)</edited>", text, re.S)
    body = m.group(1) if m else text
    parts = re.split(r"^--- (ch\d{2}-p\d{3}(?:~p\d{3})?) ---[ \t]*$", body, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def validate(n: int, path: str):
    _, _, units = load(n)
    by_id = {u["id"]: u for u in units}
    got = parse_edited(path)
    errs = []
    for uid, new in got.items():
        u = by_id.get(uid)
        if not u or not u["editable"]:
            errs.append(f"{uid}：不是可編輯單位")
            continue
        nb = check.blocks(new)
        if not nb:
            errs.append(f"{uid}：內容是空的")
            continue
        kinds = {check.kind(b) for b in nb}
        want = {"prose"} if u["kind"] == "prose" else {"quote"}
        if kinds != want:
            errs.append(f"{uid}：產生了不該有的區塊種類 {kinds - want}（段群只能是散文段，引言只能是 > 區塊）")
        if u["kind"] == "quote" and len(nb) != 1:
            errs.append(f"{uid}：引言錨點被拆成 {len(nb)} 段")
        if check.TAG.findall(new) != check.TAG.findall(u["zh"]):
            errs.append(f"{uid}：HTML 標籤改變")
        if new.count("*") != u["zh"].count("*"):
            errs.append(f"{uid}：*強調* 數量改變（{u['zh'].count('*')} → {new.count('*')}）")
        if sorted(re.findall(r"\d+(?:[.,]\d+)?", new)) != sorted(re.findall(r"\d+(?:[.,]\d+)?", u["zh"])):
            errs.append(f"{uid}：阿拉伯數字改變（請人工確認）")
        extra = set(re.findall(r"[A-Za-z]{2,}", new)) - set(re.findall(r"[A-Za-z]{2,}", u["zh"]))
        if extra:
            errs.append(f"{uid}：新出現英文 {sorted(extra)}")
    return units, got, errs


FUNC = set("的了是在和也都就他她它我你們這那一不有個著把被讓說得地很要會到來去上下裡中而與及或但又再才只還已")


def grams(s: str) -> set[str]:
    out = set()
    for run in re.findall(r"[一-鿿]+", s):
        for k in (2, 3):
            for i in range(len(run) - k + 1):
                g = run[i:i + k]
                if not set(g) & FUNC:
                    out.add(g)
    return out


def vocab_warnings(units, got, bible_text: str = "") -> list[str]:
    """用詞漂移提示：不是錯誤，交給主 Agent 與 reviewer 判斷。"""
    by_id = {u["id"]: u for u in units}
    entries = check.parse_tables()
    prose = [u["zh"] for u in units if u["editable"]]
    df: dict[str, int] = {}
    for z in prose:
        for g in grams(z):
            df[g] = df.get(g, 0) + 1
    bible_g = grams(bible_text)
    warns = []
    for uid, new in got.items():
        u = by_id.get(uid)
        if not u:
            continue
        for e in entries:
            if not check.en_regex(e["en"]).search(u["en"]):
                continue
            if any(z in u["zh"] for z in e["zh"]) and not any(z in new for z in e["zh"]):
                warns.append(f"{uid}：bible 譯名消失「{'／'.join(e['zh'])}」（{e['en']}）")
            for av in e["avoid"]:
                if av in new and av not in u["zh"]:
                    warns.append(f"{uid}：出現 bible 列為避免的譯法「{av}」（{e['en']} → {'／'.join(e['zh'])}）")
        lost = sorted(g for g in grams(u["zh"]) - grams(new) if df.get(g, 0) >= 2 or g in bible_g)
        lost = [g for g in lost if not (len(g) == 3 and (g[:2] in lost or g[1:] in lost))]
        for g in lost:
            i = u["zh"].find(g)
            ctx = re.sub(r"\s+", " ", u["zh"][max(0, i - 8):i + len(g) + 8])
            warns.append(f"{uid}：初譯用詞「{g}」不見了（初譯：…{ctx}…）")
    return warns


def cmd_validate(a):
    units, got, errs = validate(a.n, a.file)
    print("\n".join(f"ERROR {e}" for e in errs) if errs else f"OK：{len(got)} 個單位")
    bible_text = Path(a.bible).read_text(encoding="utf-8") if a.bible else ""
    warns = vocab_warnings(units, got, bible_text)
    for w in warns:
        print(f"WARN  {w}")
    if a.report:
        body = "\n".join(f"- {w}" for w in warns) or "- （無）"
        Path(a.report).write_text(
            "# 用詞差異表（tools/literary_edit.py 自動產生）\n\n"
            "以下是編輯稿相對初譯的用詞變動：bible 譯名消失、避免用語出現、全章重複出現或 bible 摘錄裡的詞不見了。\n"
            "大多數是正常的改寫；請逐條判斷是否造成一致性問題（同一事物在全章／全書叫法不同）或漏譯"
            "（例如限定語、程度副詞被拿掉）。只把真的有問題的列為 ISSUE。\n\n" + body + "\n", encoding="utf-8")
    return 1 if errs else 0


def cmd_apply(a):
    units, got, errs = validate(a.n, a.file)
    if errs:
        print("拒絕套用：\n" + "\n".join(errs))
        return 1
    out = [got.get(u["id"], u["zh"]) for u in units if u["zh"].strip()]
    check.zh_path(a.n).write_text("\n\n".join(out) + "\n", encoding="utf-8")
    print(f"已套用 {len(got)} 個單位到 {check.zh_path(a.n).relative_to(ROOT)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("terms"); p.add_argument("n", type=int)
    p = sub.add_parser("plan"); p.add_argument("n", type=int); p.add_argument("--target", type=int, default=1500)
    p = sub.add_parser("packet"); p.add_argument("n", type=int); p.add_argument("--chunk", type=int, required=True)
    p.add_argument("--out", required=True); p.add_argument("--target", type=int, default=1500)
    p.add_argument("--note"); p.add_argument("--bible"); p.add_argument("--no-draft", action="store_true")
    p = sub.add_parser("validate"); p.add_argument("n", type=int); p.add_argument("file")
    p.add_argument("--bible"); p.add_argument("--report")
    p = sub.add_parser("apply"); p.add_argument("n", type=int); p.add_argument("file")
    a = ap.parse_args()
    return {"terms": cmd_terms, "plan": cmd_plan, "packet": cmd_packet, "validate": cmd_validate, "apply": cmd_apply}[a.cmd](a) or 0


if __name__ == "__main__":
    sys.exit(main())
