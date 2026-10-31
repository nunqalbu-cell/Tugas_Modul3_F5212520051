# Sistem Informasi Perpustakaan (MVC Desktop App)

Aplikasi manajemen perpustakaan berbasis Python CustomTkinter dengan pola arsitektur MVC dan database MySQL.

## 📁 Struktur Direktori Proyek
- `config/`: Konfigurasi koneksi MySQL.
- `controllers/`: Logika alur aplikasi (Auth, Buku, Anggota).
- `models/`: Kueri database MySQL (User, Buku, Anggota).
- `views/`: Antarmuka GUI CustomTkinter.
- `tests/`: Unit testing dengan pytest.
- `main.py`: Titik masuk utama aplikasi.

## 🚀 Cara Menjalankan Aplikasi
1. Pastikan Laragon (MySQL) dalam status **Started**.
2. Jalankan perintah terminal:
   ```bash
   python main.py