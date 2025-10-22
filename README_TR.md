
# AlgoSapiens: Sıfırdan Yaratıcı Bir Zekâ İnşa Etmek

## 1. Misyon & Felsefe: Kâr Değil, Eğitim

> **PROJE UYARISI: Bu bir al-sat botu DEĞİLDİR. Amacı finansal kazanç DEĞİLDİR.**

`AlgoSapiens` tamamen **eğitim amaçlı** bir girişimdir. Bu kişisel bir meydan okumadır—bir bilgisayar bilimi, istatistik ve uygulamalı mantık egzersizidir.

Misyon, `TensorFlow` veya `XGBoost` gibi hazır modelleri sihirli bir "kara kutu" olarak kullanmak yerine, bir karar verme motorunu en temel bileşenlerinden başlayarak inşa eden kişisel gelişim yolculuğunu belgelemektir.

Amaç, *para kazanan* bir araç yaratmak değil, şu soruyu yanıtlamaktır:
**"Kaosun içinde anlamlı kalıpları bulmayı *öğrenen* bir program yazabilir miyim ve bu süreç bana 'öğrenme'nin doğası hakkında ne öğretebilir?"**

## 2. Teknik Problem: Bir "Öğrenme" Çerçevesi

Bu eğitim hedefine ulaşmak için, `AlgoSapiens`imizin çözmesi gereken net bir teknik problem tanımlıyoruz. Bu bir **ikili sınıflandırma problemidir**:

> "Bir dizi geçmiş veri (özellikler) göz önüne alındığında, belirli bir kalıbın (hedefimizin) ortaya çıkma olasılığı nedir?"

* **Hedef = 1 (Doğru):** Evet, tanımlanan kalıp başarıyla tespit edildi.
* **Hedef = 0 (Yanlış):** Hayır, kalıp tespit edilmedi (bu bir gürültüydü).

Modelin amacı, "geçmiş" (özellikler) ve bu "gelecek" (hedef) arasındaki karmaşık, doğrusal olmayan ilişkileri öğrenmektir.

## 3. Yaklaşım: Aşamalı Bir Metodoloji

Bu proje, her biri bir öncekinin üzerine inşa edilen mantıksal aşamalar halinde ilerlemektedir.

### Aşama 1: Temel (Veri ve Özellik Mühendisliği)

"Düşünme" gerçekleşmeden önce "duyular" sağlamalıyız. Bu aşama veriyi hazırlamakla ilgilidir.
1.  **Veri Toplama:** Geçmiş verilerin (örneğin bir finans piyasasından OHLCV, ancak bu herhangi bir veri seti olabilir) elde edilmesi.
2.  **Veri Hazırlama:** Verinin temizlenmesi ve `pandas` kullanılarak yapılandırılması.
3.  **Etiketleme:** "Problem" bölümünde tanımlandığı gibi, her bir zaman adımı için "Hedef"in (1 veya 0) oluşturulması.
4.  **Özellik Mühendisliği:** Modelin kullanacağı "ipuçlarını" (özellikleri) manuel olarak oluşturma. Burası, neyin önemli olabileceğini *varsaydığımız* yerdir (örn: gecikme değerleri, hareketli ortalamalar, istatistiksel özellikler).

### Aşama 2: Çekirdek Algoritma (Sıfırdan "Beyin")

Burası projenin kalbidir. Yalnızca Python ve NumPy/Pandas kullanarak bir **Karar Ağacı (Decision Tree)** algoritması uygulayacağız. Bu, şunları kodlamayı içerir:
1.  **"Bölünme" Mantığı:** Tüm özellikleri ve tüm olası eşik değerlerini (örn: "`özellik_A` < 30 mu?") yineleyerek veriyi bölen *en iyi tek soruyu* bulan bir fonksiyon.
2.  **Saflık Metriği:** Hangi "sorunun" en iyisi olduğuna matematiksel olarak karar vermek için bir puanlama sistemi (örn: **Gini Kirliliği** veya **Bilgi Kazancı/Entropi**) uygulama.
3.  **"Büyüme" Mantığı:** Bölünme mantığını tekrar tekrar uygulayan, bir sonuca (bir "yaprak" düğüme) ulaşana kadar sorulardan oluşan bir "ağaç" inşa eden **özyinelemeli (recursive)** bir fonksiyon.

### Aşama 3: Değerlendirme ve İyileştirme ("Öğrenmeyi" Ölçme)

Bir model, ancak onun "düşüncelerini" anlama yeteneğimiz kadar iyidir. Amaç kârı ölçmek değildir.
1.  **Geriye Dönük Test (Backtesting):** Modelin daha önce *hiç görmediği* geçmiş veriler (test seti) üzerindeki performansını simüle etmek için bir çerçeve.
2.  **Metrikler:** Başarıyı, tahminsel gücüne göre ölçme: **Doğruluk (Accuracy), Kesinlik (Precision), Duyarlılık (Recall) ve F1-Skoru**. Amaç, kalıbı *gerçekten öğrenip öğrenmediğini* görmektir.
3.  **Ayarlama:** **Aşırı öğrenmeyi (overfitting)** (geçmişi "öğrenmek" yerine sadece "ezberlemek") önlemek için modelin karmaşıklığını (örn: ağacın maksimum derinliği `max_depth`) kontrol etme.

### Aşama 4: Vizyon (Zihni Genişletme)

Tek bir "nöron" (Karar Ağacı) anlaşıldıktan sonra, daha karmaşık bir "beyin" (Topluluk modelleri) için temel atılmış olur:
* **Random Forest:** Sıfırdan birden fazla ağaç inşa etmek ve "oy kullanmalarına" izin vermek.
* **Gradient Boosting:** Bir ağaç inşa etmek, ardından ilk ağacın *hatalarını* tahmin etmeye çalışan *ikinci* bir ağaç inşa etmek ve bu böyle devam eder.

## 4. Kullanılan Teknolojiler

* **Python 3.x**
* **Pandas:** Tüm veri manipülasyonu ve özellik mühendisliği için.
* **NumPy:** Yüksek performanslı sayısal hesaplamalar için.
* **(Opsiyonel) Plotly / Matplotlib:** Verileri ve sonuçları görselleştirmek için.

---
**Uyarı:** Bu proje **YALNIZCA eğitim ve kişisel gelişim amaçlıdır**. Bu, makine öğrenmesini anlamak için yapılan bir kodlama egzersizidir. Üretilen modeller ve sinyaller finansal tavsiye **değildir** ve bu projenin tanımlanmış eğitim kapsamı dışında herhangi bir karar alma amacıyla kullanılmamalıdır.
