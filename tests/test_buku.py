from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True
    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()
    # Memverifikasi apakah perintah commit dipanggil
    model.conn.commit.assert_called_once()

def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi koneksi database
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Menyiapkan data tiruan (mock data)
    data_dummy = [
        {"id_buku": 1, "judul": "Pemrograman Python", "penulis": "Ahmad", "tahun_terbit": 2023},
        {"id_buku": 2, "judul": "Rekayasa Perangkat Lunak", "penulis": "Nun Qalbu", "tahun_terbit": 2024}
    ]
    mock_cursor.fetchall.return_value = data_dummy

    # Eksekusi fungsi get_all_buku
    hasil = model.get_all_buku()

    # Verifikasi pengujian
    assert hasil == data_dummy
    assert len(hasil) == 2
    mock_cursor.execute.assert_called_once_with("SELECT * FROM buku")
    mock_cursor.fetchall.assert_called_once()