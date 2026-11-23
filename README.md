# kvkk-uygunluk

6698 sayılı Kişisel Verilerin Korunması Kanunu'na uygunluk denetimi ve Kişisel Verileri Koruma Kurulu karar araştırması için bir Claude skill'i ve tarayıcıda çalışan bir arama aracı.

Bir kodu, ekran görüntüsünü, formu, aydınlatma/açık rıza metnini ya da somut bir olayı Kurulun yayımladığı kararlara göre değerlendirir; her tespiti karar sayısı, tarihi ve bağlantısıyla dayandırır.

## İçinde ne var

- **351 belge:** kvkk.gov.tr'deki İlke Kararları (17), Kurul Kararları (21) ve Kurul Karar Özetleri (313). Tam metin + yapılandırılmış alanlar (tür, sektör, sonuç, ceza, ihlal edilen madde, konu, kısa özet, ilke, kontrol maddeleri).
- **27 konu rehberi** (`references/konular/`): açık rıza, aydınlatma, veri güvenliği, ihlal bildirimi, çerez, pazarlama iletileri, biyometrik veri, çalışan verileri, yurt dışına aktarım…
- **Kod ve ekran denetimi rehberleri** (`references/kod-denetimi.md`, `references/ekran-denetimi.md`).
- **Arama aracı** (`arac/kvkk-kararlar.html`): indirip çift tıklayın. Arama, süzme, yıldız/okundu/not/etiket, Excel'e aktarma, atıf kopyalama. Notlar yalnız kendi tarayıcınızda saklanır.
- **Betikler:** `scripts/ara.py` (yerel arama), `scripts/guncel.py` (Kurum sitesini canlı tarama), `scripts/guncelle.py` (yeni kararları indirme).

## Kurulum (Claude Code)

```
git clone https://github.com/marsillllll/kvkk-uygunluk ~/.claude/skills/kvkk-uygunluk
```

Sonra Claude'a sorun: "Bu kayıt formu KVKK'ya uygun mu?" (ekran görüntüsüyle), "Bu repo kişisel veriyi nasıl işliyor, KVKK açısından risk var mı?", "Mesai takibinde parmak izi kullanılabilir mi, son kararlar ne diyor?"

Gereksinim: Python 3 ve `curl`. Taranmış Resmî Gazete PDF'lerini metne çevirmek için macOS (`scripts/ocr.swift`) ya da PDF okuyabilen bir model.

## Komut satırından

```
python3 scripts/ara.py açık rıza üyelik            # yerel veri setinde ara
python3 scripts/ara.py --kaynak ilke --yil 2026    # 2026 ilke kararları
python3 scripts/ara.py --no 2026/347 --tam         # bir kararın tam metni
python3 scripts/guncel.py                          # Kurum sitesinde yeni ne var
python3 scripts/guncelle.py                        # yeni kararları indir, her şeyi yeniden üret
```

## Sınırlar

- Hukuki görüş değildir. Bağlayıcı olan Kurumun yayımladığı metindir.
- Yapılandırılmış alanlar ve kısa özetler yapay zekâ ile çıkarılmış, ikinci bir geçişle metne karşı denetlenmiştir; yine de hata içerebilir.
- Kurul her kararını yayımlamaz; çoğu özette veri sorumlusunun adı gizlidir.
- Resmî Gazete'de taranmış olarak yayımlanan kararların metni OCR ile çıkarılmıştır; harf hataları olabilir.
- Kurum sitesinde bağlantısı bozuk olan üç eski kararın metni web arşivindeki kopyadan alınmıştır.
- Mahkeme kararları kapsam dışıdır. Rehberler ve kamuoyu duyuruları yerel veri setinde yoktur, canlı taramayla okunur.

Karar metinleri Kişisel Verileri Koruma Kurumu tarafından yayımlanmış resmî metinlerdir. Bu depo Kurumla bağlantılı değildir.
