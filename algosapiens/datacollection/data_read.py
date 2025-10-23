import pandas as pd
from pathlib import Path

# --- YENİ SATIR ---
# Pandas'a bilimsel gösterim (e+06 gibi) kullanmamasını söylüyoruz.
# Tüm float (kayan noktalı) sayıları 2 ondalık basamakla göster diyoruz.
pd.set_option('display.float_format', lambda x: '%.2f' % x)
# ------------------

def load_data(file_name="btcusdt_5m_50000.parquet"):
    """
    Ana dizindeki 'data' klasöründen belirtilen Parquet dosyasını okur
    ve bir Pandas DataFrame olarak döndürür.
    
    Bu script'in '/datacollection' klasörü içinde olduğunu varsayar.
    """
    
    try:
        # 1. Dosya Yolunu Belirle
        script_path = Path(__file__).resolve()
        script_dir = script_path.parent
        project_root = script_dir.parent
        file_path = project_root / 'data' / file_name
        
        # 2. Dosyanın var olup olmadığını kontrol et
        if not file_path.exists():
            print(f"Hata: Dosya bulunamadı! -> {file_path}")
            print("Lütfen 'data' klasörünün ana dizinde olduğundan emin olun.")
            return None
            
        print(f"Veri okunuyor: {file_path}")
        
        # 3. Parquet Dosyasını Oku
        df = pd.read_parquet(file_path)
        
        print("Veri başarıyla hafızaya yüklendi.")
        return df
        
    except Exception as e:
        print(f"Dosyayı okurken bir hata oluştu: {e}")
        return None

# Bu script'i doğrudan çalıştırırsan, aşağıdaki kod tetiklenir
if __name__ == "__main__":
    
    # 1. Veriyi yükle
    data_frame = load_data()
    
    # 2. Verinin yüklendiğini kontrol et
    if data_frame is not None:
        
        # 3. İlk 5 satırı göster
        print("\n--- Verinin İlk 5 Satırı (head) ---")
        print(data_frame.head())
        
        # 4. Veri hakkında bilgi al
        print("\n--- Veri Çerçevesi Bilgisi (info) ---")
        data_frame.info()
        
        # 5. Son 5 satırı göster
        print("\n--- Verinin Son 5 Satırı (tail) ---")
        print(data_frame.tail())