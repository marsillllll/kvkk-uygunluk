#!/usr/bin/env python3
"""data/kararlar.jsonl -> references/konular/*.md (konu rehberleri) + INDEX.md

Rehberler elle yazılmaz; denetlenmiş yapılandırılmış veriden üretilir. guncelle.py her çalıştığında yenilenir.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
HEDEF = KOK / "references" / "konular"
TR = str.maketrans("çğıöşüâîûÇĞİÖŞÜ", "cgiosuaiuCGIOSU")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.translate(TR).lower()).strip("-")


def tl(n):
    return f"{int(n):,}".replace(",", ".") + " TL"


def tarih(iso):
    return ".".join(reversed(iso.split("-"))) if iso else "tarih yok"


def atif(k):
    return f"{tarih(k.get('tarih'))} tarihli ve {k.get('no') or '(sayısız)'} sayılı"


def main():
    K = [json.loads(l) for l in (KOK / "data" / "kararlar.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    grup = defaultdict(list)
    for k in K:
        if not k.get("analizVar"):
            continue
        for konu in k.get("konular", []):
            grup[konu].append(k)
    HEDEF.mkdir(parents=True, exist_ok=True)
    for f in HEDEF.glob("*.md"):
        f.unlink()
    satirlar = []
    for konu, liste in sorted(grup.items(), key=lambda t: -len(t[1])):
        if len(liste) < 2 or konu == "Diğer":
            continue
        liste.sort(key=lambda k: k.get("tarih") or "", reverse=True)
        genel = [k for k in liste if k.get("kaynakTuru") != "Karar özeti"]
        ozet = [k for k in liste if k.get("kaynakTuru") == "Karar özeti"]
        cezali = [k for k in ozet if k.get("cezalar")]
        ihlalsiz = [k for k in ozet if any("İhlal yok" in s or "kapsamı dışında" in s for s in k.get("sonuclar", [])) and not k.get("cezalar")]
        madde = Counter(m for k in liste for m in k.get("ihlalMaddeleri", []))
        o = [f"# {konu}", "",
             f"{len(liste)} belge: {len(genel)} ilke/genel nitelikli Kurul kararı, {len(ozet)} karar özeti "
             f"({len(cezali)} tanesinde idari para cezası, {len(ihlalsiz)} tanesinde ihlal bulunmadı ya da incelenmedi).",
             "En sık ihlal bulunan maddeler: " + (", ".join(f"m.{m} ({n})" for m, n in madde.most_common(5)) or "—") + ".", "",
             "> Bu dosya yapılandırılmış veriden otomatik üretilir. \"İlke\" ve \"Bakılacaklar\" satırları yapay zekâ ile çıkarılıp "
             "ikinci geçişte denetlenmiştir; bir karara dayanmadan önce `python3 scripts/ara.py --no <sayı> --tam` ile tam metni okuyun. "
             "Aynı konuda yeni tarihli karar eskisini değiştirmiş ya da daraltmış olabilir: yukarıdan aşağı (yeniden eskiye) okuyun.", ""]
        if genel:
            o += ["## İlke kararları ve genel nitelikli Kurul kararları", "",
                  "Bunlar tek bir olaya değil tüm veri sorumlularına (ya da bir sektöre) yöneliktir; değerlendirmeye buradan başlayın.", ""]
            for k in genel:
                o += [f"### {k.get('no')} · {tarih(k.get('tarih'))} · {k.get('kaynakTuru')}", "",
                      f"**{k.get('konu')}**", "", k.get("ilke") or k.get("ozet") or "", ""]
                o += [f"- {c}" for c in k.get("kontrol", [])]
                o += ["", f"Kaynak: {k.get('url')}", ""]
        if cezali:
            o += ["## İdari para cezası verilen kararlar", "",
                  "Tutarlar kararın verildiği yılın sınırlarına göredir; bugünkü risk olarak sunmayın.", ""]
            for k in cezali:
                cz = "; ".join(f"{tl(c['tutar'])} ({c.get('gerekce') or 'gerekçe belirtilmemiş'})" for c in k["cezalar"])
                o += [f"- **{k.get('no')}** ({tarih(k.get('tarih'))}, {k.get('sektor')}) — {k.get('ilke') or k.get('ozet')} *Ceza:* {cz}"]
            o += [""]
        diger = [k for k in ozet if not k.get("cezalar") and k not in ihlalsiz]
        if diger:
            o += ["## Talimat, uyarı ve diğer sonuçlar", ""]
            o += [f"- **{k.get('no')}** ({tarih(k.get('tarih'))}, {k.get('sektor')}; {', '.join(k.get('sonuclar', []))}) — {k.get('ilke') or k.get('ozet')}" for k in diger]
            o += [""]
        if ihlalsiz:
            o += ["## İhlal bulunmayan ya da incelenmeyen kararlar", "",
                  "Lehe emsal ararken buraya bakın; olgu farkını tam metinden doğrulayın.", ""]
            o += [f"- **{k.get('no')}** ({tarih(k.get('tarih'))}, {k.get('sektor')}) — {k.get('ilke') or k.get('ozet')}" for k in ihlalsiz]
            o += [""]
        kontroller = [(c, k) for k in liste[:60] for c in k.get("kontrol", [])]
        if kontroller:
            o += ["## Bakılacaklar (kararlardan çıkan kontrol maddeleri)", ""]
            o += [f"- {c} *({k.get('no')})*" for c, k in kontroller[:70]]
            o += [""]
        ad = slug(konu) + ".md"
        (HEDEF / ad).write_text("\n".join(o), encoding="utf-8")
        satirlar.append(f"| [{konu}]({ad}) | {len(liste)} | {len(genel)} | {len(cezali)} |")
    (HEDEF / "INDEX.md").write_text("\n".join([
        "# Konu rehberleri", "",
        "Her dosya: önce ilke kararları, sonra cezalı kararlar, diğer sonuçlar, ihlal bulunmayanlar ve kontrol maddeleri.", "",
        "| Konu | Belge | İlke/genel karar | Cezalı karar |", "|---|---|---|---|", *satirlar, ""]), encoding="utf-8")
    print(f"{len(satirlar)} konu rehberi yazıldı")


if __name__ == "__main__":
    main()
