# TUGAS BESAR TST

## Fashion E-Commerce

API Usage:
- Bukalapak API (Nadya 18217020)
- Pengiriman Logistik API (Vincent 18217041)

Created by:
- David Petra Natanael - 18217011
- Vincent - 18217042

### Deskripsi Aplikasi
Aplikasi merupakan sebuah *e-commerce* sederhana dimana pengguna dapat memilih barang untuk dibeli dan dapat memilih kurir pengiriman.
Kategori barang yang tersedia yaitu tas, sandal, dan kaos.

Pengguna juga dapat melakukan *tracking* ID pengiriman pada aplikasi.

### Cara Akses
```http://52.23.248.58/```

atau

```http://52.23.248.58/index.html```

### Cara Penggunaan Aplikasi
1. Mengisi data diri pada form order
2. Memilih barang yang ingin dibeli
3. Mengisi kota asal dan tujuan
4. Menekan tombol Calculate untuk melihat harga ongkir
5. Memesan Order
6. Mengkonfirmasi Order
7. (optional) Mengecek tracking ID

### Dokumentasi API
| Method | Deskripsi | Link |
|--------|:---------:|------|
|GET     | Menampilkan nama dan harga tas|http://52.23.248.58:8080/tas
|GET     | Menampilkan nama dan harga kaos|http://52.23.248.58:8080/kaos
|GET     | Menampilkan nama dan harga sandal|http://52.23.248.58:8080/sandal
|GET     | Menampilkan nama kota | http://52.23.248.58:8000/getcity
|GET     | Menampilkan seluruh keterangan pengiriman dari order yang telah dibuat | http://3.92.50.97:4040/api/order
|POST    | Menambahkan keterangan pengiriman dari order pelanggan ke database | http://3.92.50.97:4040/api/order
|POST    | Menghitung total ongkos kirim berdasarkan kota asal dan tujuan yang dimasukan oleh pengguna | http://3.92.50.97:4040/api/cost



