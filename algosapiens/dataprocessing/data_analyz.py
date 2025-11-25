import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
from pathlib import Path

def calculate_real_body(okunacak_dosya_adi="data.parquet"):
    
    # 1. Dosya Yollarını Ayarla
    script_path = Path(__file__).resolve()
    script_dir = script_path.parent
    project_root = script_dir.parent
    
    # Çıktı dosyasının ismini otomatik üret (örn: dosya_islenmis.parquet)
    yazilacak_dosya_adi = okunacak_dosya_adi.replace(".parquet", "_1.parquet")

    okunacak_path = project_root / 'data' / okunacak_dosya_adi
    yazilacak_path = project_root / 'data' / yazilacak_dosya_adi

    print(f"Okunacak dosya yolu: {okunacak_path}")
    print(f"Yazılacak dosya yolu: {yazilacak_path}")

    # 2. Dosya Kontrolü
    if not okunacak_path.exists():
        print(f"HATA: Dosya bulunamadı! Lütfen yolu kontrol et: {okunacak_path}")
        return # Dosya yoksa fonksiyondan çık

    # 3. İşleme Başla
    parquet_dosyasi = pq.ParquetFile(okunacak_path)
    
    writer = None 
    BATCH_SIZE = 10000

    print("İşlem başlıyor...")

    for batch in parquet_dosyasi.iter_batches(batch_size=BATCH_SIZE):
        df = batch.to_pandas()
        
        # Hesaplama: (Kapanış - Açılış) / Açılış * 100 (5 basamak yuvarla)
        df['open-close'] = (((df['close'] - df['open']) / df['open']) * 100).round(5)
        
        yeni_table = pa.Table.from_pandas(df)
        
        # İlk turda writer'ı oluştur
        if writer is None:
            writer = pq.ParquetWriter(yazilacak_path, yeni_table.schema)

        writer.write_table(yeni_table)

    if writer:
        writer.close()

    print(f"İşlem tamamlandı! Kaydedilen yer: {yazilacak_path}")
