import requests
import time
import sqlite3
from datetime import datetime


while True:
    try:
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,idr'
        # ambil/dapatkan urlnya
        response = requests.get(url)
        # tunjukan statusnya apakah error
        # response.raise_for_status()
        # ubah text di yg ada di urlnya menjadi json/dictionary
        data = response.json()

        # ambil data yg harga bitcoin usd dan idr
        harga_usd = data['bitcoin']['usd']
        harga_idr = data['bitcoin']['idr']

        # proses memasukan data ke database
        koneksi = sqlite3.connect('latihan.db')
        cursor = koneksi.cursor()
        # masukan data ke table harga_bitcoin
        cursor.execute('''INSERT INTO harga_bitcoin (harga_usd, harga_idr) VALUES(?,?)''',
                       (harga_usd, harga_idr))

        koneksi.commit()
        koneksi.close()
        print('data berhasil disimpan')

        current_time = datetime.now().strftime('%H:%M:%S')
        print(
            f'[waktu saat ini {current_time}] harga saat ini: ${harga_usd} / Rp.{harga_idr}')

    except Exception as e:
        print(f'terjadi error: {e}')

    print('tunggu 60 detik....')
    time.sleep(60)
