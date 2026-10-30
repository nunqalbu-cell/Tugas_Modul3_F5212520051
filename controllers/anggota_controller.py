import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding tombol Simpan
        self.view.btn_simpan.configure(command=self.simpan_data)

        # Memuat data awal pada tabel
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tree.get_children():
            self.view.tree.delete(item)

        data_anggota = self.model.get_all_anggota()
        for anggota in data_anggota:
            self.view.tree.insert("", "end", values=(
                anggota['id_anggota'],
                anggota['nama'],
                anggota['alamat']
            ))

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete("1.0", "end")

    def simpan_data(self):
        nama = self.view.entry_nama.get().strip()
        alamat = self.view.entry_alamat.get("1.0", "end-1c").strip()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_anggota(nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data anggota.")

    def run(self):
        self.view.mainloop()