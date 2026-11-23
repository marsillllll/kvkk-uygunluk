# Özel nitelikli veri

43 belge: 6 ilke/genel nitelikli Kurul kararı, 37 karar özeti (19 tanesinde idari para cezası, 9 tanesinde ihlal bulunmadı ya da incelenmedi).
En sık ihlal bulunan maddeler: m.12 (27), m.6 (14), m.4 (10), m.10 (4), m.13 (4).

> Bu dosya yapılandırılmış veriden otomatik üretilir. "İlke" ve "Bakılacaklar" satırları yapay zekâ ile çıkarılıp ikinci geçişte denetlenmiştir; bir karara dayanmadan önce `python3 scripts/ara.py --no <sayı> --tam` ile tam metni okuyun. Aynı konuda yeni tarihli karar eskisini değiştirmiş ya da daraltmış olabilir: yukarıdan aşağı (yeniden eskiye) okuyun.

## İlke kararları ve genel nitelikli Kurul kararları

Bunlar tek bir olaya değil tüm veri sorumlularına (ya da bir sektöre) yöneliktir; değerlendirmeye buradan başlayın.

### 2026/921 · 29.04.2026 · İlke kararı

**Mesai Takibi Amacıyla Biyometrik Veri İşlenmesi**

Mesai takibi amacıyla biyometrik veri işlenmesi, Kanun'un 6. maddesindeki işleme şartlarından herhangi birine dayanmaz: takibin biyometrik veriyle yapılmasını öngören açık kanun hükmü yoktur ve işçi-işveren ilişkisindeki güç dengesizliği nedeniyle açık rıza tek başına yeterli hukuki zemin oluşturmaz. Daha az müdahaleci alternatifler mevcut olduğundan, geçerli bir açık rıza bulunsa dahi bu işleme Kanun'un 4. maddesindeki ölçülülük kriterini sağlamaz. Mesai takibi biyometrik tanımlama sistemleri yerine şifreli kart veya PIN tabanlı sistemler, imza ve kâğıt bazlı devam çizelgeleri, RFID/NFC kimlik kartları ya da denetçi gözetiminde elle giriş gibi yollarla yapılmalıdır; aykırı davranan veri sorumluları hakkında Kanun'un 18. maddesi uyarınca işlem tesis edilir.

- Mesai/devam takibi (PDKS) parmak izi, yüz tanıma, iris/retina, avuç içi damar izi gibi biyometrik veriyle yapılıyor mu? Yapılıyorsa uygulama sonlandırılmalı.
- Mesai takibi için biyometrik olmayan bir yöntem (şifreli kart, PIN, RFID/NFC kart, imza/kâğıt çizelge, gözetimli elle giriş) kullanılıyor mu?
- Çalışanlardan mesai takibi için biyometrik veri işlenmesine yönelik açık rıza alınarak işleme meşrulaştırılmaya çalışılıyor mu? (Açık rıza bu amaçla yeterli dayanak değildir.)
- Geçiş/mesai takip cihazı veya yazılımında biyometrik tanıma özelliği mesai takibi için devre dışı bırakıldı mı?

Kaynak: https://www.resmigazete.gov.tr/eskiler/2026/06/20260602-3.pdf

### 2025/2120 · 06.11.2025 · İlke kararı

**Turizm ve Otelcilik Sektöründe Konaklama Hizmeti Alan Kişilerin T.C. Kimlik Belgesi Fotokopisinin Kaydedilmesi**

Konaklama hizmeti veren veri sorumluları misafirin kimlik bilgilerini (ad, soyad, T.C. kimlik numarası) kaydedebilir ve doğruluğunu teyit için kimlik belgesini görmek üzere isteyebilir; ancak teyit amacıyla olsa dahi kimlik belgesinin fotokopisini alıp kayda geçiremez, bu işleme gereğinden fazla veri işlemedir ve hukuki dayanağı yoktur. Din, kan grubu gibi veriler içeren eski nüfus cüzdanının fotokopisinin alınması ayrıca Kanun'un 6. maddesine aykırıdır. İlke kararından önce alınmış kimlik fotokopileri Kanun'un 7. maddesine uygun olarak imha edilmelidir; bu hususlar m.12/1 kapsamındaki tedbirlerdendir ve aykırılık hâlinde m.18 uyarınca işlem tesis edilir.

- Giriş (check-in) sürecinde kimlik belgesinin fotokopisi, taraması veya fotoğrafı alınmıyor; belge yalnız bilgilerin teyidi için görülüp iade ediliyor
- Otel yönetim sistemi ve misafir kayıt formunda kimlik belgesi görseli yükleme/saklama alanı bulunmuyor
- Kimlik bildirimi kapsamında misafirin ad, soyad ve T.C. kimlik numarası ile geliş-ayrılış kayıtları tutuluyor; bilgiler kimlik belgesiyle karşılaştırılarak teyit ediliyor, belgenin kopyası saklanmıyor
- Daha önce alınmış kimlik fotokopileri (fiziksel arşiv, tarama klasörleri, e-posta ekleri, yedekler dahil) m.7'ye uygun biçimde imha edilmiş
- Faturalandırma için yalnız Vergi Usul Kanunu m.230 ve m.240'ta sayılan bilgiler (ad, soyad, adres, oda numarası, oda ücreti vb.) işleniyor
- Eski tip nüfus cüzdanı ibraz eden misafirlerde de belgenin kopyası alınmıyor; din ve kan grubu gibi özel nitelikli veriler kayda geçmiyor

Kaynak: https://www.resmigazete.gov.tr/eskiler/2025/12/20251209-11.pdf

### 2025/1572 · 04.09.2025 · Kurul kararı

**Ana Faaliyet Konusu Özel Nitelikli Kişisel Veri işleme Olan Veri Sorumlularının VERBİS’e Kayıt Yükümlülüğüne İlişkin İstisna Kriteri**

Yıllık çalışan sayısı 50'den az ve yıllık mali bilanço toplamı 100 milyon Türk lirasından az olan gerçek veya tüzel kişi veri sorumlularından ana faaliyet konusu özel nitelikli kişisel veri işleme olmayanlar VERBİS'e kayıt yükümlülüğünden istisnadır. Ana faaliyet konusu özel nitelikli kişisel veri işleme olan veri sorumluları ise yıllık çalışan sayısı 10'dan az ve yıllık mali bilanço toplamı 10 milyon Türk lirasından az ise istisnadan yararlanır. Değişiklik Resmî Gazete'de yayımlandığı tarihte yürürlüğe girer.

