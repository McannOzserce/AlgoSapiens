# AlgoSapiens's first dataCollection file dataCollection.py 

# This will get datas on binance Api 

# In first version this collector collect only bitcoin's datas

import pandas as pd
from binance.client import Client
from pathlib import Path
import time
import math

def fetch_binance_data(total_candles, symbol, interval=Client.KLINE_INTERVAL_5MINUTE):
   
    # 1. API İstemcisini Başlat
    try:
        client = Client()
        client.ping()
        print("Binance API bağlantısı başarılı.")
    except Exception as e:
        print(f"API bağlantı hatası: {e}")
        return None

    # 2. Parametreleri Ayarla
    limit_per_request = 1000  
    num_requests = math.ceil(total_candles / limit_per_request)
    
    all_klines_data = []
    endTime = None  

    print(f"Başlıyor: {symbol} için {total_candles} adet {interval} mum çekilecek...")
    print(f"Toplam {num_requests} adet API isteği atılacak.")

    try:
        # 3. Veri Çekme Döngüsü
        for i in range(num_requests):
            klines = client.get_klines(
                symbol=symbol,
                interval=interval,
                limit=limit_per_request,
                endTime=endTime
            )
            all_klines_data = klines + all_klines_data
            endTime = klines[0][0]

            print(f"Talep {i + 1}/{num_requests} tamamlandı. {len(all_klines_data)} mum çekildi.")
            time.sleep(0.5) 

        print("Tüm veriler çekildi. DataFrame oluşturuluyor...")

        # 4. Pandas DataFrame'e Dönüştür
        columns = [
            'open_time', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
        ]
        
        df = pd.DataFrame(all_klines_data, columns=columns)

        # 5. Veri Temizleme ve Dönüştürme
        
        # --- GÜNCELLEME BURADA BAŞLIYOR ---
        
        # Sadece AlgoSapiens için bize lazım olacak ana sütunları seçelim
        # ÖNEMLİ GÜNCELLEME: 'volume' (BTC adedi) yerine 'quote_asset_volume' (USDT tutarı) alıyoruz.
        df = df[['open_time', 'open', 'high', 'low', 'close', 'quote_asset_volume']]
        
        # Gelecekteki kodun basit kalması için 'quote_asset_volume' adını 'volume' olarak değiştiriyoruz.
        # Artık 'volume' sütunumuz USDT (Dolar) hacmini temsil ediyor.
        df = df.rename(columns={'quote_asset_volume': 'volume'})

        # --- GÜNCELLEME BURADA BİTTİ ---
        
        # Zaman damgasını (milisan_iye) okunabilir 'datetime' formatına çevir
        df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        
        # Sayısal olması gereken sütunları sayıya (float/int) çevir
        # (Artık 'volume' sütunu, quote_asset_volume'ü temsil ettiği için bu kod tıkır tıkır çalışır)
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = pd.to_numeric(df[col])

        # Verinin en eskiden en yeniye doğru sıralandığından emin ol
        df = df.sort_values(by='open_time')
        
        # Mumların mükerrer (duplicate) olmadığından emin ol
        df = df.drop_duplicates(subset='open_time')

        print(f"DataFrame oluşturuldu. Toplam {len(df)} adet benzersiz mum.")
        
        # 6. Dosya Yolunu Belirle ve Kaydet
        script_dir = Path(__file__).resolve().parent
        data_dir = script_dir.parent / 'data'
        data_dir.mkdir(parents=True, exist_ok=True)
        file_path = data_dir / f'{symbol.lower()}_{interval}_{total_candles}.parquet'
        
        # 7. Parquet Olarak Kaydet
        df.to_parquet(file_path, index=False, engine='pyarrow')
        
        print(f"Başarılı! Veri şu yola kaydedildi: {file_path}")
        
        return df

    except Exception as e:
        print(f"Veri çekme veya kaydetme sırasında bir hata oluştu: {e}")
        return None



