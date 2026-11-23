# Ekran görüntüsü ve arayüz denetimi

Ekran görüntüsü yalnız ilgili kişiye ne gösterildiğini kanıtlar; arka planda ne işlendiğini göstermez. Görüntüde gördüğünüzü yazın, görmediğinizi varsaymayın, sonucu etkileyen eksikleri "ekrandan anlaşılamıyor" diye ayrıca sorun. Kural koyan cümleler için rehberlerdeki kararları esas alın.

## Önce ekranı tarif et

- Ekranın türü: üyelik/kayıt, giriş, sipariş, başvuru, iletişim formu, çerez bandı, ayarlar/tercihler, onay penceresi, SMS/e-posta içeriği, kamera uyarı levhası.
- İstenen alanlar ve hangilerinin zorunlu olduğu.
- Onay kutuları: sayısı, metinleri, başlangıçta işaretli olup olmadığı, zorunlu olup olmadığı.
- Bağlantılar: aydınlatma metni, açık rıza metni, çerez politikası, ticari ileti izni.
- Düğmeler: "Kabul et" ile "Reddet" aynı görünürlükte mi, ilerlemek için hangisi gerekli?

## Formlar ve onay kutuları

- Aydınlatma metni ile açık rıza aynı metinde ya da tek kutuda birleştirilmiş mi; aydınlatmaya "okudum, kabul ediyorum / rıza veriyorum" onayı isteniyor mu? İlke kararı: `ara.py --no 2026/347 --tam`. Rehberler: `konular/aydinlatma-yukumlulugu.md`, `konular/acik-riza.md`.
- Üyelik sözleşmesi, pazarlama izni ve açık rıza tek kutuya bağlanmış mı; kutu ön işaretli mi; işaretlenmeden devam edilemiyor mu (hizmetin rıza şartına bağlanması)? Arama: `ara.py hizmetin açık rıza şartına bağlanması`.
- Açık rıza gerekmeyen bir işleme için (sözleşmenin ifası, hukuki yükümlülük) rıza isteniyor mu? Bu da yanıltıcı sayılabilir: `konular/isleme-sartlari-m-5.md`.
- İstenen alanlar amaca göre fazla mı: TCKN, doğum tarihi, kimlik fotoğrafı, cinsiyet, meslek? `konular/genel-ilkeler-m-4.md`. Konaklamada kimlik fotokopisi: `ara.py --no 2025/2120 --tam`.
- Aydınlatma metnine veri toplanırken ve kolay erişilir biçimde ulaşılıyor mu (bağlantı çalışıyor, sayfanın dibine gömülmemiş, form gönderilmeden önce görülebiliyor)?
- Özel nitelikli veri (sağlık beyanı, engel durumu, biyometrik kayıt) isteyen alan var mı? `konular/ozel-nitelikli-veri.md`.

## Çerez bandı ve tercih paneli

- Reddetme seçeneği ilk katmanda ve kabul kadar kolay mı; bant kapatılınca ya da sayfa kaydırılınca rıza varsayılıyor mu?
- Zorunlu olmayan kategoriler ön işaretli mi; kategoriler ve amaçları açık mı?
- Tercih sonradan değiştirilebiliyor mu?
- Ekran tek başına çerezlerin tercih öncesi yüklenip yüklenmediğini göstermez; ağ isteklerinin ya da kodun da incelenmesini isteyin (`kod-denetimi.md` §4).
- Rehber: `konular/cerez-ve-cevrim-ici-izleme.md`.

## İletiler (SMS, e-posta, bildirim, arama metni)

- Pazarlama iletisinde ret imkânı gösterilmiş mi; gönderen kim?
- Doğrulama kodu iletisine onay ya da izin metni eklenmiş mi ("kodu söylemeniz rıza anlamına gelir")? İlke kararı: `ara.py --no 2025/1072 --tam`.
- İletide başkasına ait veri ya da gereğinden fazla kişisel veri var mı (yanlış numaraya giden sonuç, borç bilgisi)? `konular/kimlik-dogrulama-ve-yanlis-kisiye-gonderim.md`.
- Rehber: `konular/pazarlama-iletileri-sms-arama-e-posta.md`.

## Sorgulama ve sonuç ekranları

- Yalnız TCKN, plaka, telefon ya da abone numarası girilerek başkasının bilgisine ulaşılabiliyor mu; ek doğrulama var mı? `ara.py --kaynak ilke sorgulama`, `ara.py borç sorgulama`.
- Liste ya da ilan ekranında kişilerin adı, borcu, sınav sonucu, sağlık durumu açıkça görünüyor mu; maskeleme var mı? `ara.py --kaynak ilke internet ortamında paylaşılması`, `ara.py --kaynak ilke apartman`.
- Gişe, banko, kiosk ekranında bir önceki kişinin bilgisi görünür kalıyor mu? `ara.py --kaynak ilke banko`.

## Fiziksel ortam fotoğrafları

- Kamera uyarı levhası ve aydınlatma, kameranın gördüğü alan (soyunma, dinlenme alanı), ses kaydı: `konular/kamera-ve-goruntu-ses-kaydi.md`.
- Parmak izi ya da yüz tanıma cihazı: `konular/biyometrik-veri.md`, `ara.py --no 2026/921 --tam`.
- Panoya asılmış liste, borç ilanı, vardiya çizelgesi: `ara.py --kaynak ilke apartman`.

## Raporlama

Her bulguda ekrandaki öğeyi (konumu ve metniyle) gösterin, sorunu ve dayanak kararı yazın, öğenin nasıl olması gerektiğini somut tarif edin (ör. iki ayrı, işaretsiz kutu; aydınlatma için yalnız "okudum" ifadesi). Ekrandan anlaşılamayanları ayrı bir "doğrulanmalı" listesinde toplayın: saklama süresi, aktarım, onayın kaydı, kutunun arka planda neyi tetiklediği.
