# Biyometrik veri

11 belge: 1 ilke/genel nitelikli Kurul kararı, 10 karar özeti (5 tanesinde idari para cezası, 1 tanesinde ihlal bulunmadı ya da incelenmedi).
En sık ihlal bulunan maddeler: m.4 (8), m.12 (8), m.6 (5), m.10 (3).

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

## İdari para cezası verilen kararlar

Tutarlar kararın verildiği yılın sınırlarına göredir; bugünkü risk olarak sunmayın.

- **2022/797** (04.08.2022, Sanayi ve üretim) — Mesai takibi ve iş sağlığı-güvenliği amacıyla biyometrik veri işlenmesini açıkça öngören bir kanun hükmü bulunmadığından işveren bunu ancak geçerli (belirli konuya ilişkin, bilgilendirilmiş, özgür) açık rızayla yapabilir; rıza bulunsa dahi daha az müdahaleci alternatif varken biyometrik veri işlemek ölçülülük ilkesine aykırıdır. Açık rıza dışındaki bir şarta dayanan işlemelerin açık rıza metnine dahil edilmesi aldatıcıdır ve hakkın kötüye kullanımı niteliğindedir; mahrem alanlarda izleniyor izlenimi veren (sahte dahi olsa) kamera dürüstlük kuralına aykırıdır. *Ceza:* 500.000 TL (m.12/1 - yüz tanıma ile biyometrik verinin m.6 kapsamında hiçbir işleme şartına dayanmadan işlenmesi (hukuka aykırı işlemeyi önleyecek tedbirlerin alınmaması))
- **2022/662** (07.07.2022, Diğer) — El geometrisi, ölçülebilir fizyolojik özellik üzerinden otomatik kimlik doğrulaması sağladığı için biyometrik veridir; yanında şifre kullanılması bu niteliği değiştirmez. Biyometrik veriyle giriş kontrolü ancak kanunda açıkça öngörülmüşse veya ilgili kişinin açık rızası varsa yapılabilir, sözleşmenin ifası gibi m.5 şartlarına dayandırılamaz. *Ceza:* 100.000 TL (m.12/1 - biyometrik veri niteliğindeki el geometrisinin m.6'daki işleme şartları olmaksızın işlenmesi)
- **2021/1258** (16.12.2021, Diğer) — İş sözleşmesine madde olarak konulan açık rıza, çalışanın reddetme imkânı etkin biçimde bulunmadığından özgür iradeye dayanmaz ve geçerli değildir; açık rıza bulunsa dahi aynı amaca daha az müdahaleci yöntemlerle ulaşılabiliyorsa işyeri giriş-çıkışı için biyometrik veri işlenmesi ölçülülük ilkesine aykırıdır. Açık rızaya dayanılan hallerde aydınlatma ile açık rıza alınması ayrı ayrı yerine getirilmelidir. *Ceza:* 125.000 TL (m.12/1 kişisel verilerin hukuka aykırı işlenmesini önleme yükümlülüğüne aykırılık (geçersiz açık rızaya dayanan ve ölçülülük ilkesine aykırı biyometrik veri işleme))
- **2020/404** (20.05.2020, Diğer) — İşçi-işveren ilişkisinde rıza göstermeme imkânı etkin biçimde sunulmadan alınan, kapsamı "bunlarla sınırlı olmaksızın" gibi ifadelerle belirsiz bırakılan rıza geçerli açık rıza değildir; aydınlatma ve açık rıza ayrı ayrı yerine getirilmelidir. Hash'lenerek saklanan parmak izi biyometrik veri olmaya devam eder ve alternatif yöntemlerle sağlanabilecek mekân güvenliği amacıyla işlenmesi ölçülülük ilkesine aykırıdır. *Ceza:* 50.000 TL (m.10 aydınlatma yükümlülüğünün yerine getirilmemesi (m.18/1-a)); 200.000 TL (m.12/1 veri güvenliği yükümlülüğüne aykırılık: çalışan ve yakınlarının verilerinin açık rıza olmaksızın işlenmesi, ölçüsüz biyometrik veri işleme ve açık rızasız yurt içi/yurt dışı aktarım (m.18/1-b))
- **2020/167** (27.02.2020, Spor, eğlence ve oyun) — Spor tesisine giriş-çıkış kontrolü için biyometrik veri işlenmesi, açık rıza alınsa ve alternatif giriş yöntemi sunulsa bile ölçülülük ilkesine aykırıdır; açık rıza aşırı veri toplanmasını meşrulaştırmaz. *Ceza:* 225.000 TL (m.12/1-a; giriş-çıkış kontrolünde biyometrik veri (avuç içi/el/parmak izi) işlenmesinin m.4/2-ç ölçülülük ilkesine aykırılığı)

## Talimat, uyarı ve diğer sonuçlar

- **2024/197** (08.02.2024, Eğitim; Disiplin hükümleri (kamu), Talimat, Hatırlatma / uyarı) — Yoklama/devam takibi gibi daha az müdahaleci yollarla ulaşılabilecek bir amaç için parmak izi işlenmesi, ilgili kişinin açık rızası bulunsa dahi ölçülülük ilkesine aykırıdır; açık rıza amaç için gerekli olmayan veri toplanmasını meşrulaştırmaz.
- **2020/915** (01.12.2020, Kamu kurumu; Disiplin hükümleri (kamu), Talimat) — Üstün güvenlik önlemi gerektirmeyen alanlarda salt mesai kontrolü amacıyla parmak izi işlenmesi, alternatif yöntemler mevcutken ölçülülük ilkesine aykırıdır ve açık rıza aşırı veri toplanmasını meşrulaştırmaz. İlgili kişinin Kanuna atıf yapan ve talebini açıkça belirten yazılı başvurusu, kurumun başvuru formu kullanılmadığı ya da başka birime verildiği gerekçesiyle Kanun kapsamı dışında bırakılamaz.
- **2020/649** (27.08.2020, Diğer; Diğer) — Biyometrik imza biyometrik veridir; Türk Borçlar Kanununun 15. maddesi m.6/3 anlamında kanunlarda öngörülme şartını karşılamaz, bu nedenle işleme ancak açık rıza, aydınlatma ve özel nitelikli veriler için öngörülen yeterli önlemlerle mümkündür. Biyometrik veri işlemeyi öngören kanun hükmü şüpheye yer bırakmayacak kadar açık olmalıdır.
- **2019/81** (25.03.2019, Spor, eğlence ve oyun; İdari para cezası, Talimat) — Giriş-çıkış kontrolü alternatif yollarla sağlanabilecekken biyometrik veri işlenmesi ölçülülük ilkesine aykırıdır; açık rıza, aşırı veri toplanmasını meşrulaştırmaz. Hizmetin sunulması açık rıza verilmesi şartına bağlanırsa rıza özgür iradeyle verilmiş sayılmaz.

## İhlal bulunmayan ya da incelenmeyen kararlar

Lehe emsal ararken buraya bakın; olgu farkını tam metinden doğrulayın.

- **2023/1310** (03.08.2023, Bankacılık ve finans) — Biyometrik veri işlenmesine dayanan bir işlemin biyometrik veri işlenmeden başka kanallardan da yapılabilmesi ve bunun duyurulmuş olması hâlinde hizmetin açık rıza şartına bağlandığı kabul edilmez; bununla birlikte rıza vermeyen kişiye alternatif yollar işlem akışında kolay anlaşılır ve ulaşılır biçimde bildirilmelidir.

## Bakılacaklar (kararlardan çıkan kontrol maddeleri)

- Mesai/devam takibi (PDKS) parmak izi, yüz tanıma, iris/retina, avuç içi damar izi gibi biyometrik veriyle yapılıyor mu? Yapılıyorsa uygulama sonlandırılmalı. *(2026/921)*
- Mesai takibi için biyometrik olmayan bir yöntem (şifreli kart, PIN, RFID/NFC kart, imza/kâğıt çizelge, gözetimli elle giriş) kullanılıyor mu? *(2026/921)*
- Çalışanlardan mesai takibi için biyometrik veri işlenmesine yönelik açık rıza alınarak işleme meşrulaştırılmaya çalışılıyor mu? (Açık rıza bu amaçla yeterli dayanak değildir.) *(2026/921)*
- Geçiş/mesai takip cihazı veya yazılımında biyometrik tanıma özelliği mesai takibi için devre dışı bırakıldı mı? *(2026/921)*
- Ders yoklaması ve devam takibi parmak izi gibi biyometrik veriyle yapılmamalı; biyometrik veri işlemeyen alternatif yöntemler kullanılmalı. *(2024/197)*
- Biyometrik veri işleyen bir sistem açık rızaya dayandırılmışsa, aynı amaca daha az veriyle ulaşılıp ulaşılamayacağına dair ölçülülük değerlendirmesi belgelenmiş olmalı. *(2024/197)*
- Kullanımdan kaldırılan biyometrik sistemde tutulan veriler imha edilmeli, imha belgelenmeli ve verinin aktarıldığı üçüncü kişilere bildirilmeli. *(2024/197)*
- İlgili kişi başvurularına verilen cevapların süresinde iletildiği tarihli kayıtla ispatlanabilmeli. *(2024/197)*
- Biyometrik (yüz) doğrulama içeren akışta biyometrik veri işlenmeden aynı işlemi tamamlamayı sağlayan en az bir alternatif yöntem bulunmalı. *(2023/1310)*
- Kullanıcı biyometrik veri açık rızasını reddettiğinde akış sessizce başa dönmemeli, alternatif yöntem ve kanallar aynı ekranda gösterilmeli. *(2023/1310)*
- Alternatif kanal bilgisi internet sitesinin ayrı bir bölümünde değil, işlemin yapıldığı adımda erişilebilir olmalı. *(2023/1310)*
- İşe giriş-çıkış ve mesai takibi yüz tanıma, parmak izi gibi biyometrik yöntemle değil kart, RFID veya SMS kodu gibi alternatif yöntemlerle yapılmalı. *(2022/797)*
- Tuvalet, soyunma odası, duş, mescit, dinlenme ve emzirme odası gibi alanları veya bunların girişini izleyen ya da izliyor izlenimi veren (sahte dahil) kamera bulunmamalı. *(2022/797)*
- Açık rıza metni yalnızca açık rızaya dayanan işlemeleri içermeli; sözleşme, hukuki yükümlülük gibi başka şarta dayanan işlemeler metne konulmamalı ve hangi verinin hangi amaçla işlendiği tek tek eşleştirilmiş olmalı. *(2022/797)*
- Aydınlatma metni işlenen her veri kategorisini (biyometrik veri dahil) kapsamalı ve her veri için işleme amacı ile m.5/m.6 kapsamındaki hukuki sebebi ayrı ayrı göstermeli. *(2022/797)*
- Giriş/geçiş kontrolünde el geometrisi, parmak izi, avuç içi, yüz gibi fizyolojik ölçüme dayalı sistemler biyometrik veri işleme olarak sınıflandırılmış olmalı. *(2022/662)*
- Biyometrik giriş sistemi için kanuni dayanak yoksa her kullanıcıdan, verinin kapsamı, amacı ve sonuçları hakkında önceden bilgilendirilerek alınmış açık rıza kaydı bulunmalı. *(2022/662)*
- Hukuki dayanağı olmayan biyometrik giriş uygulaması durdurulmalı, o güne kadar toplanan biyometrik veriler yok edilmeli ve veriler üçüncü kişilere aktarılmışsa yok etme işlemi onlara bildirilmeli. *(2022/662)*
- Çalışan aydınlatma metni ile açık rıza metni ayrı belgeler olmalı; ikisi tek bir karma metinde ya da iş sözleşmesinin bir maddesinde birleştirilmemeli. *(2021/1258)*
- Açık rıza beyanı iş sözleşmesinin maddesi olarak alınmamalı; çalışan rızayı reddettiğinde işe başlayabilmeli ya da çalışmaya devam edebilmeli. *(2021/1258)*
- İşyeri giriş-çıkış ve mesai takibinde parmak izi/yüz tanıma kullanılmamalı; manyetik kart, kontrol listesi gibi biyometrik veri gerektirmeyen bir yöntem bulunmalı. *(2021/1258)*
- Her çalışan için imzalı/tarihli aydınlatma kaydı ile ilgili kişi başvuru yolları ve başvuru formu belgelenebilir ve sunulabilir olmalı. *(2021/1258)*
- Personel devam kontrol sistemi (PDKS) parmak izi ya da başka biyometrik veriyle çalışmamalı; kart, sicil numarası-şifre veya imza föyü gibi bir yöntem kullanılmalı. *(2020/915)*
- Daha önce toplanmış parmak izi şablonları imha edilmiş ve imha işlemi belgelenmiş olmalı; veriler üçüncü kişilere aktarıldıysa imha onlara bildirilmiş olmalı. *(2020/915)*
- İlgili kişi başvuruları, kurumun başvuru formu kullanılmasa veya dilekçe farklı bir birime verilmiş olsa da Kanun kapsamında kaydedilip cevaplanmalı. *(2020/915)*
- Silme/imha talebine verilen cevapta talebin yerine getirilip getirilmediği açıkça belirtilmeli. *(2020/915)*
- Tablet/ped üzerinden biyometrik imza alınan süreçlerde imzadan önce ilgili kişinin açık rızası alınmalı ve kaydı tutulmalı. *(2020/649)*
- Biyometrik imza alınmadan önce m.10 kapsamında aydınlatma yapılmış olmalı. *(2020/649)*
- Biyometrik imza verileri için Kurulun özel nitelikli kişisel verilere ilişkin yeterli önlemler kararındaki tedbirler uygulanmalı. *(2020/649)*
- Çalışanlara sunulan aydınlatma metni ile açık rıza metni ayrı belgeler/ayrı onay adımları olmalı; tek bir "muvafakatname" içinde birleştirilmemeli. *(2020/404)*
- Rıza ve aydınlatma metinlerinde "bunlarla sınırlı olmaksızın", "uygun görülen diğer üçüncü kişiler", "yerini alabilecek diğer şirketler" gibi ucu açık ifadeler bulunmamalı; hangi veri kategorisinin hangi amaçla işlendiği ve kime aktarıldığı eşleştirilmiş olmalı. *(2020/404)*
- İşyeri giriş-çıkış ve mekân güvenliği için parmak izi gibi biyometrik veri yerine kart, RFID veya SMS kodu gibi alternatifler kullanılmalı; açık rıza vermeyen çalışan için özlük dosyasının eksik sayılması gibi yaptırım veya imzalamayanların listelenmesi uygulaması olmamalı. *(2020/404)*
- Sunucuları yurt dışında bulunan bulut/e-posta/saklama hizmetleri envanterde yurt dışına aktarım olarak işaretlenmiş ve m.9'daki aktarım usulü işletilmiş olmalı. *(2020/404)*
- Üye/ziyaretçi giriş-çıkış kontrolünde parmak izi, avuç içi, el geometrisi gibi biyometrik yöntemler kullanılmamalı; kart gibi daha az müdahaleci yöntem tercih edilmeli. *(2020/167)*
- Daha önce toplanmış biyometrik veriler yok edilmiş ve aktarıldığı üçüncü kişilere yok etme bildirimi yapılmış olmalı. *(2020/167)*
- Aydınlatma metni Aydınlatma Yükümlülüğü Tebliği'ne uygun ve güncel olmalı. *(2020/167)*
- Tesise giriş-çıkış kontrolü için biyometrik veri (parmak, avuç içi, el izi) zorunlu ve tek yöntem olarak sunulmamalı; kart gibi biyometrik olmayan bir seçenek bulunmalı. *(2019/81)*
- Üyelik sözleşmesinde özel nitelikli veri işlenmesine onay, sözleşmenin kurulması ya da hizmetten yararlanmanın ön şartı olarak yer almamalı. *(2019/81)*
- Banko, gişe ve ortak alanlardaki ekranlarda üyelere ait fotoğraf, ziyaret saati gibi kişisel bilgiler üçüncü kişilerin görebileceği biçimde gösterilmemeli. *(2019/81)*
- Hukuka aykırı biçimde toplanmış biyometrik veriler yok edilmeli ve verilerin aktarıldığı üçüncü kişilere yok etme işlemi bildirilmeli. *(2019/81)*
