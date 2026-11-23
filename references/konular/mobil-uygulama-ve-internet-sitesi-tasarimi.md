# Mobil uygulama ve internet sitesi tasarımı

45 belge: 4 ilke/genel nitelikli Kurul kararı, 41 karar özeti (25 tanesinde idari para cezası, 7 tanesinde ihlal bulunmadı ya da incelenmedi).
En sık ihlal bulunan maddeler: m.12 (28), m.5 (13), m.10 (10), m.4 (9), m.15 (4).

> Bu dosya yapılandırılmış veriden otomatik üretilir. "İlke" ve "Bakılacaklar" satırları yapay zekâ ile çıkarılıp ikinci geçişte denetlenmiştir; bir karara dayanmadan önce `python3 scripts/ara.py --no <sayı> --tam` ile tam metni okuyun. Aynı konuda yeni tarihli karar eskisini değiştirmiş ya da daraltmış olabilir: yukarıdan aşağı (yeniden eskiye) okuyun.

## İlke kararları ve genel nitelikli Kurul kararları

Bunlar tek bir olaya değil tüm veri sorumlularına (ya da bir sektöre) yöneliktir; değerlendirmeye buradan başlayın.

### 2026/347 · 18.02.2026 · İlke kararı

**Veri Sorumluları Tarafından Açık Rıza ve Aydınlatma Metinlerinin Ayrı Ayrı Düzenlenmesi Gerektiği**

Aydınlatma yükümlülüğü, işlemenin açık rıza dâhil hangi işleme şartına dayandığından bağımsız olarak her durumda ve kişisel veri işlemeye başlamadan önce yerine getirilir; ilgili kişinin talebine veya onayına bağlı değildir. İşleme açık rızaya dayanıyorsa aydınlatma metni ile açık rıza metni farklı başlıklar altında ayrı metinler olarak düzenlenir; aynı sayfada yer alsalar dahi alt alta, ayrı başlıklarla ve her biri için ayrı beyan alınacak şekilde sunulur. İşleme açık rıza dışındaki bir şarta dayanıyorsa yalnızca aydınlatma yapılır, ayrıca açık rıza metni sunulmaz; aydınlatma metni için yalnızca "okudum ve anladım" türünde okundu/bilgi edinildi beyanı alınabilir, onay veya rıza istenemez.

- Aydınlatma metni ile açık rıza metni ayrı başlıklar altında ayrı metinler mi; aynı sayfadaysa alt alta ve her biri için ayrı beyan/işaret kutusu var mı?
- Aydınlatma metninin altında "okudum ve kabul ediyorum", "okudum ve onaylıyorum", "okudum ve açık rıza veriyorum" gibi ifadeler yerine yalnızca "okudum ve anladım" türünde bir beyan mı kullanılıyor?
- Açık rıza dışındaki bir işleme şartına dayanan faaliyetler için ilgili kişiden ayrıca açık rıza metni/onayı isteniyor mu (istenmemeli)?
- Aydınlatma, işleme şartı ne olursa olsun veri işlemeye başlamadan önce yapılıyor ve yapıldığı ispatlanabiliyor mu; açık rızanın alındığı da ispatlanabiliyor mu?
- Metinler başka bir veri sorumlusundan birebir kopyalanmamış, kuruluşun kendi organizasyon ve faaliyetlerine göre mi hazırlanmış; yanıltıcı/yanlış bilgi (ör. yapılmayan yurt dışı aktarımı izlenimi) ve "Kanun'un 5 ve 6. maddelerindeki şartlar kapsamında işlenmektedir" gibi muğlak ifadeler içermiyor mu?
- Aydınlatma metni sade ve kısa mı (ör. 11. maddenin tamamı yerine "Kanun'un 11. maddesi kapsamındaki haklarınız" atfı); işlenen veriler ve kategorileri ile her faaliyetin amacı ve hukuki sebebi açık ve net belirtilmiş mi?

Kaynak: https://www.resmigazete.gov.tr/eskiler/2026/03/20260324-3.pdf

### 2026/266 · 11.02.2026 · İlke kararı

**Sadakat Kart Üyeliği Bulunan Bir Kişinin Cep Telefonu Numarasının veya Sadakat Kart Numarasının Üçüncü Bir Kişi Tarafından Alışveriş Esnasında Kullanılması**

Sadakat kart sahibinin cep telefonu numarasının veya kart numarasının, bilgisi ve rızası olmadan üçüncü bir kişi tarafından kasada bildirilmesiyle onun adına alışveriş yapılmasına imkân veren uygulama m.5'teki hiçbir işleme şartına dayanmaz ve hukuka aykırıdır; bu yolla ilgili kişi adına fatura düzenlenmesi veya işlem bilgisinin hesabına işlenmesi m.4'teki doğru ve güncel olma ilkesine aykırıdır. Veri sorumluları, sadakat kartın hangi amaçla olursa olsun (üyelik oluşturma, puan kazanma, puan kullanma, indirim/promosyon) kullanımında işlemin ilgili kişinin bilgisi ve rızası dahilinde yapıldığını doğrulayan mekanizmalar (SMS tek kullanımlık kod, uygulama/site barkod ya da QR kodu, fiziki kartın ibrazı, kart şifresi, yalnız telefon numarasıyla hangi işlemlere izin verildiğine dair opt-in tercih vb.) kurmak zorundadır; işlem türüne ve riskine göre farklı ve alternatif yöntemler kullanılabilir. Üyelik sözleşmesiyle kartın başkasına kullandırılmaması sorumluluğunun üyeye yüklenmesi m.12 yükümlülüğünü ortadan kaldırmaz; uyum süresi kararın yayımından itibaren 6 aydır.

- Kasada yalnız cep telefonu numarası veya sadakat kart numarası söylenerek, doğrulama ya da üyenin önceden verdiği opt-in onay olmadan sadakat kart üzerinden işlem (puan kazanma, indirim/promosyon dahil) yapılamıyor
- Sadakat kartın her kullanım türü için bir doğrulama adımı var: SMS tek kullanımlık kod, uygulama/site barkod ya da QR kodu, fiziki kartın okutulması veya kart şifresi
- Yalnız telefon numarasıyla işleme izin veriliyorsa, üye çevrim içi hesabından hangi işlemlere (alışveriş/puan kazanma, indirim/promosyon, puan harcama) onay verdiğini opt-in olarak seçmiş; varsayılan kapalı
- Doğrulanmamış bir alışveriş için üye adına fatura düzenlenmiyor ve alışveriş bilgisi üyenin hesabına/işlem geçmişine işlenmiyor
- Üyelik sözleşmesindeki 'kart üçüncü kişilere kullandırılamaz' hükmü tek tedbir olarak kullanılmıyor; teknik doğrulama ayrıca mevcut
- Doğrulama mekanizmaları ilke kararının yayımından itibaren 6 ay içinde devreye alınmış

