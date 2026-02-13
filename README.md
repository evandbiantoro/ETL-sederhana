# ETL sederhana

ini merupakan project latihan pertama membangun ETL untuk mengambil data harga bitcoin secara real-time

## Tech Stack
- Python 3.10
- SQLite
- Pandas
- time
- datetime

## Cara Menjalankan
1. Jalankan `setup_tabel_crypto.py` untuk membuat database dan tabel.
2. Jalankan `auto_ingest.py` untuk menjalankan bot otomatis (per menit).
3. Jalankan `cek_data_bitcoin.py` untuk melihat data sudah tersimpan di tabel.
4. Jalankan `export_data.py` untuk export data menjadi CSV.