- Ana faaliyet konusunun özel nitelikli kişisel veri işleme olup olmadığı tespit edilmiş mi?
- Ana faaliyeti özel nitelikli veri işleme olmayan veri sorumlusu için yıllık çalışan sayısı 50'den az ve yıllık mali bilanço toplamı 100 milyon TL'den az mı?
- Ana faaliyeti özel nitelikli veri işleme olan veri sorumlusu için yıllık çalışan sayısı 10'dan az ve yıllık mali bilanço toplamı 10 milyon TL'den az mı?
- İlgili gruptaki çalışan sayısı ve bilanço koşullarının ikisi birlikte sağlanmıyorsa VERBİS kaydı yapılmış mı?

Kaynak: https://www.resmigazete.gov.tr/eskiler/2025/10/20251001-4.pdf

### 2023/1154 · 06.07.2023 · Kurul kararı

**Veri Sorumluları Siciline Kayıt Yükümlülüğüne İlişkin İstisna Kriterinde Değişiklik Yapılması**

Yıllık çalışan sayısı 50'den az ve yıllık mali bilanço toplamı 100 milyon Türk lirasından az olan gerçek veya tüzel kişi veri sorumlularından ana faaliyet konusu özel nitelikli kişisel veri işleme olmayanlar, Veri Sorumluları Siciline kayıt yükümlülüğünden istisnadır. 2018/87 sayılı karardaki 25 milyon TL'lik bilanço eşiği bu kararla 100 milyon TL olarak değiştirilmiş olup değişiklik Resmî Gazete'de yayımlandığı tarihte yürürlüğe girer.

- Veri sorumlusunun yıllık çalışan sayısı 50'den az mı?
- Veri sorumlusunun yıllık mali bilanço toplamı 100 milyon Türk lirasından az mı?
- Ana faaliyet konusunun özel nitelikli kişisel veri işleme olup olmadığı tespit edilmiş mi?
- Çalışan sayısı ve bilanço koşullarının ikisi birlikte sağlanmıyorsa VERBİS kaydı yapılmış mı?
- İstisna değerlendirmesinde eski 25 milyon TL eşiği yerine güncel 100 milyon TL eşiği kullanılıyor mu?

Kaynak: https://www.kvkk.gov.tr/Icerik/7647/2023-1154

### 2018/87 · 19.07.2018 · Kurul kararı

**Yıllık çalışan sayısı 50’den az ve yıllık mali bilanço toplamı 25 milyon TL’den az olan gerçek veya tüzel kişi veri sorumlularından ana faaliyet konusu özel nitelikli kişisel veri işleme olmayanların Sicile kayıt yükümlülüğünden istisna tutulması**

Yıllık çalışan sayısı 50'den az ve yıllık mali bilanço toplamı 25 milyon TL'den az olan gerçek veya tüzel kişi veri sorumlularından ana faaliyet konusu özel nitelikli kişisel veri işleme olmayanlar, Veri Sorumluları Siciline kayıt yükümlülüğünden istisnadır. Bu istisna, 2018/32 sayılı Kurul kararıyla istisna tutulan veri sorumlularına ek olarak getirilmiştir.

- Veri sorumlusunun yıllık çalışan sayısının 50'den az olup olmadığı belgelenmiş mi?
- Veri sorumlusunun yıllık mali bilanço toplamı kararda öngörülen 25 milyon TL eşiğinin altında mı?
- Ana faaliyet konusunun özel nitelikli kişisel veri işleme olup olmadığı tespit edilmiş mi?
- İstisnadan yararlanmak için çalışan sayısı ve bilanço koşullarının ikisinin birlikte sağlandığı doğrulanmış mı?
- İstisna koşulları sağlanmıyorsa VERBİS kaydı yapılmış mı?

Kaynak: https://www.kvkk.gov.tr/Icerik/5271/2018-87

### 2018/10 · 31.01.2018 · Kurul kararı

**Özel Nitelikli Kişisel Verilerin İşlenmesinde Veri Sorumlularınca Alınması Gereken Yeterli Önlemler”in görüşülmesi.**

Özel nitelikli kişisel verilerin işlenmesinde Kanunun 6/4 maddesi gereği Kurulca belirlenen yeterli önlemlerin alınması şarttır: bu verilerin güvenliği için sistemli, kuralları net, yönetilebilir ve sürdürülebilir ayrı bir politika ve prosedür belirlenmeli; süreçte yer alan çalışanlara düzenli eğitim verilmeli, gizlilik sözleşmesi yapılmalı, erişim yetkilerinin kapsam ve süreleri tanımlanıp periyodik olarak kontrol edilmeli, görev değişikliği ya da işten ayrılmada yetkiler derhal kaldırılmalıdır. Elektronik ortamda veriler kriptografik yöntemlerle muhafaza edilmeli, anahtarlar güvenli ve farklı ortamlarda tutulmalı, tüm hareketler güvenli biçimde loglanmalı, güvenlik güncellemeleri izlenip güvenlik testleri düzenli yapılmalı ve sonuçları kayda alınmalı, uzaktan erişimde en az iki kademeli kimlik doğrulama sağlanmalıdır; fiziksel ortamda yeterli güvenlik önlemleri alınıp yetkisiz giriş çıkış engellenmelidir. Aktarımda e-posta şifreli olarak kurumsal adresle veya KEP ile, taşınabilir ortam kriptografik şifreleme ve anahtarın farklı ortamda tutulmasıyla, sunucular arası aktarım VPN veya sFTP ile, kâğıt evrak ise "gizlilik dereceli belge" formatında ve çalınma, kaybolma, yetkisiz görülme risklerine karşı önlem alınarak yapılmalıdır.