Kaynak: https://www.resmigazete.gov.tr/eskiler/2026/02/20260228-5.pdf

### 2022/388 · 21.04.2022 · İlke kararı

**Belediyelerin ödeme ve borç sorgulama hizmetleri hakkında İlke Kararı**

Belediyeler, emlak vergisi ödeme/hızlı ödeme ve borç sorgulama hizmetlerinde Kanunun 12. maddesi kapsamında "üyelik ve şifre" ya da "çift faktörlü doğrulama" kullanmak zorundadır. Çift faktörlü doğrulamada ilk doğrulama TC kimlik no, ad soyad, vergi no, sicil no gibi verilerle yapılabilir; ikinci doğrulama ise SMS ya da e-postaya iletilen kişiye özel şifre gibi yalnız ilgili kişinin erişebileceği bir veriyle yapılmalı, telefon no, doğum tarihi, anne baba adı, sicil no gibi başkalarının da erişebileceği bilgiler ikinci faktör olarak kullanılmamalıdır. Bu önlemleri almayan belediyeler hakkında şikâyet/ihbar üzerine Kanunun 18. maddesi çerçevesinde işlem tesis edilir.

- Çevrim içi ödeme, hızlı ödeme ve borç sorgulama ekranları yalnızca TC kimlik numarası (veya tek bir tanımlayıcı) girilerek kişiye ait bilgileri göstermiyor mu?
- Bu ekranlara erişim üyelik ve şifre ya da çift faktörlü doğrulama ile mi sağlanıyor?
- İkinci doğrulama adımı, kişiye özel oluşturulmuş şifre ya da ilgili kişinin daha önce bildirdiği telefona/e-postaya iletilen SMS kodu/şifre gibi yalnız ilgili kişinin erişebileceği bir veriye mi dayanıyor?
- Doğum tarihi, anne baba adı, telefon numarası, sicil no gibi başkalarının da bilebileceği bilgiler ikinci faktör olarak kullanılmıyor mu? (TC kimlik no + doğum günü tek kademeli doğrulama sayılır.)
- Uzaktan erişilen kişisel veriler için risk değerlendirmesi yapılmış ve doğrulama yöntemi buna göre seçilmiş mi?

Kaynak: https://www.kvkk.gov.tr/Icerik/7252/2022-388

### 2017/61 · 21.12.2017 · İlke kararı

**Rehberlik Hizmeti Veren İnternet Sitelerinde/Uygulamalarda Kişisel Verilerin Korunması**

Kanunda ve ilgili mevzuatta dayanağı bulunmaksızın ilgili kişilerin iletişim bilgilerinin paylaşımını yapan (isimden telefon numarası, telefon numarasından isim sorgulatan) internet siteleri ve mobil uygulamaların veri işleme faaliyeti Kanunun 15/7 maddesi uyarınca derhal durdurulmalıdır. Faaliyetine son vermeyen site ve uygulamalar için erişimin engellenmesi amacıyla yetkili kurumlara başvurulur, TCK 136 çerçevesinde Cumhuriyet Başsavcılığına ihbarda bulunulur ve karara uymayanlar hakkında Kanunun 18. maddesi kapsamında işlem yapılır.

- Ürün, isimden telefon numarası veya telefon numarasından isim sorgulama ya da kişinin başkalarının rehberinde nasıl kayıtlı olduğunu gösterme işlevi sunuyor mu?
- Sorgulanan/paylaşılan iletişim bilgilerinin sahibi olan her ilgili kişi bakımından Kanunun 5. (ve varsa 6.) maddesindeki bir işleme şartı, özellikle açık rıza, mevcut ve belgelenebilir mi?
- Uygulama, kullanıcının telefon rehberini ya da sosyal medya hesaplarını toplayıp rehberdeki üçüncü kişilerin verilerini başka kullanıcılara erişilebilir kılıyor mu?
- İşleme şartı bulunmayan iletişim bilgisi paylaşım/sorgulama işlevi durdurulmuş mu?

Kaynak: https://www.kvkk.gov.tr/Icerik/4113/2017-61

## İdari para cezası verilen kararlar

Tutarlar kararın verildiği yılın sınırlarına göredir; bugünkü risk olarak sunmayın.

