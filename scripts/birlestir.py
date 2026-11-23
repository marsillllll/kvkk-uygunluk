#!/usr/bin/env python3
"""data/analiz/parca/*.json -> data/analiz.json (id -> analiz). Alanları doğrular, temizler."""
import json, re, sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent / "data"
TUR = {"Şikâyet", "İhbar", "Veri ihlali bildirimi", "Resen inceleme", "Diğer"}
SONUC = {"İdari para cezası", "Talimat", "İhlal yok / işlem yapılmasına yer yok", "Hatırlatma / uyarı",
         "Disiplin hükümleri (kamu)", "Savcılığa bildirim", "Kanun kapsamı dışında / incelenemez",
         "İlke / genel düzenleme", "Diğer"}


def rakam(s):
    return re.sub(r"\D", "", s)


def main():
    kararlar = {k["id"]: k for k in json.loads((KOK / "kararlar.json").read_text(encoding="utf-8"))["kararlar"]}
    eski_yol = KOK / "analiz.json"
    cikti = json.loads(eski_yol.read_text(encoding="utf-8")) if eski_yol.exists() else {}
    uyari = []
    for f in sorted((KOK / "analiz" / "parca").glob("*.json")):
        try:
            dizi = json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            uyari.append(f"{f.name}: okunamadı ({e})")
            continue
        for a in dizi:
            try:
                kid = int(a.get("id"))
            except Exception:
                uyari.append(f"{f.name}: id yok")
                continue
            if kid not in kararlar:
                uyari.append(f"{f.name}: bilinmeyen id {kid}")
                continue
            metin = (KOK / "metin" / f"{kid}.txt").read_text(encoding="utf-8")
            mr = rakam(metin)
            cezalar = []
            for c in a.get("cezalar") or []:
                try:
                    t = int(round(float(c.get("tutar"))))
                except Exception:
                    continue
                if t <= 0:
                    continue
                if str(t) not in mr:
                    uyari.append(f"{kararlar[kid]['no'] or kid}: ceza tutarı metinde bulunamadı: {t}")
                    continue
                cezalar.append({"tutar": t, "gerekce": str(c.get("gerekce") or "").strip()})
            sonuclar = [s for s in (a.get("sonuclar") or []) if s in SONUC]
            if cezalar and "İdari para cezası" not in sonuclar:
                sonuclar.insert(0, "İdari para cezası")
            if not cezalar and "İdari para cezası" in sonuclar and not re.search(r"idari para cezası", metin, re.I):
                sonuclar.remove("İdari para cezası")
            maddeler = sorted({int(m) for m in (a.get("ihlalMaddeleri") or []) if str(m).isdigit() and 1 <= int(m) <= 33 and int(m) != 18})
            tur = a.get("tur") if a.get("tur") in TUR else "Diğer"
            cikti[str(kid)] = {
                "tur": tur,
                "sektor": str(a.get("sektor") or "Diğer").strip(),
                "veriSorumlusu": str(a.get("veriSorumlusu") or "").strip(),
                "sonuclar": sonuclar or ["Diğer"],
                "cezalar": cezalar,
                "ihlalMaddeleri": maddeler,
                "konular": [str(x).strip() for x in (a.get("konular") or []) if str(x).strip()],
                "ozet": str(a.get("ozet") or "").strip(),
                "ilke": str(a.get("ilke") or "").strip(),
                "kontrol": [str(x).strip() for x in (a.get("kontrol") or []) if str(x).strip()],
                "anahtar": [str(x).strip() for x in (a.get("anahtar") or []) if str(x).strip()],
                "tarih": str(a.get("tarih") or "") if re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(a.get("tarih") or "")) else "",
            }
    eski_yol.write_text(json.dumps(cikti, ensure_ascii=False, indent=0), encoding="utf-8")
    eksik = [k for k in kararlar if str(k) not in cikti]
    print(f"analiz.json: {len(cikti)} karar; eksik {len(eksik)}: {eksik[:20]}")
    print(f"{len(uyari)} uyarı")
    for u in uyari:
        print("  ", u)


if __name__ == "__main__":
    main()
