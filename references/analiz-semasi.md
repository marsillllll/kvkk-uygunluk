# Karar analizi şeması

Yeni bir karar özeti için `data/metin/<id>.txt` dosyasını baştan sona okuyup aşağıdaki alanlarla bir JSON nesnesi üretin. Nesneleri dizi olarak `data/analiz/parca/<ad>.json` dosyasına yazın; `scripts/birlestir.py` bunları `data/analiz.json` ile birleştirir.

Genel kural: yalnız metinde yazanı kullanın. Emin olamadığınız alanı boş (`""` ya da `[]`) bırakın.

| Alan | Tür | Açıklama |
|---|---|---|
| `id` | sayı | Metin dosyasının başındaki ID |
| `tarih` | `"YYYY-AA-GG"` | Karar tarihi; metinde yoksa `""` |
| `tur` | metin | `Şikâyet`, `İhbar`, `Veri ihlali bildirimi`, `Resen inceleme`, `Diğer` |
| `sektor` | metin | Aşağıdaki sektör listesinden biri |
| `veriSorumlusu` | metin | En çok 8 kelime. Ad kararda açıkça geçiyorsa ad, geçmiyorsa nitelik ("özel hastane") |
| `sonuclar` | dizi | `İdari para cezası`, `Talimat`, `İhlal yok / işlem yapılmasına yer yok`, `Hatırlatma / uyarı`, `Disiplin hükümleri (kamu)`, `Savcılığa bildirim`, `Kanun kapsamı dışında / incelenemez`, `İlke / genel düzenleme` (ilke kararları ve genel nitelikli Kurul kararları için), `Diğer`. Yalnız Kurulun bu kararda fiilen verdiği sonuçlar |
| `cezalar` | dizi | Her ceza için `{"tutar": TL tam sayı, "gerekce": "m.12/1 veri güvenliği tedbirlerinin alınmaması"}`. Tutar metinde yazdığı gibi; toplama ve tahmin yok. İddialarda ya da başka kararlara atıfta geçen tutarlar yazılmaz |
| `ihlalMaddeleri` | sayı dizisi | Kurulun ihlal edildiğine hükmettiği Kanun maddeleri. Yalnız anılan maddeler ve ceza hükmü olan 18. madde yazılmaz |
| `konular` | dizi | Aşağıdaki konu listesinden 1-6 adet, birebir yazımla |
| `ozet` | metin | 2-4 cümle: olay, Kurulun değerlendirmesi, sonuç. Kendi cümlelerinizle |
| `ilke` | metin | Benzer olaylara uygulanabilir ilke, 1-2 cümle. Kararın söylemediği bir şey eklenmez |
| `kontrol` | dizi | 1-4 somut, doğrulanabilir uygunluk kontrol maddesi (kod, ekran, form, süreç için). Karar somut ders içermiyorsa `[]` |
| `anahtar` | dizi | 3-8 anahtar kelime, küçük harf |

## Sektörler

Bankacılık ve finans · Sigorta · Sağlık · E-ticaret ve perakende · Telekomünikasyon · Teknoloji, yazılım ve internet platformları · Sosyal medya · Eğitim · Kamu kurumu · Hukuk, avukatlık ve icra · Ulaşım, lojistik ve kargo · Turizm, konaklama ve yeme-içme · Medya ve yayıncılık · Enerji ve altyapı · Sanayi ve üretim · Otomotiv · Gayrimenkul ve site yönetimi · İnsan kaynakları ve istihdam · Spor, eğlence ve oyun · Dernek, vakıf, sendika, siyasi parti · Gerçek kişi veri sorumlusu · Diğer

## Konular

Açık rıza · Aydınlatma yükümlülüğü · İşleme şartları (m.5) · Genel ilkeler (m.4) · Özel nitelikli veri · Veri güvenliği ve teknik/idari tedbirler · Veri ihlali bildirimi (72 saat) · Yurt içi aktarım · Yurt dışına aktarım · İlgili kişi başvurusu ve cevap süresi · Silme, yok etme, saklama süresi · Pazarlama iletileri (SMS, arama, e-posta) · Çerez ve çevrim içi izleme · Kamera ve görüntü/ses kaydı · Biyometrik veri · Çalışan verileri (işçi-işveren) · Sağlık verisi · Çocukların verisi · Unutulma hakkı ve arama motorları · Basın ve ifade özgürlüğü · Kimlik doğrulama ve yanlış kişiye gönderim · Yetkisiz erişim ve çalışan kaynaklı ihlal · Siber saldırı · VERBİS · Veri işleyen ilişkisi · İstisnalar (m.28) · Mobil uygulama ve internet sitesi tasarımı · Diğer

## Denetim

Analizi yazdıktan sonra ikinci bir geçişle metne karşı denetleyin: her ceza tutarı hüküm kısmında aynen geçiyor mu; `sonuclar` hüküm fıkrasıyla uyumlu mu; `ihlalMaddeleri` yalnız ihlal bulunan maddeler mi; `ozet` ve `ilke` metnin söylemediği bir şey iddia ediyor mu.
