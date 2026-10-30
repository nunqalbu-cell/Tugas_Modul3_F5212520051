from config.database import Database

class BukuModel:
    def __init__(self):
        db = Database()
        self.conn = db.get_connection()

    def get_all_buku(self):
        try:
            if self.conn:
                cursor = self.conn.cursor(dictionary=True)
                cursor.execute("SELECT * FROM buku")
                return cursor.fetchall()
        except Exception as e:
            print(f"Eror get_all_buku: {e}")
        return []

    def create_buku(self, judul, penulis, tahun_terbit):
        try:
            if self.conn:
                cursor = self.conn.cursor()
                query = "INSERT INTO buku (judul, penulis, tahun_terbit) VALUES (%s, %s, %s)"
                cursor.execute(query, (judul, penulis, tahun_terbit))
                self.conn.commit()
                return True
        except Exception as e:
            print(f"Eror create_buku: {e}")
        return False

    def update_buku(self, id_buku, judul, penulis, tahun_terbit):
        try:
            if self.conn:
                cursor = self.conn.cursor()
                query = "UPDATE buku SET judul=%s, penulis=%s, tahun_terbit=%s WHERE id_buku=%s"
                cursor.execute(query, (judul, penulis, tahun_terbit, id_buku))
                self.conn.commit()
                return True
        except Exception as e:
            print(f"Eror update_buku: {e}")
        return False

    def delete_buku(self, id_buku):
        try:
            if self.conn:
                cursor = self.conn.cursor()

                # 1. Hapus riwayat transaksi di tabel peminjaman terlebih dahulu
                query_peminjaman = "DELETE FROM peminjaman WHERE id_buku = %s"
                cursor.execute(query_peminjaman, (id_buku,))

                # 2. Hapus data dari tabel buku
                query_buku = "DELETE FROM buku WHERE id_buku = %s"
                cursor.execute(query_buku, (id_buku,))

                self.conn.commit()
                return True
        except Exception as e:
            print(f"Eror delete_buku: {e}")
            if self.conn:
                self.conn.rollback()
        return False