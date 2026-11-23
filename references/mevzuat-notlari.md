# Mevzuat notları

Bu dosya yön bulmak içindir; madde metinlerinin güncel hâli için mevzuat.gov.tr'deki 6698 sayılı Kanunu, Kurul kararlarının aslı için kvkk.gov.tr'yi esas alın. Buradaki bilgiler karar özetlerinden değil genel mevzuat bilgisinden derlenmiştir; atıf yapmadan önce doğrulayın.

## 6698 sayılı Kanunun madde haritası

| Madde | Konu | Kararlarda tipik karşılığı |
|---|---|---|
| m.3 | Tanımlar (kişisel veri, işleme, veri sorumlusu, veri işleyen, açık rıza) | Veri sorumlusu / veri işleyen ayrımı, bir bilginin kişisel veri olup olmadığı |
| m.4 | Genel ilkeler: hukuka ve dürüstlük kurallarına uygunluk; doğruluk ve güncellik; belirli, açık ve meşru amaç; amaçla bağlantılı, sınırlı ve ölçülü olma; gerekli süre kadar saklama | Ölçülülük, amaç dışı kullanım, fazla veri toplama, güncel olmayan veri |
| m.5 | İşleme şartları: açık rıza (5/1) ve açık rıza aranmayan haller (5/2: kanunda öngörülme, sözleşmenin kurulması/ifası, hukuki yükümlülük, alenileştirme, hakkın tesisi/kullanılması/korunması, meşru menfaat vb.) | Yanlış hukuki sebebe dayanma, gereksiz yere açık rıza alma, rızasız işleme |
| m.6 | Özel nitelikli kişisel veriler (sağlık, biyometrik, genetik, ceza mahkûmiyeti, din, sendika vb.) | Biyometrik giriş sistemleri, sağlık verisi paylaşımı |
| m.7 | Silme, yok etme, anonim hâle getirme | Saklama süresi dolan verinin tutulması, silme talebinin reddi |
| m.8 | Yurt içinde aktarım | Üçüncü kişiyle paylaşım, grup şirketleri, iş ortakları |
| m.9 | Yurt dışına aktarım | Yurt dışı sunucu, bulut, e-posta ve CRM hizmetleri |
| m.10 | Aydınlatma yükümlülüğü (veri sorumlusunun kimliği, amaç, kime ve hangi amaçla aktarılabileceği, toplama yöntemi ve hukuki sebebi, m.11 hakları) | Eksik/katmansız aydınlatma, aydınlatma ile rızanın tek metinde birleştirilmesi |
| m.11 | İlgili kişinin hakları | Erişim, düzeltme, silme, itiraz talepleri |
| m.12 | Veri güvenliği: teknik ve idari tedbirler (12/1), veri işleyenle müşterek sorumluluk (12/2), denetim (12/3), sır saklama (12/4), ihlalin Kurula ve ilgililere bildirimi (12/5) | Siber saldırı, yanlış kişiye gönderim, yetkisiz erişim, geç bildirim |
| m.13 | Veri sorumlusuna başvuru; en geç 30 gün içinde cevap | Cevapsız bırakma, eksik cevap, ücret talebi |
| m.14 | Kurula şikâyet (önce veri sorumlusuna başvuru şartı ve süreler) | Usulden ret, süre aşımı |
| m.15 | İnceleme usulü, resen inceleme, veri işlemenin durdurulması | Bilgi-belge taleplerine cevap vermeme |
| m.16 | Veri Sorumluları Sicili (VERBİS) | Kayıt ve bildirim yükümlülüğü |
| m.18 | Kabahatler: aydınlatma (18/1-a), veri güvenliği (18/1-b), Kurul kararlarını yerine getirmeme (18/1-c), VERBİS (18/1-ç) ve 2024'te eklenen standart sözleşme bildirimi | İdari para cezasının dayanağı |
| m.28 | İstisnalar (tamamen kişisel faaliyet, istatistik/araştırma, sanat-tarih-edebiyat-bilim ve ifade özgürlüğü, millî güvenlik, yargı faaliyetleri vb.) | Basın, yargı makamları, kişisel kullanım savunmaları |