- Özel nitelikli kişisel verilerin güvenliğine yönelik, genel politikadan ayrı yazılı bir politika ve prosedür var mı?
- Bu verileri işleyen çalışanlara düzenli eğitim veriliyor, gizlilik sözleşmesi yapılıyor, erişim yetkilerinin kapsamı ve süresi tanımlanıp periyodik yetki kontrolü yapılıyor ve işten ayrılan/görevi değişenlerin yetkisi derhal kaldırılıp envanter iade alınıyor mu?
- Elektronik ortamda veriler kriptografik yöntemlerle saklanıyor, kriptografik anahtarlar güvenli ve farklı ortamlarda tutuluyor ve veriler üzerindeki tüm hareketler güvenli biçimde loglanıyor mu?
- Verilerin bulunduğu ortamların ve erişim yazılımlarının güvenlik güncellemeleri takip ediliyor, kullanıcı yetkilendirmeleri yapılıyor, güvenlik testleri düzenli yapılıp/yaptırılıp sonuçları kayıt altına alınıyor mu?
- Özel nitelikli verilere uzaktan erişimde en az iki kademeli kimlik doğrulama uygulanıyor mu; fiziksel ortamlarda yangın, su baskını, hırsızlık vb. risklere karşı önlem alınmış ve yetkisiz giriş çıkış engellenmiş mi?
- Aktarımlar belirlenen yöntemlerle mi yapılıyor: e-postada şifreli kurumsal adres veya KEP, taşınabilir bellek/CD/DVD'de şifreleme ve anahtarın ayrı ortamda tutulması, sunucular arasında VPN veya sFTP, kâğıt evrakta "gizlilik dereceli belge" formatı?

Kaynak: https://www.kvkk.gov.tr/Icerik/4110/2018-10

## İdari para cezası verilen kararlar

Tutarlar kararın verildiği yılın sınırlarına göredir; bugünkü risk olarak sunmayın.

