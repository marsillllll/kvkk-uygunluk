# Kod, şema ve altyapı denetimi

Kodda hukuki sonuç yazmaz; ama hangi verinin nereden toplandığı, nereye gittiği ve ne kadar tutulduğu kodda yazar. Amaç bunları çıkarıp Kurulun kararlarıyla eşleştirmektir. Aşağıdaki her başlık için önce kodda ne aranacağı, sonra hangi rehbere ve hangi aramaya bakılacağı verilmiştir. Kural koyan cümleler için rehberlerdeki kararları esas alın; bu dosya yalnız yol haritasıdır.

## 1. Veri envanterini koddan çıkar

- Şema, model, migration, DTO ve form tanımlarında kişisel veri alanlarını listele: ad-soyad, TCKN, telefon, e-posta, adres, doğum tarihi, IP, cihaz kimliği, konum, IBAN/kart, fotoğraf, ses.
- Özel nitelikli olanları ayır: sağlık, biyometrik (parmak izi, yüz şablonu), ceza mahkûmiyeti, din, sendika, genetik. Rehber: `konular/ozel-nitelikli-veri.md`, `konular/biyometrik-veri.md`, `konular/saglik-verisi.md`.
- Her alan için amaç sor: bu alan hangi işlev için gerekli? Kullanılmayan ya da "ileride lazım olur" diye toplanan alan ölçülülük sorunudur. Rehber: `konular/genel-ilkeler-m-4.md`. Arama: `ara.py ölçülülük fazla veri`.
- Çocuk kullanıcı ihtimali varsa (yaş alanı, veli onayı akışı): `konular/cocuklarin-verisi.md`.

## 2. Toplama noktaları ve hukuki sebep

- Kayıt, üyelik, sipariş, başvuru formları ve bunların API uçları: hangi alan zorunlu, hangi onay alanı (`consent`, `kvkk_onay`, `marketing_opt_in`) var, varsayılan değeri ne?
- Onay alanı varsayılan olarak `true` geliyorsa, tek bir alan hem sözleşmeyi hem pazarlamayı hem aydınlatmayı kapsıyorsa ya da hizmet onaya bağlanmışsa: `konular/acik-riza.md`, `konular/aydinlatma-yukumlulugu.md`. Bu konuda ilke kararı var: `ara.py --no 2026/347 --tam`.
- Onayın kaydı: kim, ne zaman, hangi metin sürümüne onay verdi tutuluyor mu? İspat yükü veri sorumlusundadır.
- Rıza geri alma ve tercih değiştirme akışı kodda var mı, geri alınınca işleme gerçekten duruyor mu?

## 3. Pazarlama iletileri

- SMS, e-posta, push, arama tetikleyen kod ve kuyruklar: gönderim öncesi izin kontrolü yapılıyor mu, ret listesi uygulanıyor mu?
- Doğrulama kodu (OTP) SMS'inin içine pazarlama izni ya da başka bir onay gömülüyor mu? İlke kararı: `ara.py --no 2025/1072 --tam`.
- Üçüncü kişinin numarasının ("arkadaşını öner", sadakat kartı) işlenmesi: `ara.py --kaynak ilke sadakat`.
- Rehber: `konular/pazarlama-iletileri-sms-arama-e-posta.md`.

## 4. Çerez, SDK ve çevrim içi izleme

- Sayfa yüklenirken, kullanıcı tercih yapmadan çalışan analitik/reklam betikleri (etiket yöneticisi, piksel, yeniden pazarlama) var mı?
- Zorunlu olmayan çerezler için ret seçeneği kabul kadar kolay mı; tercih kaydediliyor ve betik yüklemesi buna bağlı mı?
- Mobil SDK'lar (analitik, reklam kimliği, çökme raporu) hangi veriyi nereye gönderiyor?
- Rehber: `konular/cerez-ve-cevrim-ici-izleme.md`, `konular/mobil-uygulama-ve-internet-sitesi-tasarimi.md`.

## 5. Aktarım: üçüncü taraflar ve yurt dışı

