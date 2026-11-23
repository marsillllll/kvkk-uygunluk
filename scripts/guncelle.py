#!/usr/bin/env python3
"""KVKK Kurul Karar Özetleri -> data/ -> arac/kvkk-kararlar.html

Kullanım:  python3 scripts/guncelle.py               (yalnız yeni kararları indirir)
           python3 scripts/guncelle.py --hepsi       (önbelleği yok sayar, hepsini yeniden indirir)
           python3 scripts/guncelle.py --indirme-yok (ağa çıkmaz; data/kararlar.json + data/analiz.json'dan
                                                      çıktıları yeniden üretir)

Yalnız standart kütüphane kullanır. Sunucuyu yormamak için istekler sıralı ve
aralıklıdır.
"""
import html
import json
import re
import sys
import time
import shutil
import subprocess
import zlib
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))

KOK = Path(__file__).resolve().parent.parent
DATA = KOK / "data"
ONBELLEK = DATA / "onbellek"
LISTE_URL = "https://www.kvkk.gov.tr/Icerik/5406/kurul-karar-ozetleri?page={}"
# Öncelik sırasıyla: aynı içerik birden çok listede varsa ilk görülen tür geçerli olur.
KAYNAKLAR = [
    ("İlke kararı", "https://www.kvkk.gov.tr/Icerik/7201/ilke-kararlari?page={}"),
    ("Kurul kararı", "https://www.kvkk.gov.tr/Icerik/5419/kurul-kararlari?page={}"),
    ("Karar özeti", LISTE_URL),
]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
BEKLE = 0.35

IZINLI = {"p", "ul", "ol", "li", "strong", "b", "em", "i", "u", "br", "table", "tbody",
          "thead", "tr", "td", "th", "h3", "h4", "h5", "blockquote", "sup", "sub"}
BOS = {"br"}


def kimlik(url):
    """Kurum sitesindeki içerik numarası; dış bağlantılar (Resmî Gazete PDF) için sabit sentetik numara."""
    m = re.search(r"kvkk\.gov\.tr/Icerik/(\d+)", url)
    return int(m.group(1)) if m else 9_000_000 + zlib.crc32(url.encode()) % 900_000


def indir_dosya(url, hedef, deneme=4):
    for i in range(deneme):
        try:
            subprocess.run(["curl", "-sS", "-L", "--fail", "--max-time", "120", "-A", UA, "-o", str(hedef), url], check=True)
            return
        except Exception:
            if i == deneme - 1:
                raise
            time.sleep(2 + 3 * i)


def pdf_metni(pdf, kid):
    """PDF -> düz metin. Önce metin katmanı (pdftotext); taranmış PDF ise macOS Vision OCR (scripts/ocr.swift).
    Sonuç data/pdf-metin/<id>.txt içinde saklanır; OCR aracı olmayan ortamda bu dosya depodan gelir."""
    hedef = DATA / "pdf-metin" / f"{kid}.txt"
    if hedef.exists() and hedef.stat().st_size > 400:
        return hedef.read_text(encoding="utf-8"), hedef.read_text(encoding="utf-8").startswith("[OCR]")
    hedef.parent.mkdir(parents=True, exist_ok=True)
    metin, ocr = "", False
    if shutil.which("pdftotext"):
        metin = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True).stdout.decode("utf-8", "replace")
    if len(re.sub(r"\s", "", metin)) < 600 and shutil.which("swift") and sys.platform == "darwin":
        r = subprocess.run(["swift", str(KOK / "scripts" / "ocr.swift"), str(pdf)], capture_output=True)
        metin, ocr = r.stdout.decode("utf-8", "replace"), True
    if len(re.sub(r"\s", "", metin)) < 600:
        return "", False
    if ocr:
        metin = "[OCR]\n" + metin
    hedef.write_text(metin, encoding="utf-8")
    return metin, ocr


