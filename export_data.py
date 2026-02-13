import sqlite3
import pandas as pd

print('membaca data dari database....')

koneksi = sqlite3.connect('latihan.db')

df = pd.read_sql_query('SELECT * FROM harga_bitcoin', koneksi)

koneksi.close()

print(f'berhasil mengambil {len(df)} baris data')
print('5 data terkahir:')
print(df.tail())

namaFile = 'laporan_bitcoin.csv'
df.to_csv(namaFile, index=False)

print(f'\nSukses File {namaFile} telah dibuat')
