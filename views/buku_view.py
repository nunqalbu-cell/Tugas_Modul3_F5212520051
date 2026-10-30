import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("white")
ctk.set_default_color_theme("blue")

class BukuView(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistem Perpustakaan - Manajemen Data Buku")
        self.geometry("900x560")
        self.resizable(False, False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # FRAME KIRI: FORM INPUT & TOMBOL
        self.frame_left = ctk.CTkFrame(self, corner_radius=10)
        self.frame_left.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.lbl_title = ctk.CTkLabel(self.frame_left, text="Form Data Buku", font=ctk.CTkFont(size=18, weight="bold"))
        self.lbl_title.pack(pady=(15, 10), padx=10)

        self.lbl_judul = ctk.CTkLabel(self.frame_left, text="Judul Buku:", anchor="w")
        self.lbl_judul.pack(fill="x", padx=15, pady=(5, 0))
        self.entry_judul = ctk.CTkEntry(self.frame_left, placeholder_text="Masukkan Judul Buku")
        self.entry_judul.pack(fill="x", padx=15, pady=(0, 10))

        self.lbl_penulis = ctk.CTkLabel(self.frame_left, text="Penulis:", anchor="w")
        self.lbl_penulis.pack(fill="x", padx=15, pady=(5, 0))
        self.entry_penulis = ctk.CTkEntry(self.frame_left, placeholder_text="Masukkan Nama Penulis")
        self.entry_penulis.pack(fill="x", padx=15, pady=(0, 10))

        self.lbl_tahun = ctk.CTkLabel(self.frame_left, text="Tahun Terbit:", anchor="w")
        self.lbl_tahun.pack(fill="x", padx=15, pady=(5, 0))
        self.entry_tahun_terbit = ctk.CTkEntry(self.frame_left, placeholder_text="Contoh: 2024")
        self.entry_tahun_terbit.pack(fill="x", padx=15, pady=(0, 15))

        # TOMBOL OPERASI CRUD
        self.btn_simpan = ctk.CTkButton(
            self.frame_left, text="Simpan Data", fg_color="#27ae60", hover_color="#1e8449"
        )
        self.btn_simpan.pack(fill="x", padx=15, pady=4)

        self.btn_update = ctk.CTkButton(
            self.frame_left, text="Perbarui Data (Update)", fg_color="#1f538d", hover_color="#14375e"
        )
        self.btn_update.pack(fill="x", padx=15, pady=4)

        self.btn_delete = ctk.CTkButton(
            self.frame_left, text="Hapus Data (Delete)", fg_color="#c0392b", hover_color="#922b21"
        )
        self.btn_delete.pack(fill="x", padx=15, pady=4)

        # Tombol Logout
        self.btn_logout = ctk.CTkButton(
            self.frame_left, text="Logout", fg_color="#7f8c8d", hover_color="#707b7c"
        )
        self.btn_logout.pack(fill="x", padx=15, pady=(15, 5))

        # FRAME KANAN: TABEL DATA BUKU (BACKGROUND PUTIH)
        self.frame_right = ctk.CTkFrame(self, corner_radius=10, fg_color="white")
        self.frame_right.grid(row=0, column=1, padx=(0, 15), pady=15, sticky="nsew")

        # Judul Tabel dengan teks hitam
        self.lbl_table_title = ctk.CTkLabel(
            self.frame_right, 
            text="Daftar Koleksi Buku", 
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="black"
        )
        self.lbl_table_title.pack(pady=(15, 10), padx=10)

        # STYLE TABEL: Mengubah warna background isi tabel & teks menjadi putih & hitam
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Treeview", 
            background="white", 
            foreground="black", 
            fieldbackground="white", 
            rowheight=25
        )
        style.configure(
            "Treeview.Heading", 
            background="#1f538d", 
            foreground="white", 
            font=('Helvetica', 10, 'bold')
        )
        style.map(
            "Treeview", 
            background=[('selected', '#1f538d')],
            foreground=[('selected', 'white')]
        )

        columns = ("id_buku", "judul", "penulis", "tahun_terbit")
        self.tree = ttk.Treeview(self.frame_right, columns=columns, show="headings", height=14)

        self.tree.heading("id_buku", text="ID")
        self.tree.heading("judul", text="Judul Buku")
        self.tree.heading("penulis", text="Penulis")
        self.tree.heading("tahun_terbit", text="Tahun")

        self.tree.column("id_buku", width=50, anchor="center")
        self.tree.column("judul", width=200, anchor="w")
        self.tree.column("penulis", width=140, anchor="w")
        self.tree.column("tahun_terbit", width=80, anchor="center")

        self.tree.pack(fill="both", expand=True, padx=15, pady=(0, 15))