- Dış servis çağrılarını listele: bulut sağlayıcı ve bölgesi, e-posta/SMS sağlayıcı, CRM, ödeme, analitik, yapay zekâ API'leri, hata izleme. Her biri için: hangi veri gidiyor, sunucu nerede?
- Yurt dışındaki bir servise kişisel veri gidiyorsa `konular/yurt-disina-aktarim.md` ve `mevzuat-notlari.md` (m.9, 1 Haziran 2024 değişikliği). Eski kararlar eski metne göredir.
- Veri işleyenle sözleşme ve denetim: `konular/veri-isleyen-iliskisi.md`. Grup şirketi, iş ortağı, bayi paylaşımı: `konular/yurt-ici-aktarim.md`.

## 6. Veri güvenliği (m.12)

Kurulun ceza verdiği kararların çoğu bu başlıktadır. Kodda ve yapılandırmada bak:

- Kimlik doğrulama: parola saklama biçimi, çok faktörlü doğrulama, oturum süresi, parola sıfırlama akışının başkasının hesabını ele geçirmeye izin verip vermediği.
- Yetkilendirme: nesne düzeyinde yetki kontrolü (başkasının kaydını kimlik numarasını değiştirerek görebilme), rol ayrımı, yönetici panellerinin erişimi.
- Sıralı ya da tahmin edilebilir kimlikler, sorgu numarasıyla açılan sayfalar, kimlik doğrulaması olmayan sorgulama ekranları: `ara.py sorgulama ekranı doğrulama`, `ara.py --kaynak ilke belediye`.
- Loglar: kişisel veri loglanıyor mu, erişim kayıtları tutuluyor mu, loglar ne kadar saklanıyor?
- Şifreleme: aktarımda ve depoda; özel nitelikli veri için ek tedbirler (`ara.py --no 2018/10 --tam`).
- Sırlar: depoda açık anahtar, parola, bağlantı dizesi; test ortamında gerçek veri.
- Açık depolama alanları, herkese açık yedekler, dizin listeleme, hata mesajlarında veri sızıntısı.
- Yanlış kişiye gönderim riski: e-posta/SMS alıcısının doğrulanması, toplu gönderimde açık alıcı listesi. Rehber: `konular/kimlik-dogrulama-ve-yanlis-kisiye-gonderim.md`.
- Çalışan erişimi: müşteri kaydını sorgulayan personelin yetki sınırı ve iz kaydı. Rehber: `konular/yetkisiz-erisim-ve-calisan-kaynakli-ihlal.md`.
- Rehberler: `konular/veri-guvenligi-ve-teknik-idari-tedbirler.md`, `konular/siber-saldiri.md`.

## 7. İhlal tespiti ve bildirimi

- İhlali fark ettirecek izleme ve alarm var mı; olay kaydı ve müdahale adımları tanımlı mı?
- Kurula ve ilgili kişilere bildirim süreci: `konular/veri-ihlali-bildirimi-72-saat.md`, usul kararı `ara.py --no 2019/10 --tam`.

## 8. Saklama ve silme

- Kayıtlar için saklama süresi tanımlı mı; süresi dolanı silen ya da anonimleştiren iş (cron, TTL) var mı?
- "Silindi" işareti koyup veriyi tutmak, yedeklerde ve loglarda bırakmak, hesabı kapatılan kullanıcının verisini pazarlamada kullanmaya devam etmek.
- Kullanıcının silme ve erişim talebini karşılayan bir akış var mı, 30 günlük süre izleniyor mu? Rehberler: `konular/silme-yok-etme-saklama-suresi.md`, `konular/ilgili-kisi-basvurusu-ve-cevap-suresi.md`.

## 9. Çalışan izleme ve işyeri sistemleri

- Kurumsal e-posta, mesajlaşma, ekran/klavye izleme, konum takibi: `ara.py --no 2026/2035 --tam`.
- Parmak izi, yüz tanıma ile mesai ya da giriş kontrolü: `ara.py --no 2026/921 --tam`, `konular/biyometrik-veri.md`.
- Kamera ve ses kaydı: `konular/kamera-ve-goruntu-ses-kaydi.md`. Genel: `konular/calisan-verileri-isci-isveren.md`.

## Raporlama

Her bulguda dosya ve satırı, gözlenen davranışı, ilgili maddeyi, dayanak kararı ve somut kod düzeltmesini verin. Kodda göremediğiniz ama sonucu etkileyen şeyleri (sözleşmeler, aydınlatma metni, sunucu konumu, saklama politikası) "koddan anlaşılamıyor, şunu doğrulayın" diye ayrı listeleyin.
