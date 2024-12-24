class Peminjaman:
    def __init__(self, buku, anggota):
        self.buku = buku
        self.anggota = anggota

    @classmethod
    def pinjam(cls, buku_list, anggota_list):
        id_buku = input("Masukkan ID Buku yang ingin dipinjam: ")
        buku = next((b for b in buku_list if b.id_buku == id_buku and b.status), None)

        id_anggota = input("Masukkan ID Anggota: ")
        anggota = next((a for a in anggota_list if a.id_anggota == id_anggota), None)

        if buku and anggota:
            buku.status = False  # Update status buku
            print("Buku berhasil dipinjam!\n")
            return cls(buku, anggota)
        else:
            print("Peminjaman gagal. Pastikan ID benar dan buku tersedia.\n")
            return None

    @classmethod
    def lihat(cls, peminjaman_list):
        if not peminjaman_list:
            print("Belum ada peminjaman.\n")
        else:
            for p in peminjaman_list:
                print(f"Buku: {p.buku.judul}, Peminjam: {p.anggota.nama}")