- **2024/1393** (15.08.2024, Telekomünikasyon) — Açık rıza dışındaki bir işleme şartına dayanan veri işleme faaliyeti için ilgili kişiden ayrıca açık rıza istenmesi, kişiyi yanıltıp yanlış yönlendirdiğinden hukuka ve dürüstlük kurallarına uygunluk ilkesine aykırıdır. Veri sorumlusuna yapılan başvuruda yer almayan iddialar Kurula şikâyette incelenmez. *Ceza:* 90.000 TL (m.12/1 - başka işleme şartına dayanan işleme için açık rıza istenerek ilgili kişinin yanıltılması (m.4/2-a hukuka ve dürüstlük kurallarına uygunluk ilkesine aykırılık))
- **2023/1796** (19.10.2023, E-ticaret ve perakende) — Veri sorumlusu, veri güvenliğine ilişkin teknik ve idari tedbirleri alma yükümlülüğünü sözleşmeyle tamamen veri işleyene devredemez; veri işleyenden alınan hizmetten kaynaklanan teknik hata da veri sorumlusunun m.12 kapsamındaki sorumluluğunu kaldırmaz. *Ceza:* 200.000 TL (m.12/1-b kişisel verilere hukuka aykırı erişilmesini önleme yükümlülüğüne aykırılık)
- **2023/1309** (03.08.2023, Ulaşım, lojistik ve kargo) — PNR ve soyadı ile girişte farklı soyadlı yolcuların verilerinin aynı PNR üzerinden görülebilmesi, m.12/1 kapsamında hukuka aykırı erişimi önleyecek tedbirlerin alınmadığını gösterir. Yalnız soyadı eşleşmesine dayalı erişim de aynı soyadlı ama birlikte seyahat etmeyen kişiler bakımından veri ihlaline yol açabileceğinden ilave teknik tedbir gerektirir. *Ceza:* 300.000 TL (m.12/1 hukuka aykırı erişimi önleyecek teknik ve idari tedbirlerin alınmaması (m.12/5 uyarınca Kurula bildirim yapılmaması da dikkate alınarak))
- **2023/924** (01.06.2023, Diğer) — Alacağın takibi ve davada ispat için plaka üzerinden kimlik tespiti ve araç fotoğrafı sunulması m.5/2-e kapsamında açık rıza gerektirmez; ancak işleme şartı ne olursa olsun aydınlatma yükümlülüğü devam eder ve plakanın aleni olması bu yükümlülüğü kaldırmaz. Çevrim içi borç sorgulama gibi hizmetlerde yalnız plaka gibi başkalarınca bilinebilen tek bir veriyle sorgulama yeterli güvenlik sağlamaz; ikinci kademede kişiye özel bir doğrulama gerekir. *Ceza:* 75.000 TL (m.10 aydınlatma yükümlülüğünün yerine getirilmemesi (m.18/1-a))
- **2023/692** (02.05.2023, Sağlık) — Sunulan hizmetle doğrudan bağlantılı olmayan tanıtım amaçlı veri işlemeye ilişkin açık rızanın hizmetin (randevunun) ön şartı yapılması rızanın özgür irade unsurunu sakatlar ve m.4'teki hukuka ve dürüstlük kurallarına uygunluk ilkesine aykırıdır. Açık rıza dışındaki bir işleme şartına dayanılabilecekken açık rıza alınması aldatıcı ve hakkın kötüye kullanımı niteliğindedir; aydınlatma metni "onay" ifadesiyle sunulmamalıdır. *Ceza:* 300.000 TL (m.12/1 yükümlülüklerinin yerine getirilmemesi (randevunun tanıtım amaçlı açık rıza şartına bağlanması; m.4 hukuka ve dürüstlük kurallarına uygunluk ilkesine aykırılık))
- **2022/1358** (23.12.2022, Spor, eğlence ve oyun) — Kesinlikle gerekli çerezler dışındaki işlevsel, performans-analitik ve reklam/pazarlama çerezleri için başka bir işleme şartı yoksa siteye giriş anında, varsayılan olarak kapalı (opt-in) bir mekanizmayla açık rıza alınmalıdır. Çerezlerle işlenen veriler için ilk ziyarette m.10'a uygun aydınlatma yapılması zorunludur. *Ceza:* 300.000 TL (m.12/1 işleme şartı olmaksızın zorunlu olmayan (reklam/pazarlama) çerezlerle kişisel veri işlenmesi)
- **2022/243** (17.03.2022, E-ticaret ve perakende) — Veri sorumlusunun, kullanıcının beyan ettiği iletişim bilgisinin doğruluğu konusunda aktif özen yükümlülüğü vardır; teyit mekanizması kurmadan beyan edilen e-posta adresine fatura gibi kişisel veri içeren ileti gönderilmesi, adresin gerçek sahibi yönünden işleme şartından yoksundur ve m.12/1'e aykırıdır. *Ceza:* 100.000 TL (m.12/1 veri güvenliği yükümlülüklerinin yerine getirilmemesi (teyit mekanizması olmadan, m.5'te işleme şartı bulunmaksızın e-posta adresinin işlenmesi))
- **2022/229** (10.03.2022, E-ticaret ve perakende) — Sitenin düzgün çalışması için kesinlikle gerekli çerezler dışındaki işlevsel, performans-analitik ve reklam/pazarlama çerezleri, başka bir işleme şartı yoksa meşru menfaate dayandırılamaz; kullanıcının giriş anında aktif hareketiyle verdiği, varsayılan olarak çerezlerin kapalı geldiği opt-in açık rızayı gerektirir. Çerezler yoluyla yurt dışına aktarım da m.9'daki usullere (o tarihte taahhütname/yeterlilik yoksa açık rıza) uygun olmalıdır. *Ceza:* 800.000 TL (m.12/1 veri güvenliği tedbirlerinin alınmaması (zorunlu olmayan çerezlerle işleme şartı olmadan veri işleme ve m.9'a aykırı yurt dışı aktarım))
- **2022/137** (17.02.2022, E-ticaret ve perakende) — Bir hizmetten yararlanmanın ön şartı olarak zorunlu tutulan ve sözleşmenin gerektirdiğini aşan veriler (e-Devlet şifresi, üyelik için T.C. kimlik numarası) bakımından verilen rıza özgür iradeye dayanmadığından geçerli değildir ve işleme m.5'e aykırıdır. Veri sorumlusu kendi internet sitesinde gerçekleşen veri toplama alanlarının kontrolünü sağlamakla yükümlüdür; bunu sağlayamaması m.12/1 kapsamında tedbir eksikliğidir. *Ceza:* 300.000 TL (m.12/1 veri güvenliği tedbirlerinin alınmaması (e-Devlet şifresi ve T.C. kimlik no'nun m.5 şartı olmadan işlenmesi ve üyelik sayfasındaki güvenlik açığı))
- **2021/1110** (02.11.2021, Otomotiv) — Alacağın tahsili için icra takibi kapsamında veri işlenmesi hukuka uygun olsa da borçlu müşterilerin verilerinin herkesin erişimine açık internet ortamında yayımlanması hiçbir işleme şartına dayanmaz. Kurulun inceleme başlatması için ihlalden etkilenen kişinin şikâyeti gerekmez; ihbar veya resen öğrenme yeterlidir. *Ceza:* 200.000 TL (m.12/1 uygun güvenlik düzeyini sağlayacak tedbirlerin alınmaması (m.5'e dayanmayan şekilde verilerin internette yayımlanması))
- **2021/389** (20.04.2021, Sigorta) — Veri işleme faaliyeti açık rıza dışındaki bir işleme şartına dayandırılabiliyorken ilgili kişiden açık rıza alınması aldatıcı ve hakkın kötüye kullanımı niteliğindedir; hukuka ve dürüstlük kurallarına uygunluk ilkesine aykırıdır. Aydınlatma yükümlülüğü ile açık rıza alınması ayrı ayrı yerine getirilmeli, tek onaya bağlanmamalıdır. *Ceza:* 250.000 TL (m.12/1 - başka işleme şartı mevcutken açık rıza alınmasının m.4 hukuka ve dürüstlük kurallarına uygunluk ilkesine aykırı olması)
- **2021/359** (13.04.2021, Gayrimenkul ve site yönetimi) — Asıl hizmetin ifasından ayrı bir amaca hizmet eden ve katılımı isteğe bağlı olan bir uygulamaya kullanıcı verilerinin aktarılması m.5/2'deki şartlara dayandırılamaz, ancak ilgili kişinin açık rızasıyla yapılabilir. Verinin işlenme amaç ve yöntemini belirleyen ve hizmet sağlayıcıya yetki veren taraf veri sorumlusudur; onun adına işlem yapan uygulama sağlayıcısı veri işleyendir. *Ceza:* 100.000 TL (m.12/1 - site sakininin telefon numarasının açık rıza olmadan isteğe bağlı ikinci uygulamaya aktarılması suretiyle hukuka aykırı işlenmesi)
- **2021/311** (25.03.2021, E-ticaret ve perakende) — Canlı sistemde yapılacak değişiklikler beklenen yüke uygun biçimde test edilmeli ve riskin en düşük olduğu zamanda uygulanmalıdır; önbellekleme/kopyalama hatasıyla kullanıcılara başkasının profilinin gösterilmesi m.12/1 ihlalidir. *Ceza:* 200.000 TL (m.12/1 veri güvenliğine ilişkin teknik ve idari tedbirlerin alınmaması)
- **2020/766** (08.10.2020, Bankacılık ve finans) — Aydınlatma metninde m.5 ve m.6'daki işleme şartlarının genel olarak sıralanması yeterli değildir; işlenen verilerin hangi şarta dayanılarak işlendiği ayrıntılı gösterilmeli ve aydınlatma, veri elde edilirken ilgili faaliyete özgü olarak yapılmalıdır. Kurul talimatının eksik yerine getirilmesi m.18/1-c kapsamında ayrıca cezalandırılır. *Ceza:* 120.000 TL (m.15/5 Kurul kararıyla verilen talimatın yerine getirilmemesi (m.18/1-c))
- **2020/765** (08.10.2020, Bankacılık ve finans) — Aydınlatma metninde m.5 ve m.6'daki işleme şartlarının yalnızca sıralanması yeterli değildir; hangi verinin hangi hukuki sebebe dayanılarak işlendiği ayrıntılı gösterilmeli ve aydınlatma, verinin elde edilmesi sırasında ilgili faaliyete özgü yapılmalıdır. Kurul talimatının yerine getirilmemesi m.15/5 uyarınca ayrıca yaptırıma bağlanır. *Ceza:* 120.000 TL (m.15/5 Kurul kararıyla verilen talimatın yerine getirilmemesi (aydınlatma metninin Tebliğe uygun hale getirilmemesi))
- **2020/567** (22.07.2020, E-ticaret ve perakende) — Kullanıcı hesaplarına erişimde kimlik doğrulamanın güçlendirilmesi (iki faktörlü doğrulama, güçlü şifre zorunluluğu) ihlalden önce alınması gereken teknik tedbirlerdendir; bunların ancak ihlalden sonra planlanması m.12/1'e aykırılık oluşturur. *Ceza:* 75.000 TL (m.12/1 veri güvenliğine yönelik gerekli teknik tedbirlerin alınmaması)
- **2020/213** (12.03.2020, Telekomünikasyon) — Yazılım değişikliklerinin test edilmeden ve canlıya alma prosedürleri uygulanmadan doğrudan gerçek ortamda yapılması ile test süreçlerinin yetersizliği, m.12/1 kapsamında teknik ve idari tedbir eksikliğidir. *Ceza:* 300.000 TL (m.12/1 veri güvenliğine yönelik teknik ve idari tedbirlerin alınmaması)
- **2020/113** (11.02.2020, E-ticaret ve perakende) — Sızma testlerinin yapılmaması, bilinen web zafiyetlerinin giderilmemesi, mobil uygulama trafiğinin korunmaması, halka açık ağlardan kısıtsız sistem erişimine izin verilmesi ve politika, müdahale planı ile eğitimlerin ihlalden önce bulunmaması m.12/1 kapsamında tedbir eksikliğidir. *Ceza:* 200.000 TL (m.12/1 veri güvenliğine yönelik teknik ve idari tedbirlerin alınmaması)
- **2020/65** (27.01.2020, Ulaşım, lojistik ve kargo) — Kullanıcıların hizmet sağlayıcılar tarafından puanlanması sözleşmenin ifasıyla doğrudan ilgili bir işleme değildir; m.5'te ayrı bir işleme şartına dayanmalı ve aydınlatma metninde açıkça belirtilmelidir. Kullanıcıya bildirilmeyen puanlama, hukuka ve dürüstlük kurallarına uygunluk ile belirli, açık ve meşru amaç ilkelerine aykırıdır. *Ceza:* 100.000 TL (m.12/1 işleme şartı bulunmadan yolcuların puanlanması (hukuka aykırı işlemenin önlenmemesi)); 10.000 TL (m.10 aydınlatma yükümlülüğünün yerine getirilmemesi)
- **2020/50** (20.01.2020, E-ticaret ve perakende) — Kişisel verilerin URL üzerinden üçüncü taraf sağlayıcılara sızması tasarım aşamasındaki testlerin yetersizliğini, ihlalin çok geç fark edilmesi ise log ve alarm sistemlerinin eksikliğini gösterir ve m.12/1'e aykırılık oluşturur. *Ceza:* 50.000 TL (m.12/1 veri güvenliğine yönelik gerekli teknik ve idari tedbirlerin alınmaması)
- **2019/269** (18.09.2019, Sosyal medya) — Yazılım özelliklerinin etkileşiminden doğan güvenlik hataları yayına alınmadan önce test aşamasında tespit edilip giderilmelidir; zafiyetin uzun süre fark edilmemesi ve tespit sonrası müdahalenin gecikmesi m.12/1 ihlalidir. İhlalin Kurula usulüne uygun bildirilmemesi ayrıca cezalandırılır. *Ceza:* 1.150.000 TL (m.12/1 teknik ve idari tedbirlerin alınmaması); 450.000 TL (m.12/5 veri ihlalinin Kurula bildirilmemesi)
- **2019/170** (18.06.2019, E-ticaret ve perakende) — Kişisel verilerin URL üzerinden üçüncü taraf sağlayıcılara sızması tasarım aşamasındaki testlerin yetersizliğini, ihlalin çok geç fark edilmesi ise log ve alarm sistemlerinin eksikliğini gösterir ve m.12/1'e aykırılık oluşturur. *Ceza:* 50.000 TL (m.12/1 veri güvenliğine yönelik gerekli teknik ve idari tedbirlerin alınmaması)
- **2019/104** (11.04.2019, Sosyal medya) — Üçüncü taraf uygulamaların kullanıcının verdiği izin kapsamını aşan verilere erişebilmesi veri ihlalidir ve veri sorumlusunun m.12/1 kapsamındaki tedbir yükümlülüğüne aykırıdır. Açık rıza, bir ürün veya hizmetten yararlanmanın ön şartı olarak ileri sürülemez. *Ceza:* 1.100.000 TL (m.12/1 veri ihlalinin oluşmaması için gerekli teknik ve idari tedbirlerin alınmaması (Fotoğraf API hatası)); 550.000 TL (m.12/5 veri ihlalinin Kurula bildirilmemesi ve ilgili kişilere en kısa sürede bildirilmemesi)
- **2019/23** (14.02.2019, Diğer) — Ardışık ve tahmin edilebilir takip numarasıyla, ek doğrulama olmaksızın kişisel veri gösteren sorgu ekranı m.12/1'e aykırıdır; yalnızca maskeleme yapmak asıl açığı gidermez. Kurul talimatının yerine getirilmemesi ayrıca idari para cezası gerektirir. *Ceza:* 150.000 TL (m.12/1 kişisel verilerin muhafazası için gerekli teknik ve idari tedbirlerin alınmaması (2019/23 sayılı karar)); 50.000 TL (m.15 uyarınca verilen Kurul kararının (talimatın) yerine getirilmemesi (05/03/2019 tarihli 2019/52 sayılı karar))
- **2023/134** (tarih yok, Sosyal medya) — Gizlilik politikası açık rıza metni yerine kullanılamaz; açık rıza aydınlatmadan ayrı alınmalı, hangi verinin hangi amaç ve işleme şartıyla işlendiği açıkça belirtilmelidir. Çocuk kullanıcıların hesaplarının varsayılan olarak herkese açık olması ve profilleme çerezlerinin açık rıza olmadan kullanılması hukuka aykırıdır. *Ceza:* 1.750.000 TL (m.12/1 kişisel verilerin hukuka aykırı işlenmesini önlemeye yönelik teknik ve idari tedbirlerin alınmaması)

## Talimat, uyarı ve diğer sonuçlar

- **2021/847** (26.08.2021, E-ticaret ve perakende; Talimat) — Aynı kişisel veri farklı işleme faaliyetlerinde farklı hukuki sebep ve saklama süresine tabi olabilir: fatura/satış sözleşmesi kaydındaki adres yasal süre boyunca saklanabilir, ancak bu, aynı adresin kullanıcı hesabı profilinde silinemez ve düzenlenemez biçimde tutulmasını haklı kılmaz. Veri sorumlusu, verilerin doğru ve güncel olmasını sağlayacak imkânları ilgili kişiye sunmalıdır.
- **2021/361** (13.04.2021, Bankacılık ve finans; İdari para cezası, Talimat) — Mobil uygulamada tanıtım amaçlı push bildirim tercihinin varsayılan olarak açık gelmesi geçerli açık rıza sayılmaz; varsayılan ayar tanıtım iletisi almama biçiminde olmalı ve onay, açık rızanın tüm unsurlarını taşıyacak şekilde alınmalıdır.
- **2021/140** (25.02.2021, Kamu kurumu; Talimat, Diğer) — Yalnızca TC kimlik numarası ya da vergi numarası gibi tek bir bilgiyle kişinin borç bilgisine erişim sağlayan çevrim içi sorgulama ekranları, isim görünmese bile, kişisel verilere hukuka aykırı erişimi önleme yükümlülüğüne (m.12/1-b) aykırıdır.
- **2021/85** (03.02.2021, E-ticaret ve perakende; Talimat) — Genel nitelikli gizlilik veya veri işleme politikaları aydınlatma metni olarak kullanılamaz; aydınlatma, verinin elde edildiği işlem (üyelik, sipariş) sırasında ve o işlem özelinde, işlenen veri bazında yapılmalıdır. Aydınlatmanın yapıldığını ispat yükü veri sorumlusundadır ve sayfa altındaki bir bağlantı bu ispat için yeterli değildir.
- **2019/389** (26.12.2019, Eğitim; Diğer) — Sınav ve değerlendirme sonuçları herkese açık şekilde tüm unsurlarıyla ilan edilmemeli; yalnız ilgili adayların kimlik doğrulamasıyla sorgulayabileceği bir yöntemle ya da ad-soyad ve kimlik numarası maskelenerek, gerekli süreyle sınırlı olarak yayımlanmalıdır. Bu işleme faaliyeti için ilgili kişiler aydınlatılmalıdır.
- **2019/296** (01.10.2019, Telekomünikasyon; Talimat, Hatırlatma / uyarı) — Veri sorumlusu, kimlik teyidi gerekçesiyle ilgili kişi başvurularını yalnızca noter veya e-imza gibi Kanun ve Tebliğde öngörülmeyen külfetli yollarla sınırlayamaz; başvuru kanallarını bu şekilde daraltmak dürüstlük kuralına aykırıdır.
- **2019/188** (01.07.2019, Eğitim; Disiplin hükümleri (kamu), Talimat) — Sınav sonuçlarının herkese ve arama motorlarına açık biçimde, süresiz olarak yayımlanması bir işleme şartına dayanmaz; sonuçlar kimlik doğrulamalı ve kişinin yalnızca kendi sonucunu görebildiği bir sistemle duyurulmalıdır. Kurulun bilgi belge talebini süresinde cevaplamayan kamu kurumunun sorumluları hakkında disiplin hükümleri uygulanır.
- **2018/90** (26.07.2018, İnsan kaynakları ve istihdam; Talimat) — Açık rızaya dayalı işlemede aydınlatma yükümlülüğü ile açık rızanın alınması ayrı ayrı yerine getirilmelidir; aydınlatma onaya bağlı değildir ve aydınlatma metnini okuyan kişi içeriğine rıza vermek zorunda değildir.
- **2018/91** (26.07.2018, E-ticaret ve perakende; İdari para cezası, Talimat) — Sistemsel bir hata sonucu bir müşterinin bilgilerinin diğer müşterilerce görülebilir hale gelmesi, hata sonradan giderilmiş olsa dahi m.12/1 kapsamında tedbir eksikliğidir. Silme talebinde bulunan ilgili kişiye yapılan işlemler belgeleriyle birlikte bildirilmelidir.

## İhlal bulunmayan ya da incelenmeyen kararlar

Lehe emsal ararken buraya bakın; olgu farkını tam metinden doğrulayın.

- **2023/1675** (28.09.2023, Sanayi ve üretim) — İnsan hatasından kaynaklanan bir ihlalde, veri sorumlusu eğitim, gizlilik taahhüdü, disiplin süreci ve uygun teknik tedbirleri önceden almış, ihlali hızla tespit edip düzeltici adım atmışsa m.12/1 kapsamında yaptırım uygulanmayabilir. Bilgi sistemleri ihtiyaçları belirlenirken insan hatasını önleyecek teknik tedbirler de değerlendirilmelidir.
- **2023/1310** (03.08.2023, Bankacılık ve finans) — Biyometrik veri işlenmesine dayanan bir işlemin biyometrik veri işlenmeden başka kanallardan da yapılabilmesi ve bunun duyurulmuş olması hâlinde hizmetin açık rıza şartına bağlandığı kabul edilmez; bununla birlikte rıza vermeyen kişiye alternatif yollar işlem akışında kolay anlaşılır ve ulaşılır biçimde bildirilmelidir.
- **2023/890** (25.05.2023, Ulaşım, lojistik ve kargo) — Temel hizmetten bağımsız olarak yalnızca ek menfaat sağlayan bir sadakat programına katılımın açık rızaya bağlanması, açık rızanın hizmet şartı olarak dayatılması sayılmaz.
- **2022/707** (21.07.2022, E-ticaret ve perakende) — Az sayıda kişiyi ve sınırlı veriyi etkileyen, kısa sürede tespit edilip giderilen ve ilgili kişilere bildirilen bir teknik hata kaynaklı ihlalde, veri sorumlusunun sistemlerini denetlediği ve hızla müdahale ettiği gösterilebiliyorsa m.12/1 kapsamında yaptırım uygulanmayabilir.
- **2021/850** (26.08.2021, Telekomünikasyon) — Mevzuatın öngördüğü kimlik belgesi örneğinin, gerekli teknik ve idari tedbirleri alınmış kurumsal bir uygulama yüklü şahsi cihazla alınması tek başına m.12'ye aykırılık oluşturmaz. Yine de genel ilkelere uyum bakımından işlemin bayilere tanımlanmış, denetlenen ve takip edilen kurumsal cihazlarla yapılması ve ilgili kişinin bu konuda aydınlatılması gerekir.
- **2020/608** (11.08.2020, Ulaşım, lojistik ve kargo) — Bir kullanıcının bildirim almak üzere sisteme sehven başkasına ait telefon numarasını girmesi, numaranın sahibini belirleyecek sistemsel bir eşleştirme imkânı bulunmadığı durumda tek başına veri sorumlusunun m.12 yükümlülüğünü ihlal ettiğini göstermez; ancak ilgili kişinin başvurusuna süresinde cevap verilmelidir.
- **2019/206** (08.07.2019, E-ticaret ve perakende) — Açık rıza bir ürün veya hizmetin ön şartı yapılamaz; ancak yalnızca indirim ve avantajların üyelere sunulması hizmetin açık rızaya bağlanması sayılmaz. Açık rıza dışında bir işleme şartı varken işlemenin açık rızaya dayandırılması aldatıcıdır ve hakkın kötüye kullanımıdır; aydınlatma metninde hukuki sebep açıkça gösterilmeli, aydınlatma ile açık rıza ayrı ayrı yerine getirilmelidir.

## Bakılacaklar (kararlardan çıkan kontrol maddeleri)

- Aydınlatma metni ile açık rıza metni ayrı başlıklar altında ayrı metinler mi; aynı sayfadaysa alt alta ve her biri için ayrı beyan/işaret kutusu var mı? *(2026/347)*
- Aydınlatma metninin altında "okudum ve kabul ediyorum", "okudum ve onaylıyorum", "okudum ve açık rıza veriyorum" gibi ifadeler yerine yalnızca "okudum ve anladım" türünde bir beyan mı kullanılıyor? *(2026/347)*
- Açık rıza dışındaki bir işleme şartına dayanan faaliyetler için ilgili kişiden ayrıca açık rıza metni/onayı isteniyor mu (istenmemeli)? *(2026/347)*
- Aydınlatma, işleme şartı ne olursa olsun veri işlemeye başlamadan önce yapılıyor ve yapıldığı ispatlanabiliyor mu; açık rızanın alındığı da ispatlanabiliyor mu? *(2026/347)*
- Metinler başka bir veri sorumlusundan birebir kopyalanmamış, kuruluşun kendi organizasyon ve faaliyetlerine göre mi hazırlanmış; yanıltıcı/yanlış bilgi (ör. yapılmayan yurt dışı aktarımı izlenimi) ve "Kanun'un 5 ve 6. maddelerindeki şartlar kapsamında işlenmektedir" gibi muğlak ifadeler içermiyor mu? *(2026/347)*
- Aydınlatma metni sade ve kısa mı (ör. 11. maddenin tamamı yerine "Kanun'un 11. maddesi kapsamındaki haklarınız" atfı); işlenen veriler ve kategorileri ile her faaliyetin amacı ve hukuki sebebi açık ve net belirtilmiş mi? *(2026/347)*
- Kasada yalnız cep telefonu numarası veya sadakat kart numarası söylenerek, doğrulama ya da üyenin önceden verdiği opt-in onay olmadan sadakat kart üzerinden işlem (puan kazanma, indirim/promosyon dahil) yapılamıyor *(2026/266)*
- Sadakat kartın her kullanım türü için bir doğrulama adımı var: SMS tek kullanımlık kod, uygulama/site barkod ya da QR kodu, fiziki kartın okutulması veya kart şifresi *(2026/266)*
- Yalnız telefon numarasıyla işleme izin veriliyorsa, üye çevrim içi hesabından hangi işlemlere (alışveriş/puan kazanma, indirim/promosyon, puan harcama) onay verdiğini opt-in olarak seçmiş; varsayılan kapalı *(2026/266)*
- Doğrulanmamış bir alışveriş için üye adına fatura düzenlenmiyor ve alışveriş bilgisi üyenin hesabına/işlem geçmişine işlenmiyor *(2026/266)*
- Üyelik sözleşmesindeki 'kart üçüncü kişilere kullandırılamaz' hükmü tek tedbir olarak kullanılmıyor; teknik doğrulama ayrıca mevcut *(2026/266)*
- Doğrulama mekanizmaları ilke kararının yayımından itibaren 6 ay içinde devreye alınmış *(2026/266)*
- Giriş/üyelik ekranlarında, sözleşmenin ifası veya hukuki yükümlülük gibi başka bir şarta dayanan işlemeler için açık rıza onay kutucuğu bulunmamalı. *(2024/1393)*
- Hizmetten yararlanmak, açık rıza niteliğindeki bir kutucuğun işaretlenmesi şartına bağlanmamalı. *(2024/1393)*
- Her veri işleme faaliyetinin dayandığı m.5 işleme şartı envanterde belirlenmiş ve ekrandaki onay metinleriyle tutarlı olmalı. *(2024/1393)*
- CDN/önbellek yapılandırmasında kimliği doğrulanmış kullanıcıya özel sayfalar ve yanıtlar (hesap, adres, sipariş) önbelleğe alınmamalı. *(2023/1796)*
- Önbellek, yama ve konfigürasyon değişiklikleri canlıya alınmadan önce bir kullanıcının verisinin başka kullanıcıya gösterilmediğini doğrulayan testlerden geçirilmeli. *(2023/1796)*
- Veri işleyenle yapılan sözleşmede tedbir yükümlülüğü ona bırakılmış olsa bile veri sorumlusu veri işleyenin süreçlerini denetlemeli veya denetletmeli. *(2023/1796)*
- Usule uygun olmayan kanaldan gelen ilgili kişi başvurusuna esasa ilişkin yanıt verildiyse başvuru usul eksikliği gerekçesiyle yok sayılmamalı. *(2023/1796)*
- Toplu gönderim ile kişiye özel gönderim işlevleri arayüzde ayrı sekme/ekranlarda ve açıkça ayırt edilebilir olmalı. *(2023/1675)*
- Kişisel veriye erişen çalışanlara veri koruma ve bilgi güvenliği eğitimi verildiği belgelenmeli. *(2023/1675)*
- Çalışanlarla gizlilik taahhütnamesi imzalanmış ve veri güvenliği ihlalleri için disiplin süreci tanımlanmış olmalı. *(2023/1675)*
- Yanlış gönderimden sonra alıcılardan verinin silindiğine ve paylaşılmayacağına dair teyit alınmalı. *(2023/1675)*
- Biyometrik (yüz) doğrulama içeren akışta biyometrik veri işlenmeden aynı işlemi tamamlamayı sağlayan en az bir alternatif yöntem bulunmalı. *(2023/1310)*
- Kullanıcı biyometrik veri açık rızasını reddettiğinde akış sessizce başa dönmemeli, alternatif yöntem ve kanallar aynı ekranda gösterilmeli. *(2023/1310)*
- Alternatif kanal bilgisi internet sitesinin ayrı bir bölümünde değil, işlemin yapıldığı adımda erişilebilir olmalı. *(2023/1310)*
- Rezervasyon/check-in ekranına rezervasyon kodu ve soyadı ile giren kullanıcı, aynı grup kaydındaki farklı soyadlı yolcuların kimlik, pasaport ve vize bilgilerini görememeli. *(2023/1309)*
- Yalnız soyadı eşleşmesiyle birlikte görüntüleme yapılıyorsa, aynı soyadlı ama birlikte seyahat etmeyen yolcuları ayıracak ek doğrulama bulunmalı. *(2023/1309)*
- Kullanıcıların başkasının verisini görebildiği tespit edildiğinde olay veri ihlali olarak kaydedilip Kurula bildirilmeli. *(2023/1309)*
- Plaka, T.C. kimlik no gibi tek bir bilgiyle borç/bilgi sorgulanan internet sayfalarında ikinci kademe olarak SMS/e-posta ile iletilen kod, kişiye özel şifre veya üyelik girişi zorunlu olmalı. *(2023/924)*
- İkinci doğrulama adımında doğum tarihi, anne-baba adı, telefon numarası gibi başkalarının da bilebileceği bilgiler kullanılmamalı. *(2023/924)*
- Hizmetten yararlanan kişilere (ör. otopark kullanıcıları) verilerin hangi durumlarda işleneceğini de belirten, Tebliğ'e uygun bir aydınlatma metni sunulmalı ve aydınlatmanın yapıldığı ispatlanabilir olmalı. *(2023/924)*
- Veri işleme açık rıza dışındaki bir şarta dayansa bile aydınlatma adımı sürecin içinde yer almalı. *(2023/924)*
- Temel ürün veya hizmet, pazarlama amaçlı açık rıza verilmeden de satın alınabilir ve kullanılabilir olmalı. *(2023/890)*
- Açık rıza koşuluna bağlanan unsur yalnızca sadakat programı gibi ek menfaat sağlayan üyelik olmalı. *(2023/890)*
- Kullanıcı, mevcut puan/mil gibi bilgilerini rıza kutusunu işaretlemeden ya da alternatif kanallardan (çağrı merkezi, form, satış ofisi) görüntüleyebilmeli. *(2023/890)*
- Randevu/başvuru formunda tanıtım ve duyuru iletişimi onay kutucuğu isteğe bağlı olmalı; işaretlenmeden de formda ilerlenebilmeli. *(2023/692)*
- Aydınlatma metnine ilişkin kutucuk yalnızca "okudum" beyanı içermeli, "verilerimin işlenmesine onay veriyorum" ifadesi bulunmamalı. *(2023/692)*
- Sözleşme, hukuki yükümlülük veya meşru menfaat şartına dayanan zorunlu form verileri için ayrıca açık rıza istenmemeli. *(2023/692)*
- Açık rızaya dayanan işlemeler için açık rıza metni aydınlatma metninden ayrı düzenlenmeli; aynı kural şikâyet formu ve mobil sürümde de uygulanmalı. *(2023/692)*
- Siteye ilk girişte, kullanıcı aktif olarak onay vermeden zorunlu olmayan (analitik, işlevsel, reklam/pazarlama) hiçbir çerez yerleştirilmemeli. *(2022/1358)*
- Çerez tercih panelinde zorunlu olmayan çerez kategorileri varsayılan olarak kapalı gelmeli. *(2022/1358)*
- İlk ziyarette çerezlerle işlenen verilere ilişkin, m.10 ve Aydınlatma Tebliği'ndeki zorunlu unsurları içeren bir çerez aydınlatma metni sunulmalı. *(2022/1358)*
- Üyelik/kayıt formundaki aydınlatma metni veri sorumlusunun kimliği, amaç, aktarım (yurt dışı dahil), toplama yöntemi, hukuki sebep ve m.11 haklarını eksiksiz içermeli. *(2022/1358)*
- Kullanıcıya özel profil/üyelik sayfası yanıtlarının önbelleğe (cache/CDN) alınmadığı doğrulanmalı. *(2022/707)*
- Kampanya öncesi yapılan mobil uygulama güncellemelerinden sonra bir kullanıcının başka kullanıcının verisini görmediği test edilmeli. *(2022/707)*
- Müşteri bildirimi ile gelen ihlal şüphesinde sistemi kapatmayı da içeren müdahale adımları tanımlı olmalı. *(2022/707)*
- Veri işleyen/tedarikçi sistemleri üzerinde veri sorumlusu tarafından denetim yapıldığı belgelenebilmeli. *(2022/707)*
- Çevrim içi ödeme, hızlı ödeme ve borç sorgulama ekranları yalnızca TC kimlik numarası (veya tek bir tanımlayıcı) girilerek kişiye ait bilgileri göstermiyor mu? *(2022/388)*
- Bu ekranlara erişim üyelik ve şifre ya da çift faktörlü doğrulama ile mi sağlanıyor? *(2022/388)*
- İkinci doğrulama adımı, kişiye özel oluşturulmuş şifre ya da ilgili kişinin daha önce bildirdiği telefona/e-postaya iletilen SMS kodu/şifre gibi yalnız ilgili kişinin erişebileceği bir veriye mi dayanıyor? *(2022/388)*
- Doğum tarihi, anne baba adı, telefon numarası, sicil no gibi başkalarının da bilebileceği bilgiler ikinci faktör olarak kullanılmıyor mu? (TC kimlik no + doğum günü tek kademeli doğrulama sayılır.) *(2022/388)*
- Uzaktan erişilen kişisel veriler için risk değerlendirmesi yapılmış ve doğrulama yöntemi buna göre seçilmiş mi? *(2022/388)*
- Misafir (üyeliksiz) alışveriş akışında girilen e-posta adresi ve telefon numarası, fatura ya da sipariş bilgisi gönderilmeden önce doğrulama kodu/bağlantısı ile teyit edilmeli. *(2022/243)*
- Doğrulanmamış bir e-posta adresine ad, soyad, adres, T.C. kimlik numarası ya da sipariş içeriği barındıran fatura/ileti gönderilmemeli. *(2022/243)*
- Site ve mobil uygulama ilk açılışta zorunlu olmayan (işlevsel, analitik, reklam/pazarlama) çerezleri kullanıcı aktif olarak onaylamadan yüklememeli; çerez tercihleri varsayılan olarak kapalı gelmeli. *(2022/229)*
- Çerez bildirimi yalnızca bilgilendirme yapan bir pop-up olmamalı; zorunlu olmayan çerezler için kullanıcının aktif onayını alan bir açık rıza mekanizması içermeli. *(2022/229)*
- Üçüncü taraf çerezleriyle yurt dışına veri aktarımı varsa m.9'a uygun bir aktarım dayanağı (açık rıza ya da öngörülen diğer usul) belgelenmiş olmalı. *(2022/229)*
- Çerez Politikası, her çerez için amaç, hukuki sebep, toplama yöntemi, aktarım alıcıları ve m.11 haklarını anlaşılır biçimde içermeli ve Gizlilik Politikasından doğrudan bağlantıyla erişilebilmeli. *(2022/229)*
- Hiçbir form, ödeme veya onay ekranında kullanıcıdan e-Devlet şifresi istenmemeli. *(2022/137)*
- Üyelik oluşturma formunda T.C. kimlik numarası zorunlu alan olmamalı ve diğer alanların açılması bu bilgiye bağlanmamalı. *(2022/137)*
- Kayıt/hesap oluşturma sayfasına bir tanımlayıcı (T.C. kimlik no, e-posta, telefon) girildiğinde mevcut üyeye ait ad, soyad, adres gibi veriler kimlik doğrulaması olmadan ekrana getirilmemeli. *(2022/137)*
- Kişisel verilere üçüncü kişilerin eriştiği bir açık tespit edildiğinde m.12/5 uyarınca Kurula ihlal bildirimi yapılmalı. *(2022/137)*
- Borçlu/icra takibi listeleri (ad, T.C. kimlik no, adres, plaka) kimlik doğrulaması olmadan erişilebilen hiçbir internet adresinde yayımlanmamalıdır. *(2021/1110)*
- Tahsilat veya araç yakalama süreçlerinde üçüncü kişilerle paylaşılan sorgu ekranları yalnızca yetkilendirilmiş kullanıcı adı ve şifresiyle erişilebilir olmalıdır. *(2021/1110)*
- Kullanıcı hesabındaki kayıtlı adresler, geçmiş siparişlerin faturasında kullanılmış olsa bile profil ekranından silinebilmeli ve düzenlenebilmeli. *(2021/847)*
- Fatura/sipariş kayıtlarındaki adres verisi profil adres defterinden ayrı tutulmalı; profilden silinen adres kullanıcıya gösterilmemeli ve yalnız saklama amacıyla (arşivde) tutulmalı. *(2021/847)*
- Arayüzde görünen 'Sil' ve 'Düzenle' düğmeleri fiilen çalışmalı; işlevsiz seçenek sunulmamalı. *(2021/847)*
- Yasal saklama yükümlülüğü nedeniyle tutulan veriler saklama amacı dışında kullanılmamalı ve saklama süresi her fatura tarihi için ayrı hesaplanmalı. *(2021/847)*
- Kimlik belgesi görüntüsü alan mobil uygulama, görüntüyü cihazda saklamamalı ve personelin çekilen görüntüye sonradan erişmesine izin vermemeli. *(2021/850)*