- **2024/2196** (26.12.2024, Sanayi ve üretim) — Fidye yazılımı saldırısında iki faktörlü doğrulama, özel nitelikli veriler için şifreleme, ağ segmentasyonu ve erişilebilir log kayıtları gibi tedbirlerin ihlal öncesinde alınmamış olması m.12/1 ihlalidir. Tüzel kişiye ait veriler de bir gerçek kişiyi belirli veya belirlenebilir kılıyorsa kişisel veridir ve aksini belgelerle ortaya koymak veri sorumlusuna düşer. *Ceza:* 250.000 TL (m.12/1 veri güvenliğine yönelik teknik ve idari tedbirlerin alınmaması)
- **2024/275** (22.02.2024, Medya ve yayıncılık) — Ad-soyadın baş harfleri ile telefon numarasının yalnızca son dört hanesinin gizlenmesi, özellikle belirli bir bölgeyi hedefleyen ve mahalle gibi dolaylı tanımlayıcılar içeren kayıtlarda anonimleştirme sayılmaz; veri kişisel veri olmayı sürdürür. Siyasi düşünce verisi, kanunda öngörülmeyen hallerde ancak unsurlarını taşıyan açık rıza ile işlenebilir. *Ceza:* 40.179 TL (m.12/1 uygun güvenlik düzeyini temin edecek tedbirlerin alınmaması (m.6'ya aykırı, hukuki dayanaksız siyasi düşünce verisi işleme/yayımlama))
- **2023/1787** (19.10.2023, Sağlık) — İlgili kişi yeni bir iletişim bilgisi bildirdiği halde sistemde kayıtlı eski iletişim bilgisine (özellikle sağlık verisi içeren) bildirim gönderilmesi, m.4/2-b doğru ve güncel olma ilkesine ve m.12/1'e aykırıdır. Veri sorumlusu, verilerin doğru ve güncel tutulmasını sağlayacak kanalları açık tutmalı ve makul önlemleri almalıdır. *Ceza:* 30.000 TL (m.12/1 veri güvenliği yükümlülüğüne aykırılık (test sonucunun m.4/2-b doğru ve güncel olma ilkesine aykırı biçimde eski telefon numarasına gönderilmesi))
- **2023/767** (11.05.2023, Medya ve yayıncılık) — İfade özgürlüğü istisnası (m.28/1-c) ancak özel hayatın gizliliği ve kişilik hakları ihlal edilmediği sürece uygulanır; haberde kamu yararı bulunsa bile, haberin gerektirdiğinden fazla ayrıntıyla ve özel nitelikli veriler açıklanarak verilmesi özle biçim dengesini bozar ve istisnayı ortadan kaldırır. *Ceza:* 100.000 TL (m.12/1 özel nitelikli kişisel verilerin geçerli işleme şartı olmaksızın haberde yayımlanması (veri güvenliği tedbirlerinin alınmaması))
- **2023/787** (11.05.2023, Sağlık) — Sektöre özgü mevzuatın yasakladığı bir amaç için yapılan veri işleme, ilgili kişinin açık rızası alınmış olsa dahi hukuka uygun hale gelmez; açık rıza, meşru olmayan amacı ve ölçüsüz veri toplamayı meşrulaştırmaz. *Ceza:* 250.000 TL (m.12/1-a kişisel verilerin hukuka aykırı işlenmesini önlemeye yönelik tedbirlerin alınmaması (sağlık verilerinin reklam amacıyla işlenmesi))
- **2022/1357** (23.12.2022, Spor, eğlence ve oyun) — Kan grubu sağlık verisidir ve spor salonu üyeliği kapsamında ancak açık rıza ile işlenebilir; pazarlama iletisi onayı, kişisel verilerin işlenmesine verilmiş açık rıza sayılmaz. Aydınlatma ve açık rıza metinleri sözleşme metninden ayrı düzenlenmeli, açık rıza her faaliyet için onay verme ve vermeme seçeneklerini içermelidir. *Ceza:* 100.000 TL (m.12/1 yükümlülüklerinin yerine getirilmemesi (özel nitelikli kan grubu verisinin açık rıza alınmadan işlenmesi))
- **2022/662** (07.07.2022, Diğer) — El geometrisi, ölçülebilir fizyolojik özellik üzerinden otomatik kimlik doğrulaması sağladığı için biyometrik veridir; yanında şifre kullanılması bu niteliği değiştirmez. Biyometrik veriyle giriş kontrolü ancak kanunda açıkça öngörülmüşse veya ilgili kişinin açık rızası varsa yapılabilir, sözleşmenin ifası gibi m.5 şartlarına dayandırılamaz. *Ceza:* 100.000 TL (m.12/1 - biyometrik veri niteliğindeki el geometrisinin m.6'daki işleme şartları olmaksızın işlenmesi)
- **2021/1258** (16.12.2021, Diğer) — İş sözleşmesine madde olarak konulan açık rıza, çalışanın reddetme imkânı etkin biçimde bulunmadığından özgür iradeye dayanmaz ve geçerli değildir; açık rıza bulunsa dahi aynı amaca daha az müdahaleci yöntemlerle ulaşılabiliyorsa işyeri giriş-çıkışı için biyometrik veri işlenmesi ölçülülük ilkesine aykırıdır. Açık rızaya dayanılan hallerde aydınlatma ile açık rıza alınması ayrı ayrı yerine getirilmelidir. *Ceza:* 125.000 TL (m.12/1 kişisel verilerin hukuka aykırı işlenmesini önleme yükümlülüğüne aykırılık (geçersiz açık rızaya dayanan ve ölçülülük ilkesine aykırı biyometrik veri işleme))
- **2021/1111** (02.11.2021, Hukuk, avukatlık ve icra) — Avukatlık Kanunu m.2, avukata üçüncü kişinin adli sicil bilgisine resen erişme yetkisi vermez; bu veri ancak Adlî Sicil Kanunu m.7'de sayılanlara verilebilir. Özel nitelikli veri baştan hukuka aykırı elde edilmişse, bu veriyle yapılan sonraki işlemeler (mahkemeye sunma dahil) de hukuka aykırıdır. *Ceza:* 75.000 TL (m.12/1(a) hukuka aykırı işlemeyi önleyecek tedbirlerin alınmaması (adli sicil verisinin m.6'daki hukuki sebep olmadan işlenmesi))
- **2021/407** (20.04.2021, Sağlık) — Sağlık ve genetik veri içeren fiziksel hasta dosyalarının bulunduğu arşivlerde yetkisiz giriş çıkış engellenmeli, kamera kayıtları ve erişim düzenli izlenmeli ve bu süreçlerde görev alan çalışanlara düzenli eğitim verilmelidir. İhlal 72 saat içinde Kurula, makul sürede de ilgili kişilere bildirilmelidir. *Ceza:* 450.000 TL (m.12/1 veri güvenliğini sağlamaya yönelik gerekli tedbirlerin alınmaması); 150.000 TL (m.12/5 ihlal bildirim yükümlülüğünün (72 saat, ilgili kişilere bildirim) yerine getirilmemesi)
- **2020/511** (30.06.2020, Sigorta) — Sistem geçişlerinde güvenlik gereksinimlerini gözetmeyen, belge yüklemelerinde onay ve kontrol mekanizması kurmayan ve sağlık verisini daha sıkı tedbirlerle (kriptografik koruma) saklamayan veri sorumlusu, fiilî zarar sınırlı olsa da m.12/1'i ihlal eder. *Ceza:* 100.000 TL (m.12/1 veri güvenliğine ilişkin teknik ve idari tedbirlerin alınmaması)
- **2020/463** (16.06.2020, Sağlık) — Özel nitelikli veri işleyen veri sorumlusu, sızma testleri, risk analizi ve log takibi ile saldırıları kendisi tespit edebilmeli; veri yedeklerini ağ dışında ve yalnız sistem yöneticisinin erişebileceği şekilde tutmalıdır. *Ceza:* 125.000 TL (m.12/1 veri güvenliğine yönelik teknik ve idari tedbirlerin alınmaması)
- **2020/407** (20.05.2020, Sağlık) — Sağlık verisinin açık rıza veya m.6'daki şartlar olmaksızın, sehven de olsa üçüncü kişiye gönderilmesi hukuka aykırı aktarımdır ve m.12/1'e aykırılık oluşturur. Tüzel kişilerde veri sorumlusu, mesul müdür gibi bir gerçek kişi değil tüzel kişinin kendisidir. *Ceza:* 100.000 TL (m.12/1 sağlık verisinin hukuki dayanak olmaksızın üçüncü kişiye aktarılması (veri güvenliği yükümlülüğü))
- **2020/355** (07.05.2020, Sağlık) — Sağlık verilerine erişim sağlayan bir sistemi kullanan veri sorumlusu, bu sisteme yetkisiz üçüncü kişilerin (yakınları dâhil) erişimini önleyecek tedbirleri almak zorundadır; aksi m.12/1'in ihlalidir ve verileri ele geçirip kullanan kişi bakımından TCK m.136 kapsamında savcılığa bildirim yapılabilir. *Ceza:* 60.000 TL (m.12/1 Medula sistemine üçüncü kişilerin erişimini önleyecek güvenlik tedbirlerinin alınmaması)
- **2020/255** (02.04.2020, Eğitim) — Okul rehberlik servisinin uyguladığı psikolojik ölçme aracı öğrencinin ruh sağlığına ilişkin veri üretiyorsa, işleme velinin açık rızasına dayanmalıdır; velinin testten bilgisi ve onayı olması açık rıza ve aydınlatma yerine geçmez. Aydınlatma yükümlülüğünün yerine getirildiğini ispat yükü veri sorumlusundadır. *Ceza:* 50.000 TL (m.12 - öğrencinin sağlık verisinin velinin açık rızası olmadan işlenmesini önleyecek idari ve teknik tedbirlerin alınmaması)
- **2020/167** (27.02.2020, Spor, eğlence ve oyun) — Spor tesisine giriş-çıkış kontrolü için biyometrik veri işlenmesi, açık rıza alınsa ve alternatif giriş yöntemi sunulsa bile ölçülülük ilkesine aykırıdır; açık rıza aşırı veri toplanmasını meşrulaştırmaz. *Ceza:* 225.000 TL (m.12/1-a; giriş-çıkış kontrolünde biyometrik veri (avuç içi/el/parmak izi) işlenmesinin m.4/2-ç ölçülülük ilkesine aykırılığı)
- **2019/372** (09.12.2019, Medya ve yayıncılık) — Kamu yararı bulunmayan bir yayında sağlık verisinin açıklanması ifade özgürlüğü istisnasından (m.28/1-c) yararlanamaz; m.6'daki şartlardan birine dayanmayan böyle bir paylaşım m.12/1(a)'ya aykırıdır. *Ceza:* 125.000 TL (m.12/1(a) özel nitelikli sağlık verisinin m.6 şartlarına dayanmaksızın köşe yazısında paylaşılması)
- **2019/294** (01.10.2019, Ulaşım, lojistik ve kargo) — Kimlik doğrulaması için ek bilgi istenebilir; ancak din ve kan grubu gibi özel nitelikli veri içeren arkalı önlü kimlik görüntüsü istenmesi ölçülülük ilkesine ve m.6'ya aykırıdır, daha az veriyle doğrulama yapılmalıdır. İlgili kişiye verilerinin saklanması ve paylaşılması hakkında yanlış bilgi verilmesi dürüstlük kuralına ve başvuru hakkına aykırıdır. *Ceza:* 100.000 TL (m.12/1 veri güvenliği yükümlülüğüne aykırılık (kimlik görüntüsünün hukuka aykırı işlenmesi))
- **2019/269** (18.09.2019, Sosyal medya) — Yazılım özelliklerinin etkileşiminden doğan güvenlik hataları yayına alınmadan önce test aşamasında tespit edilip giderilmelidir; zafiyetin uzun süre fark edilmemesi ve tespit sonrası müdahalenin gecikmesi m.12/1 ihlalidir. İhlalin Kurula usulüne uygun bildirilmemesi ayrıca cezalandırılır. *Ceza:* 1.150.000 TL (m.12/1 teknik ve idari tedbirlerin alınmaması); 450.000 TL (m.12/5 veri ihlalinin Kurula bildirilmemesi)

## Talimat, uyarı ve diğer sonuçlar

- **2024/197** (08.02.2024, Eğitim; Disiplin hükümleri (kamu), Talimat, Hatırlatma / uyarı) — Yoklama/devam takibi gibi daha az müdahaleci yollarla ulaşılabilecek bir amaç için parmak izi işlenmesi, ilgili kişinin açık rızası bulunsa dahi ölçülülük ilkesine aykırıdır; açık rıza amaç için gerekli olmayan veri toplanmasını meşrulaştırmaz.
- **2022/172** (24.02.2022, Diğer; Talimat) — Yabancı şirketin tüzel kişiliği olmayan Türkiye irtibat bürosunun çalışanları bakımından veri sorumlusu yurt dışındaki şirketin kendisidir; irtibat bürosu yetkilisine (işveren vekiline) yapılan ilgili kişi başvurusu geçerlidir ve süresinde yanıtlanmalıdır. Silme ve yok etme işlemleri kayıt altına alınmalı, talep hâlinde belgelenebilmelidir.
- **2021/962** (21.09.2021, Sağlık; İdari para cezası, Talimat) — Bir çalışanın, başka bir çalışana (hekime) ait yetkiyle sağlık kayıtlarına hizmet ilişkisi olmaksızın erişebilmesi, eğitim verilmiş olsa dahi veri sorumlusunun m.12/1-b kapsamında hukuka aykırı erişimi önleyecek makul teknik ve idari tedbirleri almadığını gösterir. Veri sorumlusu kendisine ulaşan m.13 başvurularını yanıtlamakla yükümlüdür.
- **2021/761** (06.08.2021, Sağlık; Talimat, Disiplin hükümleri (kamu)) — Sağlık kuruluşunda tüm hekim ve kayıt personelinin tüm hasta dosyalarına erişebilmesi ölçülülük ilkesine aykırıdır; erişim, hastanın muayene ve tedavisiyle ilgili personelle sınırlanmalı ve görüntüleme dahil tüm erişimler loglanmalıdır. Sağlık verisi, vekâletnamesinde özel nitelikli verilerin aktarımına ilişkin özel hüküm bulunmayan avukata verilemez.
- **2020/915** (01.12.2020, Kamu kurumu; Disiplin hükümleri (kamu), Talimat) — Üstün güvenlik önlemi gerektirmeyen alanlarda salt mesai kontrolü amacıyla parmak izi işlenmesi, alternatif yöntemler mevcutken ölçülülük ilkesine aykırıdır ve açık rıza aşırı veri toplanmasını meşrulaştırmaz. İlgili kişinin Kanuna atıf yapan ve talebini açıkça belirten yazılı başvurusu, kurumun başvuru formu kullanılmadığı ya da başka birime verildiği gerekçesiyle Kanun kapsamı dışında bırakılamaz.
- **2020/649** (27.08.2020, Diğer; Diğer) — Biyometrik imza biyometrik veridir; Türk Borçlar Kanununun 15. maddesi m.6/3 anlamında kanunlarda öngörülme şartını karşılamaz, bu nedenle işleme ancak açık rıza, aydınlatma ve özel nitelikli veriler için öngörülen yeterli önlemlerle mümkündür. Biyometrik veri işlemeyi öngören kanun hükmü şüpheye yer bırakmayacak kadar açık olmalıdır.
- **2019/81** (25.03.2019, Spor, eğlence ve oyun; İdari para cezası, Talimat) — Giriş-çıkış kontrolü alternatif yollarla sağlanabilecekken biyometrik veri işlenmesi ölçülülük ilkesine aykırıdır; açık rıza, aşırı veri toplanmasını meşrulaştırmaz. Hizmetin sunulması açık rıza verilmesi şartına bağlanırsa rıza özgür iradeyle verilmiş sayılmaz.
- **2018/143** (05.12.2018, Sağlık; İdari para cezası) — Sağlık verisinin, m.8'deki aktarım şartları (açık rıza ya da m.6/3'teki haller) bulunmaksızın üçüncü kişiyle paylaşılması m.12/4'e aykırıdır ve idari para cezasını gerektirir.
- **** (tarih yok, Sağlık; İdari para cezası) — Sağlık verisinin, erişim yetkisi olan personel tarafından ekran görüntüsünün çekilmesi yoluyla sosyal medyada ifşa edilmesi hâlinde veri sorumlusu m.12/1-c kapsamında uygun güvenlik düzeyini sağlamamış sayılır.

