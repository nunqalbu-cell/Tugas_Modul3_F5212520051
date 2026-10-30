import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")

class AnggotaView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Perpustakaan - Manajemen Data Anggota")
        self.geometry("900x520")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Frame Form Input (Kiri)
        self.frame_left = ctk.CTkFrame(self, corner_radius=10)
        self.frame_left.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.lbl_title = ctk.CTkLabel(self.frame_left, text="Form Data Anggota", font=ctk.CTkFont(size=18, weight="bold"))
        self.lbl_title.pack(pady=(15, 10), padx=10)

        self.lbl_nama = ctk.CTkLabel(self.frame_left, text="Nama Anggota:", anchor="w")
        self.lbl_nama.pack(fill="x", padx=15, pady=(5, 0))
        self.entry_nama = ctk.CTkEntry(self.frame_left, placeholder_text="Masukkan Nama Lengkap")
        self.entry_nama.pack(fill="x", padx=15, pady=(0, 10))

        self.lbl_alamat = ctk.CTkLabel(self.frame_left, text="Alamat:", anchor="w")
        self.lbl_alamat.pack(fill="x", padx=15, pady=(5, 0))
        self.entry_alamat = ctk.CTkTextbox(self.frame_left, height=120)
        self.entry_alamat.pack(fill="x", padx=15, pady=(0, 15))

        # Hanya menggunakan Tombol Simpan Data
        self.btn_simpan = ctk.CTkButton(
            self.frame_left, text="Simpan Data", fg_color="#27ae60", hover_color="#1e8449"
        )
        self.btn_simpan.pack(fill="x", padx=15, pady=10)

        # Frame Tabel (Kanan)
        self.frame_right = ctk.CTkFrame(self, corner_radius=10)
        self.frame_right.grid(row=0, column=1, padx=(0, 15), pady=15, sticky="nsew")

        self.lbl_table_title = ctk.CTkLabel(self.frame_right, text="Daftar Anggota Perpustakaan", font=ctk.CTkFont(size=18, weight="bold"))
        self.lbl_table_title.pack(pady=(15, 10), padx=10)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", rowheight=25)
        style.configure("Treeview.Heading", background="#1f538d", foreground="white", font=('Helvetica', 10, 'bold'))
        style.map("Treeview", background=[('selected', '#1f538d')])

        columns = ("id_anggota", "nama", "alamat")
        self.tree = ttk.Treeview(self.frame_right, columns=columns, show="headings", height=14)

        self.tree.heading("id_anggota", text="ID Anggota")
        self.tree.heading("nama", text="Nama Anggota")
        self.tree.heading("alamat", text="Alamat")

        self.tree.column("id_anggota", width=90, anchor="center")
        self.tree.column("nama", width=180, anchor="w")
        self.tree.column("alamat", width=230, anchor="w")

        self.tree.pack(fill="both", expand=True, padx=15, pady=(0, 15))

if __name__ == "__main__":
    app = AnggotaView()
    app.mainloop()