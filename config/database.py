import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""  # Password default Laragon biasanya kosong
        self.database = "perpustakaan"
        self.conn = None

    def get_connection(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conn.is_connected():
                return self.conn
        except Error as e:
            print(f"Koneksi ke database gagal: {e}")
            return None