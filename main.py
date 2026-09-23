print("=" * 50)
print("  SISTEM INFORMASI DATA DAN KEHADIRAN MAHASISWA  ")
print("=" * 50)

# Input interaktif dari terminal
nama_mahasiswa = input("Masukkan Nama Lengkap : ")
nim_mahasiswa  = input("Masukkan NIM          : ")
mata_kuliah    = input("Mata Kuliah           : ")
status_absen   = input("Status Kehadiran (Hadir/Izin/Sakit): ")

print("-" * 50)
print("              REKAP BUKTI PRESENSI                   ")
print("-" * 50)

# Format ringkasan data
print(f"Nama Lengkap  : {nama_mahasiswa.upper()}")
print(f"NIM           : {nim_mahasiswa}")
print(f"Mata Kuliah   : {mata_kuliah}")
print(f"Keterangan    : {status_absen.capitalize()}")

# Validasi status sederhana
if status_absen.lower() == "hadir":
    print("Status Sistem : Presensi berhasil tercatat tepat waktu.")
else:
    print("Status Sistem : Keterangan ketidakhadiran telah diajukan.")

print("=" * 50)