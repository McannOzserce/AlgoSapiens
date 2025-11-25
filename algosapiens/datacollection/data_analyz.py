import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
from pathlib import Path

# --- 1. DOSYA YOLU AYARLAMALARI (SENİN DÜZELTTİĞİN KISIM) ---

script_path = Path(__file__).resolve()

# Scriptin olduğu klasör (örn: .../AlgoSapiens/datacollection/)
script_dir = script_path.parent

# Proje ana dizini (örn: .../AlgoSapiens/)
project_root = script_dir.parent

# Dosya isimleri
okunacak_dosya_adi = "btcusdt_5m_50000.parquet"
yazilacak_dosya_adi = "btcusdt_5m_50000_islenmis.parquet"

# Tam dosya yollarını oluşturuyoruz
# Data klasörünün proje ana dizini altında 'data' isminde olduğunu varsayıyoruz
okunacak_path = project_root / 'data' / okunacak_dosya_adi
yazilacak_path = project_root / 'data' / yazilacak_dosya_adi

print(f"Okunacak dosya yolu: {okunacak_path}")
print(f"Yazılacak dosya yolu: {yazilacak_path}")


# --- 2. PARQUET İŞLEME KISMI ---

# Dosyanın var olup olmadığını kontrol edelim, yoksa hata almayalım
if not okunacak_path.exists():
    print(f"HATA: Dosya bulunamadı! Lütfen yolu kontrol et: {okunacak_path}")
else:
    # Parquet dosyasını açıyoruz
    parquet_dosyasi = pq.ParquetFile(okunacak_path)
    
    writer = None 
    BATCH_SIZE = 10000

    print("İşlem başlıyor...")

    for batch in parquet_dosyasi.iter_batches(batch_size=BATCH_SIZE):
        df = batch.to_pandas()
        
        yeni_degerler = []
        
        # Satır satır dönme işlemi
        for index, satir in df.iterrows():
            fiyat = satir['close'] # Sütun isminin 'close' olduğundan emin ol
            
            # --- ÖRNEK MANTIK ---
            if fiyat > 50000:
                sonuc = "Yuksek"
            else:
                sonuc = "Dusuk"
            # --------------------
            
            yeni_degerler.append(sonuc)
        
        # Yeni sütunu ekle
        df['trend_durumu'] = yeni_degerler
        
        # Tabloyu dönüştür
        yeni_table = pa.Table.from_pandas(df)
        
        # Yazıcıyı başlat (İlk turda)
        if writer is None:
            writer = pq.ParquetWriter(yazilacak_path, yeni_table.schema)
        
        # Yaz
        writer.write_table(yeni_table)

    if writer:
        writer.close()

    print(f"İşlem tamamlandı! Kaydedilen yer: {yazilacak_path}")