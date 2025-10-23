# AlgoSapiens Değişim Günlüğü

Bu projede yapılan tüm önemli değişiklikler bu dosyada belgelenecektir.

Biçim, [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standardına dayanmaktadır ve proje [Anlamsal Sürümlemeyi (Semantic Versioning)](https://semver.org/spec/v2.0.0.html) takip eder.

## [0.0.1] - 2025-10-22

### Eklendi (Added)

- **Proje Başlatma:** `AlgoSapiens` deposu (repository) oluşturuldu.
- **İlk Dokümantasyon:**
  - `README.md`: Projenin temel misyonu, "önce eğitim" felsefesi ve çok aşamalı geliştirme planı eklendi.
  - `CHANGELOG.md`: Gelecekteki tüm sürümleri ve önemli değişiklikleri izlemek için bu dosya oluşturuldu.
- **İlk `.gitignore`:** Standart bir Python `.gitignore` dosyası eklendi (yaygın geçici dosyaları, `__pycache__` ve sanal ortamları sürüm kontrolü dışında tutmak için).

## [0.1.0] - 2025-10-23

### Eklendi
- Aşama 1'de tanımlanan temel veri hattı script'leri (`datacollection/` klasörü) eklendi.
- `data_collection.py`: Binance API'sinden toplu geçmiş mum verisi çekmek için yeni script eklendi.
- `data_read.py`: Diskteki veriyi okuyup pandas DataFrame'e yüklemek için yeni script eklendi.
- Yüksek hızlı okuma/yazma (I/O) performansı ve ölçeklenebilirlik için (50k satırla başarıyla test edildi) CSV/Excel yerine `.parquet` dosya formatı tercih edildi.

### Değiştirildi
- **KRİTİK:** `data_collection.py`, `volume` (örn: BTC adedi) yerine `quote_asset_volume` (örn: USDT değeri) çekecek şekilde güncellendi. Bu, finansal güç için çok daha doğru bir sinyaldir.
- Gelecekteki özelliklerde tutarlı kullanım için `quote_asset_volume` sütununun adı DataFrame içinde `volume` olarak yeniden adlandırıldı.

### Düzeltildi
- Depo kirliliğini önlemek için `.DS_Store` (macOS sistem dosyaları) `.gitignore` dosyasına eklendi.
- Ayrışan dal (divergent branch) sorunlarını 'merge' stratejisiyle çözmek için global `git config pull.rebase false` ayarı yapıldı.
- Commit yazarı (author) hatalarını çözmek için global `git config user.name` ve `user.email` ayarları yapıldı.