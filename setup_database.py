import sqlite3

print('memulai pembuatan database.....')

# membuat file latihan.db
koneksi = sqlite3.connect('latihan.db')
cursor = koneksi.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS transaksi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produk TEXT,
    harga INTEGER,
    tanggal DATE
    )''')

print('tabel transaksi berhasil dibuat!')

koneksi.commit()
koneksi.close()
