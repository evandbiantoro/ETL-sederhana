import sqlite3

koneksi = sqlite3.connect('latihan.db')
cursor = koneksi.cursor()

cursor.execute(
    '''SELECT id, waktu_ambil, harga_usd, harga_idr FROM harga_bitcoin ORDER BY waktu_ambil DESC''')

for baris_data in cursor:
    print(baris_data)

koneksi.close()
