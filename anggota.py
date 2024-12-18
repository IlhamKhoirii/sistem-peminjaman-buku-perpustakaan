class Anggota:
    def __init__(self, id_anggota, nama, alamat):
        self.id_anggota = id_anggota
        self.nama = nama
        self.alamat = alamat

    @classmethod
    def tambah(cls):
        id_anggota = input("Masukkan ID Anggota: ")
        nama = input("Masukkan Nama: ")
        alamat = input("Masukkan Alamat: ")
        return cls(id_anggota, nama, alamat)

    @classmethod
    def lihat(cls, anggota_list):
        if not anggota_list:
            print("Belum ada anggota di sistem.\n")
        else:
            for anggota in anggota_list:
                print(f"ID: {anggota.id_anggota}, Nama: {anggota.nama}, Alamat: {anggota.alamat}")

    @classmethod
    def cari(cls, anggota_list):
        id_anggota = input("Masukkan ID Anggota yang dicari: ")
        for anggota in anggota_list:
            if anggota.id_anggota == id_anggota:
                print(f"Nama: {anggota.nama}, Alamat: {anggota.alamat}")
                return
        print("Anggota tidak ditemukan.\n")
