import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()
        self.selected_id_buku = None

        # Menampilkan role pengguna pada judul window
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding Tombol dan Event
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)
        self.view.btn_logout.configure(command=self.logout_action)  # Tugas 3
        self.view.tree.bind("<<TreeviewSelect>>", self.pilih_data)

        # TUGAS 2: Mengunci seluruh tombol manipulasi data jika role bukan admin
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.btn_update.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.btn_delete.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")

            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun_terbit.configure(state="disabled")

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tree.get_children():
            self.view.tree.delete(item)

        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tree.insert("", "end", values=(
                buku['id_buku'],
                buku['judul'],
                buku['penulis'],
                buku['tahun_terbit']
            ))

    def bersihkan_form(self):
        if self.user_role == "admin":
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun_terbit.delete(0, 'end')
        self.selected_id_buku = None

    def pilih_data(self, event):
        selected_item = self.view.tree.selection()
        if selected_item:
            item_data = self.view.tree.item(selected_item[0])['values']
            self.selected_id_buku = item_data[0]

            if self.user_role == "admin":
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_judul.insert(0, item_data[1])

                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_penulis.insert(0, item_data[2])

                self.view.entry_tahun_terbit.delete(0, 'end')
                self.view.entry_tahun_terbit.insert(0, str(item_data[3]))

    def simpan_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun_terbit.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data buku.")

    def perbarui_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk memperbarui data!")
            return

        if not self.selected_id_buku:
            messagebox.showwarning("Peringatan", "Pilih baris data buku yang ingin diperbarui dari tabel!")
            return

        judul = self.view.entry_judul.get().strip()
        penulis = self.view.entry_penulis.get().strip()
        tahun = self.view.entry_tahun_terbit.get().strip()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_buku(self.selected_id_buku, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data buku.")

    def hapus_data(self):
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        if not self.selected_id_buku:
            messagebox.showwarning("Peringatan", "Pilih baris data buku yang ingin dihapus dari tabel!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data buku ini?")
        if konfirmasi:
            if self.model.delete_buku(self.selected_id_buku):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data buku.")

    # TUGAS 3: Fungsi Logout
    def logout_action(self):
        self.view.destroy()
        from controllers.auth_controller import AuthController
        app_auth = AuthController()
        app_auth.run()

    def run(self):
        self.view.mainloop()