Kurul, veri ihlalinin "en kısa sürede" bildirilmesi yükümlülüğünü 24.01.2019 tarihli ve 2019/10 sayılı kararıyla 72 saat olarak yorumlamıştır. Karar veri setindedir (`ara.py --no 2019/10 --tam`); ihlal bildirimi kararlarının çoğu bu süreye atıf yapar.

## 2024 değişikliği (7499 sayılı Kanun)

12 Mart 2024'te Resmî Gazete'de yayımlanan 7499 sayılı Kanunla 6698 sayılı Kanunun 6., 9. ve 18. maddeleri değişti; değişiklikler 1 Haziran 2024'te yürürlüğe girdi.

- **m.6 (özel nitelikli veri):** "Açık rıza ya da kanunda öngörülme" ikiliği yerine sayılan işleme şartları getirildi (açık rıza, kanunlarda açıkça öngörülme, fiilî imkânsızlık hâlinde hayatın korunması, alenileştirme, hakkın tesisi/kullanılması/korunması, sır saklama yükümlülüğü altındaki kişilerce sağlık hizmetleri, istihdam ve sosyal güvenlik alanındaki hukuki yükümlülükler, belirli vakıf/dernek faaliyetleri).
- **m.9 (yurt dışına aktarım):** Açık rızaya dayalı genel aktarım rejimi kaldırıldı. Sıra: yeterlilik kararı → uygun güvenceler (standart sözleşme, bağlayıcı şirket kuralları, taahhütname, kamu kurumları arası anlaşma) → arızi aktarıma ilişkin istisnai hâller. Standart sözleşmenin imzadan itibaren beş iş günü içinde Kuruma bildirilmesi gerekir. Eski açık rıza hükmü 1 Eylül 2024'e kadar yeni düzenlemeyle birlikte uygulandı.
- **m.18:** Standart sözleşmeyi bildirmeme için ayrı idari para cezası eklendi. Kurulun idari yaptırım kararlarına karşı başvuru yolu idare mahkemeleri oldu.

**Sonuç:** Özel nitelikli veri ve yurt dışına aktarım konusunda 1 Haziran 2024'ten önceki kararlar eski metne göre verilmiştir. Bu kararları kullanırken olgu tespiti ve Kurulun yaklaşımı hâlâ yol göstericidir; ancak hukuki sebep değerlendirmesini güncel madde metnine göre yeniden yapın ve bunu yanıtta belirtin.

## İdari para cezaları

m.18'deki alt ve üst sınırlar her yıl yeniden değerleme oranında artar. Bu yüzden:

- Bir karardaki tutar, o kararın verildiği yılın sınırlarına göredir. Yıllar arası karşılaştırma yaparken bunu belirtin.
- Güncel yılın alt/üst sınırlarını bu dosyadan ya da hafızadan vermeyin; Kurumun sitesindeki güncel duyurudan doğrulatın.
- Kamu kurumları ve kamu kurumu niteliğindeki meslek kuruluşları için para cezası yerine m.18/3 uyarınca disiplin hükümleri uygulanır; kararlarda bu "disiplin hükümleri" sonucu olarak görünür.

## Bu veri setinin sınırları

- kvkk.gov.tr'deki İlke Kararları, Kurul Kararları ve Kurul Karar Özetleri bölümlerini içerir. Kamuoyu duyuruları, rehberler ve yönetmelikler `scripts/guncel.py` ile canlı okunur; mahkeme kararları dâhil değildir.
- Kurul her kararını yayımlamaz; yayımlananlar özet metindir ve çoğunda veri sorumlusunun adı gizlenmiştir.
- Sitede yayın tarihi ile karar tarihi arasında uzun süre olabilir (2024 ve 2025 tarihli pek çok karar 2026'da yayımlanmıştır). "En yeni" derken hangisini kastettiğinizi belirtin.
- En eski birkaç kayıt (2018) tarih ve sayı içermeyen kısa özetlerdir.
