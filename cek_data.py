import sqlite3

koneksi = sqlite3.connect('latihan.db')
cursor = koneksi.cursor()

cursor.execute('''SELECT * FROM transaksi WHERE harga > 1000000''')

# mengambil data yg telah dieksekusi sql diatas dari database, lalu disimpan di hardisk
# lalu mengambil semua data sekaligus yg tersimpan di hardisk tadi dengan fetchall(), lalu disimpan di ram
hasil = cursor.fetchall()

# lalu loop hasil dan print
for baris in hasil:
    print(baris)

koneksi.close()
