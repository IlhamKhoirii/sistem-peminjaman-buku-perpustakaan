class Perpustakaan:
    buku_list = []
    anggota_list = []
    peminjaman_list = []

    def __init__(self):
        pass

    @classmethod
    def menu(cls):
        print("Selamat datang di Sistem Manajemen Perpustakaan!")
        print('''
        1. Tambah Buku Baru
        2. Lihat Semua Buku
        3. Cari Buku berdasarkan ID

        4. Tambah Anggota Baru
        5. Lihat Semua Anggota
        6. Cari Anggota berdasarkan ID

        7. Pinjam Buku
        8. Lihat Semua Peminjaman
        9. Keluar
        ''')

        while True:
            try:
                pilihan = int(input("Silakan pilih menu (1-9): "))
                print()
                if pilihan == 1:
                    cls.tambah_buku()

                elif pilihan == 2:
                    cls.lihat_buku()

                elif pilihan == 3:
                    cls.cari_buku()

                elif pilihan == 4:
                    cls.tambah_anggota()

                elif pilihan == 5:
                    cls.lihat_anggota()

                elif pilihan == 6:
                    cls.cari_anggota()

                elif pilihan == 7:
                    cls.pinjam_buku()

                elif pilihan == 8:
                    cls.lihat_peminjaman()

                elif pilihan == 9:
                    print("Terima kasih telah menggunakan sistem kami. Sampai jumpa!")
                    break

                else:
                    print("Masukkan angka yang valid!\n")
            except ValueError:
                print("Input salah. Masukkan angka yang benar!\n")

    # Metode Buku
    @classmethod
    def tambah_buku(cls):
        from buku import Buku
        buku = Buku.tambah()
        cls.buku_list.append(buku)

    @classmethod
    def lihat_buku(cls):
        from buku import Buku
        Buku.lihat(cls.buku_list)

    @classmethod
    def cari_buku(cls):
        from buku import Buku
        Buku.cari(cls.buku_list)

    # Metode Anggota
    @classmethod
    def tambah_anggota(cls):
        from anggota import Anggota
        anggota = Anggota.tambah()
        cls.anggota_list.append(anggota)

    @classmethod
    def lihat_anggota(cls):
        from anggota import Anggota
        Anggota.lihat(cls.anggota_list)

    @classmethod
    def cari_anggota(cls):
        from anggota import Anggota
        Anggota.cari(cls.anggota_list)

    # Metode Peminjaman
    @classmethod
    def pinjam_buku(cls):
        from peminjaman import Peminjaman
        peminjaman = Peminjaman.pinjam(cls.buku_list, cls.anggota_list)
        if peminjaman:
            cls.peminjaman_list.append(peminjaman)

    @classmethod
    def lihat_peminjaman(cls):
        from peminjaman import Peminjaman
        Peminjaman.lihat(cls.peminjaman_list)
