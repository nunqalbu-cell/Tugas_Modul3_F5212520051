from models.buku_model import BukuModel
from models.anggota_model import AnggotaModel

# === PENGUJIAN BUKU MODEL ===
print("=== PENGUJIAN BUKU MODEL ===")
model_buku = BukuModel()

# 1. Create Buku
print("\n[+] Menambahkan data buku...")
model_buku.create_buku("Gadis Kretek", "Ratih Kumala", 2012)

# 2. Update Buku (ID: 6)
print("\n[*] Mengubah data buku ID 6...")
model_buku.update_buku(6, "Hujan", "Tere Liye", 2016)

# 3. Delete Buku (ID: 9 - sesuaikan dengan ID di DB Anda jika ada)
print("\n[-] Menghapus data buku ID 9...")
model_buku.delete_buku(9)

# 4. Read Buku
print("\n=== Daftar Buku Terkini ===")
for buku in model_buku.get_all_buku():
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")

# === PENGUJIAN ANGGOTA MODEL ===
print("\n=== PENGUJIAN ANGGOTA MODEL ===")
model_anggota = AnggotaModel()

# 1. Create Anggota
print("\n[+] Menambahkan data anggota...")
model_anggota.create_anggota("Nun Qalbu Ain", "Palu")

# 2. Read Anggota
print("\n=== Daftar Anggota Terkini ===")
for anggota in model_anggota.get_all_anggota():
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")