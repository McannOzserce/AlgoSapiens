# AlgoSapiens - Data Loading Utility
import pandas as pd
from pathlib import Path

# --- Configuration ---
# Virgülden sonra 5 basamak göster
pd.set_option('display.float_format', lambda x: '%.5f' % x)
# ---------------------

def load_data(file_name="data_1.parquet", verbose=True):
    """
    Veriyi okur ve verbose=True ise ekrana rapor basar.
    """
    try:
        # 1. Dosya Yolunu Bul
        script_path = Path(__file__).resolve()
        script_dir = script_path.parent
        project_root = script_dir.parent
        file_path = project_root / 'data' / file_name
        
        # 2. Dosya Kontrolü
        if not file_path.exists():
            print(f"HATA: Dosya bulunamadı! -> {file_path}")
            return None
            
        print(f"Veri okunuyor: {file_path}")
        
        # 3. Dosyayı Oku
        df = pd.read_parquet(file_path)
        print("Veri hafızaya yüklendi.")
        
        # --- İŞTE İSTEDİĞİN KISIM ---
        # Eğer verbose True ise (varsayılan), bilgileri burada basar.
        # Main dosyasında print yazmana gerek kalmaz.
        if verbose:
            print("\n" + "="*40)
            print(" VERİ ÖNİZLEMESİ (İLK 5 SATIR) ")
            print("="*40)
            print(df.head())
            
            print("\n" + "="*40)
            print(" SÜTUN VE TİP BİLGİLERİ ")
            print("="*40)
            df.info()
            
            print("\n" + "="*40)
            print(" SON 5 SATIR ")
            print("="*40)
            print(df.tail())
            print("\n")
        # ----------------------------
        
        return df
        
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None

# Bu blok sadece dosyayı tek başına test edersen çalışır
if __name__ == "__main__":
    load_data()