## İhlal bulunmayan ya da incelenmeyen kararlar

Lehe emsal ararken buraya bakın; olgu farkını tam metinden doğrulayın.

- **2023/1310** (03.08.2023, Bankacılık ve finans) — Biyometrik veri işlenmesine dayanan bir işlemin biyometrik veri işlenmeden başka kanallardan da yapılabilmesi ve bunun duyurulmuş olması hâlinde hizmetin açık rıza şartına bağlandığı kabul edilmez; bununla birlikte rıza vermeyen kişiye alternatif yollar işlem akışında kolay anlaşılır ve ulaşılır biçimde bildirilmelidir.
- **2021/925** (16.09.2021, Hukuk, avukatlık ve icra) — Sendikal nedenle fesih iddiasına dayanan bir davada, ispat yükü kapsamında dosyayla ilgili olan başka bir işçinin sendika üyeliği/istifa bilgisinin avukat tarafından dava dilekçesinde kullanılması, Avukatlık Kanunu m.2 ve HMK m.119 uyarınca Kanunun 6. maddesine aykırılık oluşturmaz.
- **2020/935** (08.12.2020, Sigorta) — Tek kişiyi etkileyen ve süresinde bildirilen yanlış kişiye gönderim ihlalinde Kurul yaptırım uygulamayabilir; ancak veri sorumlusu ilgili kişiye bildirimi ve verinin yanlış alıcı nezdinde silindiğini belgelemekle yükümlü tutulur.
- **2020/769** (08.10.2020, Diğer) — Eski çalışanların özlük dosyalarının İş Kanunu ve Sosyal Sigortalar Kanunu uyarınca saklanması m.5/2 (a) ve (ç) şartlarına dayanır ve açık rıza gerektirmez. Çalışan sağlık verileri, Kurulun belirlediği yeterli önlemler alınarak, sır saklama yükümlülüğü altındaki iş yeri hekimi tarafından mevzuattaki görevleri kapsamında açık rıza aranmadan işlenebilir.
- **2020/667** (03.09.2020, Sigorta) — Sağlık sigortası poliçesindeki sağlık verileri m.6/3 istisnası kapsamında işlenemeyeceğinden, sigorta şirketinin poliçe için ilgili kişiden açık rıza istemesi Kanuna aykırı değildir.
- **2020/396** (20.05.2020, Kamu kurumu) — Sağlık ve cinsel hayat dışındaki özel nitelikli verilerin açık rıza olmadan işlenmesinde m.6/3'teki "kanunlarda öngörülme" şartı maddi kanun (düzenleyici işlemler dahil) olarak anlaşılır. Memur hakkındaki yargı kararları, özlük dosyası mevzuatı gereği açık rıza bulunmasa da dosyada tutulabilir ve silme talebi bu nedenle reddedilebilir.
- **2020/138** (18.02.2020, Diğer) — Görülmekte olan bir davada mahkemenin talebi üzerine özlük dosyasının (içindeki sağlık raporları dahil) mahkemeye sunulmasına ilişkin şikâyetler, Kanunun 28/1-d istisnası ve yargı mercilerinin görevine giren konuların incelenememesi kuralı nedeniyle Kurulca incelenmez.
- **2020/93** (06.02.2020, Kamu kurumu) — Sağlık verileri m.6/3'te sayılan amaçlara hizmet etmeye devam ettiği sürece işleme şartları ortadan kalkmış sayılmaz; bu durumda silme talebi yönünden Kanun kapsamında işlem yapılmaz. Sehven oluşturulduğu ileri sürülen sağlık verilerinin düzeltilmesi, Kişisel Sağlık Verileri Hakkında Yönetmeliğin 13. maddesindeki il sağlık müdürlüğü başvuru usulüne tabidir.
- **2019/82** (25.03.2019, E-ticaret ve perakende) — Katılımı zorunlu olmayan ve katılmayanların temel hizmetten yararlanabildiği bir sadakat programında üyelik için açık rıza istenmesi, hizmetin açık rıza şartına bağlanması sayılmaz. Aydınlatma metni ile rıza beyanı birbiriyle tutarlı olmalı, pazarlama programı için amaçla ölçüsüz özel nitelikli veri işlenmemeli; kişiye özel pazarlamada kullanılan veri anonim sayılamaz.