def pdf_coz(metin, url, baslik, ocr):
    metin = metin.replace("[OCR]\n", "", 1)
    satirlar = []
    for l in metin.splitlines():
        l = l.strip()
        if not l or re.fullmatch(r"-+ sayfa \d+ -+", l) or re.fullmatch(r"Sayfa\s*:?\s*\d+|\d{1,3}", l):
            continue
        if re.fullmatch(r"Resm[iî] Gazete|RESM[İI] GAZETE|Sayı\s*:\s*\d+|KURUL KARARI|\d{1,2} \S+ \d{4} [A-ZÇĞİÖŞÜ]+", l):
            continue
        satirlar.append(l)
    paragraflar, cur = [], ""
    for l in satirlar:
        yeni = bool(re.match(r"^(?:[•\-–▪■]|\d{1,2}[.)]\s|[a-zçğıöşü]\)\s|Karar No|Karar Tarihi)", l))
        if cur and (yeni or (re.search(r"[.:;]$", cur) and len(cur.rsplit(" ", 12)[-1]) >= 0 and re.match(r"^[A-ZÇĞİÖŞÜ0-9\"“(]", l) and cur.endswith("."))):
            paragraflar.append(cur)
            cur = l
        else:
            cur = (cur[:-1] if cur.endswith("-") and l[:1].islower() else cur + " " if cur else "") + l
    if cur:
        paragraflar.append(cur)
    govde = "".join("<p>" + html.escape(x, quote=False) + "</p>" for x in paragraflar)
    duzm = "\n".join(paragraflar)
    mno = re.search(r"Karar No\s*:?\s*(\d{4})\s*/\s*(\d{1,4})", duzm) or re.search(r"(\d{4})\s*/\s*(\d{1,4})\s*sayılı", baslik, re.I)
    mt = re.search(r"Karar Tarihi\s*:?\s*(\d{1,2}\s*[./]\s*\d{1,2}\s*[./]\s*\d{4})", duzm) or re.search(r"(\d{1,2}\s*[./]\s*\d{1,2}\s*[./]\s*\d{4})\s*tarih", baslik, re.I)
    my = re.search(r"/(\d{4})/(\d{2})/\d{4}\d{2}(\d{2})", url)
    mk, bk = kucuk(duzm), kucuk(baslik)
    cz = cezalar(duzm)
    konu = re.sub(r"\s*(?:Hakkında|İlişkin|ile ilgili)?\s*Kişisel Verileri Koruma Kurulunun.*$", "", baslik, flags=re.I).strip(" \"“”") or baslik
    return {
        "id": kimlik(url), "url": url, "baslik": baslik, "konu": konu,
        "no": f"{mno.group(1)}/{mno.group(2)}" if mno else "", "tarih": tarih_iso(mt.group(1)) if mt else "",
        "yayin": f"{my.group(1)}-{my.group(2)}-{my.group(3)}" if my else "",
        "tur": tur(mk, bk), "sonuc": sonuc(mk, cz), "ceza": cz, "cezaToplam": sum(cz),
        "maddeler": maddeler(duzm), "konular": [ad for ad, rx in KONULAR if rx.search(mk)],
        "html": govde, "ocr": bool(ocr),
    }


def indir(url, deneme=4):
    for i in range(deneme):
        try:
            # curl sistem sertifika deposunu kullanır; bazı Python kurulumları
            # sitenin sertifika zincirini doğrulayamıyor.
            r = subprocess.run(["curl", "-sS", "-L", "--fail", "--max-time", "60", "-A", UA, url],
                               capture_output=True, check=True)
            return r.stdout.decode("utf-8", errors="replace")
        except Exception as e:  # ağ hatası: bekle, yeniden dene
            if i == deneme - 1:
                raise
            time.sleep(2 + 3 * i)
    return ""


