import sqlite3

koneksi = sqlite3.connect('latihan.db')
cursor = koneksi.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS harga_bitcoin(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   waktu_ambil TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                   harga_usd REAL,
                   harga_idr REAL
               )
               ''')

koneksi.commit()
koneksi.close()
