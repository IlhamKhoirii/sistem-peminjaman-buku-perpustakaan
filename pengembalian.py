class Pengembalian:
    @classmethod
    def kembalikan(cls, peminjaman_list, buku_list):
        id_buku = input("Masukkan ID Buku yang akan dikembalikan: ").strip()

        if not id_buku:
            print("ID Buku tidak boleh kosong. Silakan coba lagi.\n")
            return None

        # Mencari peminjaman berdasarkan ID Buku
        peminjaman = next((p for p in peminjaman_list if p.buku.id_buku == id_buku), None)

        if peminjaman:
            # Mengubah status buku menjadi tersedia
            peminjaman.buku.status = True
            
            # Menghapus peminjaman dari daftar peminjaman
            peminjaman_list.remove(peminjaman)

            print(f"Buku '{peminjaman.buku.judul}' berhasil dikembalikan.\n")
            return peminjaman
        else:
            print("Pengembalian gagal. Buku dengan ID tersebut tidak ditemukan dalam daftar peminjaman.\n")
            return None
