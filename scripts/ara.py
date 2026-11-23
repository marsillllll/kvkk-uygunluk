#!/usr/bin/env python3
"""KVKK Kurul karar özetlerinde arama (skill'in emsal bulma aracı).

Örnekler:
  python3 scripts/ara.py açık rıza üyelik            # kelimeler birlikte aranır (VE)
  python3 scripts/ara.py "meşru menfaat" -sigorta    # tam ifade, dışlama
  python3 scripts/ara.py --konu çerez --ceza-var     # konuya göre, yalnız cezalılar
  python3 scripts/ara.py --madde 12 --yil 2024       # ihlal edilen madde + yıl
  python3 scripts/ara.py --sektor sağlık --sirala ceza
  python3 scripts/ara.py --kaynak ilke               # yalnız ilke kararları (bağlayıcı genel kurallar)
  python3 scripts/ara.py --son 15                    # en son yayımlanan 15 karar
  python3 scripts/ara.py --no 2024/1393 --tam        # kararın tam metni
  python3 scripts/ara.py --konular                   # konu / sektör listeleri ve sayıları

Çıktı kısa tutulur; bir karara dayanmadan önce `--no <sayı> --tam` ile tam metni okuyun.
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
VERI = KOK / "data" / "kararlar.jsonl"
METIN = KOK / "data" / "metin"

HARF = str.maketrans({"â": "a", "î": "i", "û": "u", "ş": "s", "ğ": "g", "ç": "c", "ö": "o", "ü": "u",
                      "ı": "i", "İ": "i", "I": "i", "Ş": "s", "Ğ": "g", "Ç": "c", "Ö": "o", "Ü": "u",
                      "Â": "a", "Î": "i", "Û": "u", "’": "'", "‘": "'", "“": '"', "”": '"'})


def sade(s):
    return (s or "").translate(HARF).lower()


def yukle():
    if not VERI.exists():
        sys.exit(f"Veri yok: {VERI}. Önce `python3 scripts/guncelle.py` çalıştırın.")
    return [json.loads(l) for l in VERI.read_text(encoding="utf-8").splitlines() if l.strip()]


def tam_metin(k):
    f = METIN / f"{k['id']}.txt"
    return f.read_text(encoding="utf-8") if f.exists() else ""


def tl(n):
    return f"{int(n):,}".replace(",", ".") + " TL" if n else ""


def tarih(iso):
    return ".".join(reversed(iso.split("-"))) if iso else "tarih yok"


def yaz_kisa(k, terimler, kesit=True):
    ceza = sum(c["tutar"] for c in k.get("cezalar", []))
    kt = k.get("kaynakTuru", "Karar özeti")
    print(f"■ {k.get('no') or '(sayı yok)'} · {tarih(k.get('tarih'))} · {kt.upper() if kt != 'Karar özeti' else k.get('tur')} · {k.get('sektor')}"
          + (f" · CEZA {tl(ceza)}" if ceza else ""))
    print(f"  Konu: {k.get('konu')}")
    print(f"  Sonuç: {', '.join(k.get('sonuclar', []))}"
          + (f" · İhlal: {', '.join('m.' + str(m) for m in k['ihlalMaddeleri'])}" if k.get("ihlalMaddeleri") else ""))
    if k.get("ilke"):
        print(f"  İlke: {k['ilke']}")
    if kesit and terimler:
        m = tam_metin(k)
        s = sade(m)
        i = min([p for p in (s.find(t) for t in terimler) if p >= 0], default=-1)
        if i >= 0:
            a, b = max(0, i - 120), min(len(m), i + 260)
            print("  Metinden: …" + re.sub(r"\s+", " ", m[a:b]) + "…")
    print(f"  Kaynak: {k.get('url')}  (id {k['id']})")
    print()


def yaz_tam(k):
    ceza = k.get("cezalar", [])
    print("=" * 78)
    print(f"BELGE TÜRÜ: {k.get('kaynakTuru', 'Karar özeti')}" + ("  (metin OCR ile çıkarıldı; yazım hatası olabilir)" if k.get("ocr") else ""))
    print(f"KARAR NO: {k.get('no')}   KARAR TARİHİ: {tarih(k.get('tarih'))}   YAYIN: {tarih(k.get('yayin'))}")
    print(f"BAŞLIK: {k.get('baslik')}")
    print(f"TÜR: {k.get('tur')}   SEKTÖR: {k.get('sektor')}   VERİ SORUMLUSU: {k.get('veriSorumlusu')}")
    print(f"SONUÇ: {', '.join(k.get('sonuclar', []))}")
    for c in ceza:
        print(f"CEZA: {tl(c['tutar'])} — {c.get('gerekce', '')}")
    if k.get("ihlalMaddeleri"):
        print("İHLAL EDİLEN MADDELER: " + ", ".join("m." + str(m) for m in k["ihlalMaddeleri"]))
    print(f"KONULAR: {', '.join(k.get('konular', []))}")
    print(f"ÖZET (otomatik): {k.get('ozet')}")
    print(f"İLKE (otomatik): {k.get('ilke')}")
    for c in k.get("kontrol", []):
        print(f"KONTROL: {c}")
    print(f"KAYNAK: {k.get('url')}" + (f"   ARŞİV: {k['arsiv']}" if k.get("arsiv") else ""))
    print("-" * 78)
    m = tam_metin(k)
    print(m.split("\n\n", 1)[1] if "\n\n" in m else m)
    print()


def main():
    p = argparse.ArgumentParser(description="KVKK Kurul karar özetlerinde arama")
    p.add_argument("terimler", nargs="*", help='aranacak kelimeler; "tam ifade"; -dışla')
    p.add_argument("--konu", action="append", default=[], help="konu adının bir parçası (yinelenebilir, VE)")
    p.add_argument("--sektor", help="sektör adının bir parçası")
    p.add_argument("--madde", type=int, action="append", default=[], help="ihlal edilen Kanun maddesi (yinelenebilir)")
    p.add_argument("--yil", action="append", default=[], help="karar yılı (yinelenebilir, VEYA)")
    p.add_argument("--kaynak", help="belge türünün bir parçası: ilke, kurul, özet")
    p.add_argument("--tur", help="inceleme türünün bir parçası (şikâyet, ihlal, resen, ihbar)")
    p.add_argument("--sonuc", help="sonucun bir parçası (ceza, talimat, ihlal yok ...)")
    p.add_argument("--ceza-var", action="store_true", help="yalnız idari para cezası verilenler")
    p.add_argument("--ceza-min", type=int, default=0, help="toplam ceza alt sınırı (TL)")
    p.add_argument("--no", action="append", default=[], help="karar sayısı (ör. 2024/1393)")
    p.add_argument("--id", type=int, action="append", default=[], help="karar id")
    p.add_argument("--son", type=int, help="yayın tarihine göre en yeni N karar")
    p.add_argument("--sirala", choices=["alaka", "tarih", "yayin", "ceza"], default=None)
    p.add_argument("--limit", type=int, default=12)
    p.add_argument("--tam", action="store_true", help="tam metni yazdır")
    p.add_argument("--json", action="store_true", help="eşleşenleri JSON satırları olarak yaz")
    p.add_argument("--konular", action="store_true", help="konu, sektör, yıl dağılımını göster")
    a = p.parse_args()

    K = yukle()
    if a.konular:
        for ad, al in (("KONULAR", lambda k: k.get("konular", [])), ("SEKTÖRLER", lambda k: [k.get("sektor")]),
                       ("YILLAR", lambda k: [(k.get("tarih") or k.get("no") or "?")[:4]]),
                       ("SONUÇLAR", lambda k: k.get("sonuclar", []))):
            c = Counter(x for k in K for x in al(k) if x)
            print(ad)
            for x, n in sorted(c.items(), key=lambda t: (-t[1], t[0])) if ad != "YILLAR" else sorted(c.items(), reverse=True):
                print(f"  {n:4d}  {x}")
            print()
        print(f"Toplam {len(K)} karar. Rehber dosyaları: references/konular/")
        return

    dahil, haric = [], []
    for t in a.terimler:
        (haric if t.startswith("-") and len(t) > 1 else dahil).append(sade(t.lstrip("-") if t.startswith("-") else t))

    sonuc = []
    for k in K:
        if a.no and (k.get("no") or "") not in a.no:
            continue
        if a.id and k["id"] not in a.id:
            continue
        if any(sade(x) not in sade(" | ".join(k.get("konular", []))) for x in a.konu):
            continue
        if a.sektor and sade(a.sektor) not in sade(k.get("sektor")):
            continue
        if a.madde and not set(a.madde) <= set(k.get("ihlalMaddeleri", [])):
            continue
        if a.yil and (k.get("tarih") or k.get("no") or "")[:4] not in a.yil:
            continue
        if a.kaynak and sade(a.kaynak) not in sade(k.get("kaynakTuru", "Karar özeti")):
            continue
        if a.tur and sade(a.tur) not in sade(k.get("tur")):
            continue
        if a.sonuc and sade(a.sonuc) not in sade(" | ".join(k.get("sonuclar", []))):
            continue
        ceza = sum(c["tutar"] for c in k.get("cezalar", []))
        if (a.ceza_var and not ceza) or ceza < a.ceza_min:
            continue
        puan = 0.0
        if dahil or haric:
            ust = sade(" ".join([k.get("konu", ""), k.get("baslik", ""), k.get("no", ""), k.get("ozet", ""), k.get("ilke", ""),
                                 " ".join(k.get("anahtar", [])), " ".join(k.get("kontrol", [])), k.get("veriSorumlusu", "")]))
            govde = sade(tam_metin(k))
            if any(t in ust or t in govde for t in haric):
                continue
            if any(t not in ust and t not in govde for t in dahil):
                continue
            puan = sum(6 * (t in ust) + min(govde.count(t), 12) * 0.5 for t in dahil)
        sonuc.append((puan, ceza, k))

    sira = a.sirala or ("yayin" if a.son else "alaka" if dahil else "tarih")
    if sira == "alaka":
        sonuc.sort(key=lambda t: (t[0], t[2].get("tarih") or ""), reverse=True)
    elif sira == "ceza":
        sonuc.sort(key=lambda t: t[1], reverse=True)
    elif sira == "yayin":
        sonuc.sort(key=lambda t: (t[2].get("yayin") or "", t[2].get("tarih") or ""), reverse=True)
    else:
        sonuc.sort(key=lambda t: t[2].get("tarih") or "", reverse=True)

    limit = a.son or a.limit
    goster = sonuc[:limit]
    if a.json:
        for _, _, k in goster:
            print(json.dumps(k, ensure_ascii=False))
        return
    print(f"{len(sonuc)} karar eşleşti" + (f", ilk {len(goster)} gösteriliyor ({sira} sırasıyla)" if len(sonuc) > len(goster) else f" ({sira} sırasıyla)") + ".\n")
    for _, _, k in goster:
        if a.tam:
            yaz_tam(k)
        else:
            yaz_kisa(k, dahil)


if __name__ == "__main__":
    main()
