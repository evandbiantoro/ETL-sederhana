import sqlite3
# membuat data dummy
data_mentah = [
    ('Macbook Pro', 25000000, '2024-07-01'),
    ('Magic Keyboard', 1500000, '2023-11-12'),
    ('Speaker Bose', 1200000, '2020-12-12')
]
# menhubungkan ke databesenya
koneksi = sqlite3.connect('latihan.db')
cursor = koneksi.cursor()

print('Memasukan data...')

# tahap memanipulasi data
# disini nama produk di manipulasi menjadi huruf besar .upper()
for barang in data_mentah:
    nama_produk = barang[0].upper()
    harga = barang[1]
    tanggal = barang[2]

# menjalankan sintaks sql
    cursor.execute('''INSERT INTO transaksi (produk, harga, tanggal) VALUES (?,?,?)''',
                   (nama_produk, harga, tanggal))

koneksi.commit()
koneksi.close()