class Makale(HTMLParser):
    """news__detail-article bloğunun içini, temizlenmiş HTML olarak toplar."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.derinlik = 0
        self.icinde = False
        self.baslikta = False
        self.baslik = ""
        self.out = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if not self.icinde:
            sinif = a.get("class") or ""
            if tag == "div" and ("news__detail-article" in sinif or "blog-post-inner" in sinif):
                self.icinde = True
                self.derinlik = 1
            return
        if tag == "div":
            self.derinlik += 1
        sinif = a.get("class") or ""
        if tag in ("h2", "h3") and ("news__detail-article-title" in sinif or "blog-post-title" in sinif):
            self.baslikta = True
            return
        if tag in ("script", "style"):
            return
        if tag in IZINLI:
            ek = ""
            if tag in ("td", "th"):
                for k in ("colspan", "rowspan"):
                    if (a.get(k) or "").isdigit():
                        ek += f' {k}="{a[k]}"'
            self.out.append(f"<{tag}{ek}>")
        elif tag in ("div", "h1", "h2", "h6"):
            self.out.append("<p>")

    def handle_endtag(self, tag):
        if not self.icinde:
            return
        if tag in ("h2", "h3") and self.baslikta:
            self.baslikta = False
            return
        if tag == "div":
            self.derinlik -= 1
            if self.derinlik == 0:
                self.icinde = False
                return
        if tag in IZINLI and tag not in BOS:
            self.out.append(f"</{tag}>")
        elif tag in ("div", "h1", "h2", "h6"):
            self.out.append("</p>")

    def handle_data(self, data):
        if not self.icinde:
            return
        if self.baslikta:
            self.baslik += data
        else:
            self.out.append(html.escape(data, quote=False))


def duz(s):
    s = re.sub(r"<(br|/p|/li|/tr|/h\d)>", "\n", s)
    s = re.sub(r"</td>", " ", s)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    s = s.replace("\xa0", " ")
    return re.sub(r"[ \t]+", " ", re.sub(r"\s*\n\s*", "\n", s)).strip()


def tarih_iso(s):
    m = re.search(r"(\d{1,2})\s*[./]\s*(\d{1,2})\s*[./]\s*(\d{4})", s or "")
    if not m:
        return ""
    g, a, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if not (1 <= g <= 31 and 1 <= a <= 12 and 2016 <= y <= 2100):
        return ""
    return f"{y:04d}-{a:02d}-{g:02d}"


AYLAR = {"ocak": 1, "şubat": 2, "mart": 3, "nisan": 4, "mayıs": 5, "haziran": 6, "temmuz": 7,
         "ağustos": 8, "eylül": 9, "ekim": 10, "kasım": 11, "aralık": 12}


def yayin_iso(sayfa):
    m = re.search(r"Yayınlanma Tarihi:</span>\s*<span>\s*(\d{1,2})\s+(\S+)\s+(\d{4})", sayfa)
    if not m:
        return ""
    ay = AYLAR.get(m.group(2).lower())
    return f"{int(m.group(3)):04d}-{ay:02d}-{int(m.group(1)):02d}" if ay else ""


def sayi(s):
    """'1.250.000' / '250.000,00' / '1 milyon' -> float TL"""
    s = s.strip()
    s = re.sub(r",\d{1,2}$", "", s)
    s = s.replace(".", "").replace(" ", "")
    try:
        return float(s)
    except ValueError:
        return 0.0


CEZA_RE = re.compile(
    r"(\d{1,3}(?:[.\s]\d{3})+(?:,\d{1,2})?|\d{4,})\s*(?:\(|-)?[^()\n]{0,40}?\)?\s*(?:TL|Türk Lirası|lira)[^.\n]{0,160}?idari para cezası",
    re.I)
CEZA_RE2 = re.compile(
    r"idari para cezası[^.\n]{0,120}?(\d{1,3}(?:[.\s]\d{3})+(?:,\d{1,2})?)\s*(?:TL|Türk Lirası)", re.I)


def cezalar(metin):
    bulunan = []
    for m in CEZA_RE.finditer(metin):
        v = sayi(m.group(1))
        if v >= 1000:
            bulunan.append(v)
    if not bulunan:
        for m in CEZA_RE2.finditer(metin):
            v = sayi(m.group(1))
            if v >= 1000:
                bulunan.append(v)
    return bulunan


def tur(metin_k, baslik_k):
    if "veri ihlal" in baslik_k or "ihlal bildirimi" in baslik_k:
        return "Veri ihlali bildirimi"
    if "resen" in baslik_k or "re'sen" in baslik_k:
        return "Resen inceleme"
    if "şikâyet" in baslik_k or "şikayet" in baslik_k or "başvuru" in baslik_k or "ihbar" in baslik_k:
        return "Şikâyet / ihbar"
    bas = metin_k[:1500]
    if "veri ihlal" in bas:
        return "Veri ihlali bildirimi"
    if "şikâyet" in bas or "şikayet" in bas or "ihbar" in bas:
        return "Şikâyet / ihbar"
    if "resen" in bas:
        return "Resen inceleme"
    return "Diğer"


KONULAR = [
    ("Açık rıza", r"açık rıza"),
    ("Aydınlatma yükümlülüğü", r"aydınlatma"),
    ("Veri güvenliği (m.12)", r"veri güvenliği|teknik ve idari tedbir"),
    ("Veri ihlali bildirimi / 72 saat", r"72 saat|ihlal bildirim|veri ihlal"),
    ("Yurt dışına aktarım", r"yurt ?dışına aktar"),
    ("Özel nitelikli veri", r"özel nitelikli"),
    ("Sağlık verisi", r"sağlık veri|hasta |hastane|sağlık bilgi"),
    ("Biyometrik veri", r"biyometrik|parmak izi|yüz tanıma|avuç içi"),
    ("Kamera / görüntü kaydı", r"kamera|görüntü kayd"),
    ("Ses kaydı", r"ses kayd"),
    ("SMS / arama / e-posta ile pazarlama", r"\bsms\b|kısa mesaj|reklam|pazarlama|ticari elektronik ileti"),
    ("Çerez", r"çerez"),
    ("Unutulma hakkı / arama motoru", r"unutulma|arama motor|indeksten"),
    ("Silme / yok etme talebi", r"silinmesi|yok edilmesi|silme taleb"),
    ("İlgili kişi başvurusuna cevap (m.13)", r"başvuruya (?:süresi içinde |süresi içerisinde )?cevap|13 ?üncü madde|otuz gün|30 gün"),
    ("İşçi-işveren ilişkisi", r"işveren|çalışan(?:ın|lar)|işçi|eski çalışan|personel(?:in|e ait)"),
    ("Banka / finans", r"banka|finansman|kredi|varlık yönetim|faktoring|ödeme kuruluş"),
    ("Sigorta", r"sigorta"),
    ("Avukat / icra takibi", r"avukat|icra |vekalet"),
    ("E-ticaret / internet sitesi", r"e-ticaret|elektronik ticaret|internet sitesi|mobil uygulama|platform"),
    ("Telekomünikasyon", r"telekom|gsm|operatör|internet servis sağlayıcı|abonelik"),
    ("Eğitim / okul", r"okul|üniversite|öğrenci|eğitim kurum"),
    ("Kamu kurumu", r"kamu kurum|belediye|bakanlığı|valili|müdürlüğü"),
    ("Site / apartman yönetimi", r"site yönetim|apartman|kat malik"),
    ("Sosyal medya", r"sosyal medya|whatsapp|instagram|facebook|twitter"),
    ("Kimlik / TCKN", r"t\.?c\.? kimlik|kimlik fotokopi|kimlik numaras"),
    ("VERBİS / sicil", r"verbis|sicile kayıt|veri sorumluları sicil"),
    ("Yetkisiz erişim / sorgulama", r"yetkisiz|hukuka aykırı (?:olarak )?eriş|sorgula"),
    ("Siber saldırı / fidye yazılımı", r"siber saldırı|fidye|oltalama|zararlı yazılım|phishing|sızma"),
    ("Basın / ifade özgürlüğü", r"basın|haber|ifade özgürlüğü|gazete"),
    ("Çocuk / yaşı küçük", r"çocuk|yaşı küçük|reşit olmayan|veli"),
    ("Konum verisi", r"konum veri|gps|araç takip"),
    ("Meşru menfaat", r"meşru menfaat"),
    ("Ölçülülük ilkesi", r"ölçülü"),
]
KONULAR = [(ad, re.compile(r)) for ad, r in KONULAR]

MADDE_RE = re.compile(r"kanunun?\s+(?:“[^”]{0,90}”\s+)?(?:başlıklı\s+)?(\d{1,2})\s*(?:’|')?\s*(?:n?c[iıuü]|inci|ıncı|uncu|üncü|üncü)\s+madde", re.I)
MADDE_RE2 = re.compile(r"(\d{1,2})\s*(?:’|')?\s*(?:n?c[iıuü]|inci|ıncı|uncu|üncü)\s+maddesi", re.I)


def kucuk(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


def maddeler(metin):
    s = set()
    for rx in (MADDE_RE, MADDE_RE2):
        for m in rx.finditer(metin):
            n = int(m.group(1))
            if 1 <= n <= 33:
                s.add(n)
    return sorted(s)


def sonuc(metin_k, ceza_list):
    etiket = []
    if ceza_list:
        etiket.append("İdari para cezası")
    if re.search(r"talimat(?:landırıl| veril)", metin_k):
        etiket.append("Talimat")
    if re.search(r"(?:yapılacak|tesis edilecek) (?:bir |herhangi bir )?işlem (?:bulunmadığına|olmadığına)|işlem tesis edilmesine yer olmadığına|işlem yapılmasına yer olmadığına", metin_k):
        etiket.append("İşlem yapılmasına yer yok")
    if re.search(r"disiplin", metin_k) and re.search(r"18 ?inci maddesinin \(?3\)?|ilgili(?:ler)? hakkında disiplin|disiplin hükümleri", metin_k):
        etiket.append("Disiplin hükümleri (kamu)")
    if re.search(r"hatırlatıl|uyarıl|dikkat edilmesi (?:gerektiği|hususunda)|azami dikkat", metin_k):
        etiket.append("Hatırlatma / uyarı")
    if re.search(r"suç duyurusu|cumhuriyet başsavcılığı", metin_k):
        etiket.append("Savcılığa bildirim")
    if not etiket:
        etiket.append("Belirlenemedi")
    return etiket


def detay_coz(sayfa, url, liste_baslik):
    p = Makale()
    p.feed(sayfa)
    govde = "".join(p.out)
    govde = re.sub(r"<(p|li|td|strong|b|em|i|u|h\d)>\s*</\1>", "", govde)
    govde = re.sub(r"\n{2,}", "\n", govde).strip()
    baslik = re.sub(r"\s+", " ", p.baslik).strip() or liste_baslik
    metin = duz(govde)

    def satir(ad):
        m = re.search(ad + r"\s*</(?:strong|b)>\s*</td>\s*<td>\s*:?\s*</td>\s*<td>(.*?)</td>", govde, re.S | re.I)
        if not m:
            m = re.search(ad + r"\s*:?\s*</(?:strong|b)>\s*:?\s*(?:</td>\s*<td>)?\s*:?\s*([^<\n]{3,400})", govde, re.S | re.I)
        return duz(m.group(1)) if m else ""

    karar_tarihi = tarih_iso(satir("Karar Tarihi"))
    karar_no = satir("Karar No")
    konu = satir("Konu Özeti")
    mno = re.search(r"\d{4}\s*/\s*\d+", karar_no or "")
    karar_no = mno.group(0).replace(" ", "") if mno else ""
    if not karar_no:
        m = re.search(r"(\d{4})\s*/\s*(\d{1,4})\s*sayılı", baslik, re.I)
        if m:
            karar_no = f"{m.group(1)}/{m.group(2)}"
    if not karar_tarihi:
        m = re.search(r"(\d{1,2}\s*[./]\s*\d{1,2}\s*[./]\s*\d{4})\s*tarih", baslik, re.I)
        if m:
            karar_tarihi = tarih_iso(m.group(1))
    if not konu:
        m = re.search(r"[\"“”](.+?)[\"“”]", baslik)
        konu = m.group(1).strip() if m else baslik
    konu = re.sub(r"^(?:\s*Konu Özeti\s*:?\s*)+", "", konu, flags=re.I).strip(" \"“”:")
    # Künye tablosu (Karar Tarihi / Karar No / Konu Özeti) arayüzde ayrıca gösteriliyor;
    # gövdenin başındaki kopyasını çıkar.
    mt = re.match(r"\s*(?:<p>\s*</p>\s*)*<table>.*?</table>", govde, re.S)
    if mt and "Karar No" in mt.group(0) and len(govde) - mt.end() > 300:
        govde = govde[mt.end():].strip()
        metin = duz(govde)

    mk, bk = kucuk(metin), kucuk(baslik + " " + konu)
    cz = cezalar(metin)
    return {
        "id": int(re.search(r"/Icerik/(\d+)", url).group(1)),
        "url": url,
        "baslik": baslik,
        "konu": konu,
        "no": karar_no,
        "tarih": karar_tarihi,
        "yayin": yayin_iso(sayfa),
        "tur": tur(mk, bk),
        "sonuc": sonuc(mk, cz),
        "ceza": cz,
        "cezaToplam": sum(cz),
        "maddeler": maddeler(metin),
        "konular": [ad for ad, rx in KONULAR if rx.search(mk)],
        "html": govde,
    }


def liste_topla():
    """Üç listeyi tarar; (url, başlık, kaynak türü) döndürür. Aynı içerik bir kez alınır."""
    kayitlar, gorulen = [], set()
    for tur_adi, kalip in KAYNAKLAR:
        ilk = indir(kalip.format(1))
        taban = re.escape(kalip.split("/")[-1].split("?")[0])
        son = max([int(x) for x in re.findall(taban + r"\?page=(\d+)", ilk)] or [1])
        print(f"{tur_adi}: {son} sayfa", flush=True)
        for s in range(1, son + 1):
            sayfa = ilk if s == 1 else indir(kalip.format(s))
            for m in re.finditer(r'<h2>(.*?)</h2>(?:(?!<h2>).)*?<a href="([^"]+)"[^>]*class="read-more"', sayfa, re.S):
                url = html.unescape(m.group(2)).strip()
                kid = kimlik(url)
                if kid in gorulen:  # site aynı içeriği birden çok bağlantıyla ya da listede gösterebiliyor
                    continue
                gorulen.add(kid)
                kayitlar.append((url, re.sub(r"\s+", " ", html.unescape(re.sub("<[^>]+>", "", m.group(1)))).strip(), tur_adi))
            if s > 1:
                time.sleep(BEKLE)
    return kayitlar


def main():
    hepsi = "--hepsi" in sys.argv
    if "--indirme-yok" in sys.argv:
        kararlar = json.loads((DATA / "kararlar.json").read_text(encoding="utf-8"))["kararlar"]
        for k in kararlar:
            k.pop("ai", None)
        yaz(kararlar, 0, [])
        return
    ONBELLEK.mkdir(parents=True, exist_ok=True)
    liste = liste_topla()
    print(f"{len(liste)} karar bulundu", flush=True)
    kararlar, yeni, hata = [], 0, []
    # Depo klonunda ham HTML önbelleği yoktur; daha önce çözülmüş kararları yeniden indirme.
    eski_yol = DATA / "kararlar.json"
    eski = {} if hepsi or not eski_yol.exists() else {
        str(k["id"]): k for k in json.loads(eski_yol.read_text(encoding="utf-8"))["kararlar"] if k.get("html")}
    for i, (url, lb, tur_adi) in enumerate(liste, 1):
        kid = str(kimlik(url))
        pdf = url.lower().split("?")[0].endswith(".pdf")
        dosya = ONBELLEK / f"{kid}.{'pdf' if pdf else 'html'}"
        try:
            if kid in eski and not dosya.exists():
                k = eski[kid]
                k.pop("ai", None)
                k["kaynakTuru"] = tur_adi
                kararlar.append(k)
                continue
            if pdf:
                if not dosya.exists() or hepsi:
                    if not (DATA / "pdf-metin" / f"{kid}.txt").exists() or hepsi:
                        indir_dosya(url, dosya)
                        yeni += 1
                        time.sleep(BEKLE)
                metin, ocr = pdf_metni(dosya, kid)
                if not metin:
                    hata.append((url, "PDF metne çevrilemedi (taranmış belge; macOS'ta scripts/ocr.swift gerekir)"))
                    continue
                k = pdf_coz(metin, url, lb, ocr)
                k["kaynakTuru"] = tur_adi
                kararlar.append(k)
                continue
            if dosya.exists() and not hepsi:
                sayfa = dosya.read_text(encoding="utf-8")
            else:
                sayfa = indir(url)
                dosya.write_text(sayfa, encoding="utf-8")
                yeni += 1
                time.sleep(BEKLE)
            arsivden = False
            if "news__detail-article" not in sayfa:
                # Kurumun sitesinde bağlantısı bozuk olan (ana sayfaya yönlenen) kararlar:
                # elle indirilmiş web arşivi kopyası varsa onu kullan.
                yedek = DATA / "arsiv" / f"{kid}.html"
                if yedek.exists():
                    sayfa = yedek.read_text(encoding="utf-8", errors="replace")
                    arsivden = True
            k = detay_coz(sayfa, url, lb)
            if arsivden:
                k["arsiv"] = f"https://web.archive.org/web/2021/{url}"
            if not k["html"]:
                hata.append((url, "metin alınamadı (bağlantı kurum sitesinde bozuk olabilir)"))
            k["kaynakTuru"] = tur_adi
            kararlar.append(k)
        except Exception as e:
            hata.append((url, str(e)))
        if i % 25 == 0:
            print(f"  {i}/{len(liste)}", flush=True)
    yaz(kararlar, yeni, hata)


def yaz(kararlar, yeni, hata):
    analiz_yolu = DATA / "analiz.json"
    if analiz_yolu.exists():
        analiz = json.loads(analiz_yolu.read_text(encoding="utf-8"))
        for k in kararlar:
            a = analiz.get(str(k["id"]))
            if a:
                k["ai"] = a
                if not k["tarih"] and a.get("tarih"):
                    k["tarih"] = a["tarih"]
    eksik = [k["id"] for k in kararlar if "ai" not in k and k["html"]]
    kararlar.sort(key=lambda k: (k["tarih"] or "0000", k["id"]), reverse=True)
    (DATA / "analiz-bekleyen.json").write_text(json.dumps(eksik), encoding="utf-8")
    metin_dizini = DATA / "metin"
    metin_dizini.mkdir(exist_ok=True)
    for k in kararlar:
        (metin_dizini / f"{k['id']}.txt").write_text(
            f"ID: {k['id']}\nKAYNAK TÜRÜ: {k.get('kaynakTuru', 'Karar özeti')}{' (OCR ile metne çevrildi; yazım hatası olabilir)' if k.get('ocr') else ''}\nKARAR NO: {k['no']}\nKARAR TARİHİ: {k['tarih']}\nBAŞLIK: {k['baslik']}\n\n{duz(k['html'])}\n",
            encoding="utf-8")
    veri = {"guncelleme": time.strftime("%Y-%m-%d %H:%M"), "kaynak": LISTE_URL.format(1), "kararlar": kararlar}
    # kararlar.json: yapılandırılmış alanlar (ai) hariç ham veri; ai her seferinde analiz.json'dan eklenir
    ham = {"guncelleme": veri["guncelleme"], "kaynak": veri["kaynak"],
           "kararlar": [{a: b for a, b in k.items() if a != "ai"} for k in kararlar]}
    (DATA / "kararlar.json").write_text(json.dumps(ham, ensure_ascii=False), encoding="utf-8")
    (DATA / "guncelleme.txt").write_text(veri["guncelleme"] + "\n", encoding="utf-8")
    satirlar = []
    for k in kararlar:
        a = k.get("ai") or {}
        cz = a.get("cezalar") if a else [{"tutar": int(t), "gerekce": ""} for t in k["ceza"]]
        satirlar.append(json.dumps({
            "id": k["id"], "no": k["no"], "tarih": k["tarih"], "yayin": k["yayin"], "konu": k["konu"],
            "baslik": k["baslik"], "url": k["url"], "arsiv": k.get("arsiv", ""),
            "kaynakTuru": k.get("kaynakTuru", "Karar özeti"), "ocr": bool(k.get("ocr")),
            "tur": a.get("tur") or k["tur"], "sektor": a.get("sektor") or "Sınıflandırılmadı",
            "veriSorumlusu": a.get("veriSorumlusu", ""), "sonuclar": a.get("sonuclar") or k["sonuc"],
            "cezalar": cz or [], "ihlalMaddeleri": a.get("ihlalMaddeleri", []),
            "konular": a.get("konular") or k["konular"], "ozet": a.get("ozet", ""), "ilke": a.get("ilke", ""),
            "kontrol": a.get("kontrol", []), "anahtar": a.get("anahtar", []), "analizVar": bool(a),
        }, ensure_ascii=False))
    (DATA / "kararlar.jsonl").write_text("\n".join(satirlar) + "\n", encoding="utf-8")
    sablon = KOK / "arac" / "sablon.html"
    if sablon.exists():
        gomulu = json.dumps(veri, ensure_ascii=False).replace("</", "<\\/")
        (KOK / "arac" / "kvkk-kararlar.html").write_text(
            sablon.read_text(encoding="utf-8").replace("/*__VERI__*/null", gomulu), encoding="utf-8")
        print("arac/kvkk-kararlar.html yazıldı")
    import rehber
    rehber.main()
    print(f"Bitti: {len(kararlar)} karar, {yeni} yeni indirme, {len(hata)} hata, analiz bekleyen {len(eksik)}")
    for h in hata:
        print("  HATA", h)


if __name__ == "__main__":
    main()
