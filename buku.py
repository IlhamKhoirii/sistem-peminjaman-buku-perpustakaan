class Buku:
    def __init__(self, id_buku, judul, penulis, penerbit):
        self.id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.status = True  # True: Tersedia, False: Dipinjam

    @classmethod
    def tambah(cls):
        id_buku = input("Masukkan ID Buku: ")
        judul = input("Masukkan Judul Buku: ")
        penulis = input("Masukkan Penulis: ")
        penerbit = input("Masukkan Penerbit: ")
        return cls(id_buku, judul, penulis, penerbit)

    @classmethod
    def lihat(cls, buku_list):
        if not buku_list:
            print("Belum ada buku di sistem.\n")
        else:
            for buku in buku_list:
                status = "Tersedia" if buku.status else "Dipinjam"
                print(f"ID: {buku.id_buku}, Judul: {buku.judul}, Status: {status}")

    @classmethod
    def cari(cls, buku_list):
        id_buku = input("Masukkan ID Buku yang dicari: ")
        for buku in buku_list:
            if buku.id_buku == id_buku:
                print(f"Judul: {buku.judul}, Penulis: {buku.penulis}, Status: {'Tersedia' if buku.status else 'Dipinjam'}")
                return
        print("Buku tidak ditemukan.\n")