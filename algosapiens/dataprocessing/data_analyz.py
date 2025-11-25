import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
from pathlib import Path

# --- 1. DOSYA YOLU AYARLAMALARI ---

script_path = Path(__file__).resolve()
script_dir = script_path.parent
project_root = script_dir.parent

# Dosya isimleri
okunacak_dosya_adi = "btcusdt_5m_50000.parquet"
yazilacak_dosya_adi = "btcusdt_5m_50000_islenmis.parquet"

# Tam yollar
okunacak_path = project_root / 'data' / okunacak_dosya_adi
yazilacak_path = project_root / 'data' / yazilacak_dosya_adi

print(f"Okunacak dosya yolu: {okunacak_path}")
print(f"Yazılacak dosya yolu: {yazilacak_path}")


# --- 2. PARQUET İŞLEME KISMI ---

if not okunacak_path.exists():
    print(f"HATA: Dosya bulunamadı! Lütfen yolu kontrol et: {okunacak_path}")
else:
    parquet_dosyasi = pq.ParquetFile(okunacak_path)
    
    writer = None 
    BATCH_SIZE = 10000

    print("İşlem başlıyor...")

    for batch in parquet_dosyasi.iter_batches(batch_size=BATCH_SIZE):
        df = batch.to_pandas()
        
        # --- ESKİ YAVAŞ YÖNTEM (İPTAL EDİLDİ) ---
        # for index, satir in df.iterrows(): ...
        # ----------------------------------------
        
        # --- YENİ HIZLI YÖNTEM (VECTORIZATION) ---
        # Tek satırda tüm hesaplamayı yapıyoruz.
        # Formül: ((Kapanış - Açılış) / Açılış) * 100
        
        df['open-close'] = ((df['close'] - df['open']) / df['open']) * 100
        
        # Not: Eğer açılış ve kapanış eşitse üst taraf 0 olur, sonuç otomatik 0 çıkar.
        # Ekstra if/else kontrolüne gerek yoktur.
        
        # -----------------------------------------
        
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