## Bakılacaklar (kararlardan çıkan kontrol maddeleri)

- Mesai/devam takibi (PDKS) parmak izi, yüz tanıma, iris/retina, avuç içi damar izi gibi biyometrik veriyle yapılıyor mu? Yapılıyorsa uygulama sonlandırılmalı. *(2026/921)*
- Mesai takibi için biyometrik olmayan bir yöntem (şifreli kart, PIN, RFID/NFC kart, imza/kâğıt çizelge, gözetimli elle giriş) kullanılıyor mu? *(2026/921)*
- Çalışanlardan mesai takibi için biyometrik veri işlenmesine yönelik açık rıza alınarak işleme meşrulaştırılmaya çalışılıyor mu? (Açık rıza bu amaçla yeterli dayanak değildir.) *(2026/921)*
- Geçiş/mesai takip cihazı veya yazılımında biyometrik tanıma özelliği mesai takibi için devre dışı bırakıldı mı? *(2026/921)*
- Giriş (check-in) sürecinde kimlik belgesinin fotokopisi, taraması veya fotoğrafı alınmıyor; belge yalnız bilgilerin teyidi için görülüp iade ediliyor *(2025/2120)*
- Otel yönetim sistemi ve misafir kayıt formunda kimlik belgesi görseli yükleme/saklama alanı bulunmuyor *(2025/2120)*
- Kimlik bildirimi kapsamında misafirin ad, soyad ve T.C. kimlik numarası ile geliş-ayrılış kayıtları tutuluyor; bilgiler kimlik belgesiyle karşılaştırılarak teyit ediliyor, belgenin kopyası saklanmıyor *(2025/2120)*
- Daha önce alınmış kimlik fotokopileri (fiziksel arşiv, tarama klasörleri, e-posta ekleri, yedekler dahil) m.7'ye uygun biçimde imha edilmiş *(2025/2120)*
- Faturalandırma için yalnız Vergi Usul Kanunu m.230 ve m.240'ta sayılan bilgiler (ad, soyad, adres, oda numarası, oda ücreti vb.) işleniyor *(2025/2120)*
- Eski tip nüfus cüzdanı ibraz eden misafirlerde de belgenin kopyası alınmıyor; din ve kan grubu gibi özel nitelikli veriler kayda geçmiyor *(2025/2120)*
- Ana faaliyet konusunun özel nitelikli kişisel veri işleme olup olmadığı tespit edilmiş mi? *(2025/1572)*
- Ana faaliyeti özel nitelikli veri işleme olmayan veri sorumlusu için yıllık çalışan sayısı 50'den az ve yıllık mali bilanço toplamı 100 milyon TL'den az mı? *(2025/1572)*
- Ana faaliyeti özel nitelikli veri işleme olan veri sorumlusu için yıllık çalışan sayısı 10'dan az ve yıllık mali bilanço toplamı 10 milyon TL'den az mı? *(2025/1572)*
- İlgili gruptaki çalışan sayısı ve bilanço koşullarının ikisi birlikte sağlanmıyorsa VERBİS kaydı yapılmış mı? *(2025/1572)*
- İşletme dışından iş kaynaklarına yapılan kullanıcı girişlerinde iki faktörlü kimlik doğrulama zorunlu olmalı. *(2024/2196)*
- Grup şirketlerinin sistemleri arasında ağ segmentasyonu yapılmış olmalı; bir şirketteki saldırı diğerlerinin verilerine yayılamamalı. *(2024/2196)*
- Özel nitelikli kişisel veriler güvenli şifreleme/kriptografik anahtarlarla saklanmalı. *(2024/2196)*
- Log kayıtları saldırıdan etkilenmeyecek ayrı bir ortamda tutulmalı ve Kişisel Veri İşleme Envanteri talep hâlinde sunulabilir durumda olmalı. *(2024/2196)*
- Yayımlanan anket/sonuç tablolarında telefon numarası, ad-soyad baş harfi, mahalle gibi dolaylı tanımlayıcılar bir arada yer almamalı; kısmi maskeleme anonimleştirme olarak kabul edilmemeli. *(2024/275)*
- Siyasi görüş/oy tercihi toplayan anket formlarında belirli konuya ilişkin, bilgilendirmeye dayanan ve özgür iradeyle verilen açık rıza ayrıca alınmalı ve kaydı saklanmalı. *(2024/275)*
- Anket sonuçları kamuya açıklanmadan önce kayıtların başka verilerle eşleştirilerek kişiye ulaşılıp ulaşılamayacağı test edilmeli, yalnızca toplulaştırılmış sonuç yayımlanmalı. *(2024/275)*
- Anket katılımcılarına veri toplanırken Kanun ve Tebliğ'e uygun aydınlatma metni sunulmalı. *(2024/275)*
- Ders yoklaması ve devam takibi parmak izi gibi biyometrik veriyle yapılmamalı; biyometrik veri işlemeyen alternatif yöntemler kullanılmalı. *(2024/197)*
- Biyometrik veri işleyen bir sistem açık rızaya dayandırılmışsa, aynı amaca daha az veriyle ulaşılıp ulaşılamayacağına dair ölçülülük değerlendirmesi belgelenmiş olmalı. *(2024/197)*
- Kullanımdan kaldırılan biyometrik sistemde tutulan veriler imha edilmeli, imha belgelenmeli ve verinin aktarıldığı üçüncü kişilere bildirilmeli. *(2024/197)*
- İlgili kişi başvurularına verilen cevapların süresinde iletildiği tarihli kayıtla ispatlanabilmeli. *(2024/197)*
- Hizmet anında formla alınan güncel telefon numarası, sistemdeki eski hasta kaydındaki numaranın yerine geçmeli; sonuç bildirimi yeni bildirilen numaraya gönderilmeli. *(2023/1787)*
- Sağlık sonucu SMS/e-posta ile gönderilmeden önce, mevcut kayıttaki iletişim bilgisi ile başvuru sırasında beyan edilen bilginin uyuşup uyuşmadığı kontrol edilmeli. *(2023/1787)*
- Güncelliğini yitiren iletişim bilgileri kayıtlardan çıkarılmalı/imha edilmeli ve ilgili kişinin bilgilerini güncelleyebileceği kanal bulunmalı. *(2023/1787)*
- Biyometrik (yüz) doğrulama içeren akışta biyometrik veri işlenmeden aynı işlemi tamamlamayı sağlayan en az bir alternatif yöntem bulunmalı. *(2023/1310)*
- Kullanıcı biyometrik veri açık rızasını reddettiğinde akış sessizce başa dönmemeli, alternatif yöntem ve kanallar aynı ekranda gösterilmeli. *(2023/1310)*
- Alternatif kanal bilgisi internet sitesinin ayrı bir bölümünde değil, işlemin yapıldığı adımda erişilebilir olmalı. *(2023/1310)*
- Veri sorumlusunun yıllık çalışan sayısı 50'den az mı? *(2023/1154)*
- Veri sorumlusunun yıllık mali bilanço toplamı 100 milyon Türk lirasından az mı? *(2023/1154)*
- Ana faaliyet konusunun özel nitelikli kişisel veri işleme olup olmadığı tespit edilmiş mi? *(2023/1154)*
- Çalışan sayısı ve bilanço koşullarının ikisi birlikte sağlanmıyorsa VERBİS kaydı yapılmış mı? *(2023/1154)*
- İstisna değerlendirmesinde eski 25 milyon TL eşiği yerine güncel 100 milyon TL eşiği kullanılıyor mu? *(2023/1154)*
- Haber içeriğinde yer alan sağlık ve cinsel hayata ilişkin ayrıntılar, haberin özünü aktarmak için gerekli olanla sınırlı tutulmalı. *(2023/767)*
- Kimliği belirli kişilere ilişkin özel nitelikli veri içeren haberler yayımlanmadan önce kamu yararı, gerçeklik-güncellik ve özle biçim dengesi ölçütleri bakımından editoryal kontrolden geçirilmeli. *(2023/767)*
- Haberde ad-soyad gibi kimlik bilgileri ile sağlık verisinin birlikte yayımlanmasının haber amacı bakımından zorunlu olup olmadığı değerlendirilmeli. *(2023/767)*
- Sağlık kuruluşunun internet sitesi ve sosyal medya hesaplarında hasta görüntüsü, hastalık ve tedavi sonucu anlatımı içeren reklam/tanıtım niteliğinde içerik bulunmamalı. *(2023/787)*
- Hasta onam/açık rıza formlarında 'pazarlama, reklam ve tanıtım' amacıyla sağlık verisi ve görüntü işlenmesine ilişkin rıza maddesi yer almamalı. *(2023/787)*
- Açık rızaya dayandırılan her işleme amacı, sektörel mevzuattaki yasaklara aykırı olup olmadığı yönünden ayrıca kontrol edilmeli. *(2023/787)*
- Bilgilendirme amaçlı içeriklerde amaca kişisel veri işlenmeden ulaşılabiliyorsa hasta verisi kullanılmamalı. *(2023/787)*
- Üyelik formunda/sözleşmesinde kan grubu gibi sağlık verisi alanı varsa bu veri için ayrı ve belgelenebilir açık rıza alınmalı; rıza yoksa alan toplanmamalı. *(2022/1357)*
- Aydınlatma metni ve açık rıza metni üyelik sözleşmesinin içine gömülmemeli, ayrı metinler olarak sunulmalı. *(2022/1357)*
- Pazarlama iletisi onayında "istiyorum" seçeneğinin yanında "istemiyorum" seçeneği de sunulmalı ve bu onay başka veri işlemeleri için rıza olarak kullanılmamalı. *(2022/1357)*
- E-posta ile gelen ilgili kişi başvuruları yasal süre içinde cevaplanmalı ve cevap kayıt altına alınmalı. *(2022/1357)*
- Giriş/geçiş kontrolünde el geometrisi, parmak izi, avuç içi, yüz gibi fizyolojik ölçüme dayalı sistemler biyometrik veri işleme olarak sınıflandırılmış olmalı. *(2022/662)*
- Biyometrik giriş sistemi için kanuni dayanak yoksa her kullanıcıdan, verinin kapsamı, amacı ve sonuçları hakkında önceden bilgilendirilerek alınmış açık rıza kaydı bulunmalı. *(2022/662)*
- Hukuki dayanağı olmayan biyometrik giriş uygulaması durdurulmalı, o güne kadar toplanan biyometrik veriler yok edilmeli ve veriler üçüncü kişilere aktarılmışsa yok etme işlemi onlara bildirilmeli. *(2022/662)*
- İrtibat bürosu/şube üzerinden gelen ilgili kişi başvuruları merkeze iletilip 30 gün içinde yanıtlanacak şekilde bir süreç tanımlanmış olmalı. *(2022/172)*
- Silme, yok etme ve anonim hale getirme işlemleri kayıt altına alınmalı ve kayıtlar en az üç yıl saklanmalı. *(2022/172)*
- İşe alımda istenen her belgenin hangi mevzuat hükmüne veya işleme şartına dayandığı yazılı olarak gösterilebilmeli. *(2022/172)*
- Çalışan verilerinin yurt dışındaki merkezde işlenmesi açık rızaya dayanıyorsa, bu rıza iş sözleşmesi kurulurken alınmış ve belgelenmiş olmalı. *(2022/172)*
- Çalışan aydınlatma metni ile açık rıza metni ayrı belgeler olmalı; ikisi tek bir karma metinde ya da iş sözleşmesinin bir maddesinde birleştirilmemeli. *(2021/1258)*
- Açık rıza beyanı iş sözleşmesinin maddesi olarak alınmamalı; çalışan rızayı reddettiğinde işe başlayabilmeli ya da çalışmaya devam edebilmeli. *(2021/1258)*
- İşyeri giriş-çıkış ve mesai takibinde parmak izi/yüz tanıma kullanılmamalı; manyetik kart, kontrol listesi gibi biyometrik veri gerektirmeyen bir yöntem bulunmalı. *(2021/1258)*
- Her çalışan için imzalı/tarihli aydınlatma kaydı ile ilgili kişi başvuru yolları ve başvuru formu belgelenebilir ve sunulabilir olmalı. *(2021/1258)*
- Ceza mahkûmiyeti/adli sicil verisi işlenen her süreçte açık rıza ya da bu veriyi işlemeye açıkça izin veren özel kanun hükmü belgelenmiş olmalı. *(2021/1111)*
- Üçüncü kişilere (tanık, karşı taraf vb.) ait adli sicil bilgisi, genel yardım/bilgi alma yetkisine dayanılarak değil, yalnız Adlî Sicil Kanunu m.7'deki usulle temin edilmeli. *(2021/1111)*
- Hukuka aykırı elde edildiği anlaşılan veriler ve bunlara dayalı kayıtlar imha edilmeli ve imha kayıt altına alınmalı. *(2021/1111)*
- Hekime ait e-Nabız/hasta bilgi sistemi oturumu, hekim dışındaki personel (sekreter vb.) tarafından kullanılamayacak şekilde korunmalı (kişiye özel kimlik bilgisi, oturum kilidi/zaman aşımı). *(2021/962)*
- İlgili kişilerin yazılı başvuruları kayda alınmalı ve yasal süre içinde yanıtlanmalı. *(2021/962)*
- Dava dilekçesinde üçüncü kişilere ait özel nitelikli veriye yalnızca ispat yükü kapsamındaki vakıayla doğrudan ilgili olduğu ölçüde yer verilmeli. *(2021/925)*
- Özel nitelikli verinin açık rıza olmadan işlendiği her durumda dayanılan kanun hükmü (ör. Avukatlık Kanunu m.2, HMK m.119) belgelenebilir olmalı. *(2021/925)*
- Hasta kayıt/otomasyon sisteminde yalnız ekleme-silme-değiştirme değil, kayıt görüntüleme işlemleri de kullanıcı bazında loglanmalı. *(2021/761)*
- Hasta dosyalarına erişim, tüm personele açık olmak yerine muayene ve tedaviyle ilgili personele göre tanımlanmış yazılı bir yetki matrisine bağlanmalı. *(2021/761)*
- Sistemden hasta kaydı çıktısı alma yetkisi belirli personelle sınırlandırılmalı ve yazılı bir prosedüre bağlanmalı. *(2021/761)*
- Sağlık verisi talep eden avukatın vekâletnamesinde özel nitelikli verilerin işlenmesi ve aktarılmasına ilişkin açık rızayı gösteren özel hüküm bulunduğu kontrol edilmeden veri verilmemeli. *(2021/761)*
