# # Buatlah aplikasi manajemen buku dengan menggunakan list dan dictionary,
# # setiap buku terdiri dari (no_isbn, judul, pengarang, isihalaman, deskripsi, stok, booked).
# # Lalu ada list mahasiswa (nama, nim, nomerhp, alamat)
# # Lalu ada list peminjam (nim, no_isbn, tanggalpinjam, tanggal_kembali, status)

print("                                                                            ")
print("                           PERPUSTAKAAN ZAHRA KUSUMA                        ")
print("                                                                            ")
print("----------------------------------------------------------------------------")
print("Selamat datang di perpustakaan")
print("----------------------------------------------------------------------------")


buku_list = [
    {
        "no_isbn": "978-3-16-148410-0",
        "judul": "Belajar Python",
        "pengarang": "Andi",
        "isihalaman": "300",
        "deskripsi": "Buku untuk belajar pemrograman Python dari dasar hingga mahir",
        "stok": 10,
        "booked": 2
    },
    {
        "no_isbn": "978-0-12-345678-9",
        "judul": "Indahnya Surga",
        "pengarang": "Budi",
        "isihalaman": "450",
        "deskripsi": "Panduan lengkap untuk menjadi seorang Data Scientist",
        "stok": 5,
        "booked": 1
    },
    {
        "no_isbn": "978-1-234-56789-1",
        "judul": "Kumpulan Dongeng Nusantara",
        "pengarang": "Siti",
        "isihalaman": "200",
        "deskripsi": "Kumpulan cerita dongeng dari berbagai daerah di Nusantara",
        "stok": 8,
        "booked": 3
    },
    {
        "no_isbn": "978-3-16-148411-7",
        "judul": "Aljabar Linear",
        "pengarang": "Cahyo",
        "isihalaman": "320",
        "deskripsi": "Dasar-dasar machine learning untuk pemula",
        "stok": 7,
        "booked": 2
    },
    {
        "no_isbn": "978-1-234-56780-4",
        "judul": "Pemrograman Web dengan Django",
        "pengarang": "Eko",
        "isihalaman": "280",
        "deskripsi": "Panduan lengkap membangun aplikasi web dengan Django",
        "stok": 9,
        "booked": 4
    },
    {
        "no_isbn": "978-3-16-148412-4",
        "judul": "Deep Learning Illustrated",
        "pengarang": "Farah",
        "isihalaman": "350",
        "deskripsi": "Ilustrasi lengkap tentang deep learning",
        "stok": 5,
        "booked": 1
    },
    {
        "no_isbn": "978-0-12-345680-2",
        "judul": "Cybersecurity Essentials",
        "pengarang": "Gilang",
        "isihalaman": "400",
        "deskripsi": "Dasar-dasar keamanan siber untuk profesional",
        "stok": 4,
        "booked": 0
    }
]

def tampilkan_buku():
    print("\nDaftar Buku")
    print("----------------------------------------------------------------------------")
    nomor = 1
    for buku in buku_list:
        print(f"{nomor}.")
        print(f"   ISBN        : {buku['no_isbn']}")
        print(f"   Judul       : {buku['judul']}")
        print(f"   Pengarang   : {buku['pengarang']}")
        print(f"   Isi Halaman : {buku['isihalaman']}")
        print(f"   Deskripsi   : {buku['deskripsi']}")
        print(f"   Stok        : {buku['stok']}")
        print(f"   Booked      : {buku['booked']}")
        nomor += 1


mahasiswa_list = []

def tambah_mahasiswa_dan_peminjaman():
    print("\nData Mahasiswa yang meminjam ")
    print("----------------------------------------------------------------------------")
    nama =    input("Masukkan nama lengkap      : ")
    nim =     input("Masukkan NIM               : ")
    nomerHp = input("Masukkan Nomor Handphone   : ")
    alamat =  input("Masukkan alamat            : ")

    mahasiswa = {
        "nama"      : nama,
        "NIM"       : nim,
        "nomerHp"   : nomerHp,
        "alamat"    : alamat
    }
    mahasiswa_list.append(mahasiswa)
    print("Mahasiswa berhasil ditambahkan!")
    
    while True:
        tampilkan_buku()
        pilihan_buku = int(input("Pilih nomor buku yang ingin dipinjam: ")) - 1

        if 0 <= pilihan_buku < len(buku_list):
            buku = buku_list[pilihan_buku]
            if int(buku['stok']) > 0:
                tanggalpinjam =   input("Tanggal pinjam (YYYY-MM-DD) : ")
                tanggal_kembali = input("Tanggal kembali (YYYY-MM-DD): ")
                buku['stok'] = str(int(buku['stok']) - 1)
                buku['booked'] = str(int(buku['booked']) + 1)
                peminjam_list.append({
                    "nim"                   : mahasiswa["NIM"],
                    "no_isbn"               : buku['no_isbn'],
                    "tanggalpinjam"         : tanggalpinjam,
                    "tanggal_kembali"       : tanggal_kembali,
                    "status"                : "Dipinjam"
                })
                print("Buku berhasil dipinjam!")
            else:
                print("Buku sudah habis di pinjam.")
        else:
            print("Pilihan buku tidak valid.")
        
        lagi = input("Apakah Anda ingin meminjam buku lain? (y/n): ")
        if lagi.lower() != 'y':
            break

peminjam_list = []

def tampilkan_peminjam():
    print("\nDaftar Peminjam")
    print("----------------------------------------------------------------------------")
    if not peminjam_list:
        print("Belum ada peminjam yang terdaftar.")
    else:
        for peminjam in peminjam_list:
            print(f"NIM                   : {peminjam['nim']}")
            print(f"No ISBN               : {peminjam['no_isbn']}")
            print(f"Tanggal Pinjam        : {peminjam['tanggalpinjam']}")
            print(f"Tanggal Kembali       : {peminjam['tanggal_kembali']}")
            print(f"Status                : {peminjam['status']}\n")

while True:
    print("\nMenu Utama:")
    print("1. Tambah Mahasiswa dan Peminjaman Buku")
    print("2. Tampilkan Daftar Peminjam")
    print("3. Tampilkan Daftar Buku")
    print("4. Keluar")
    
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        tambah_mahasiswa_dan_peminjaman()
    elif pilihan == '2':
        tampilkan_peminjam()
    elif pilihan == '3':
        tampilkan_buku()
    elif pilihan == '4':
        print("----------------------------------------------------------------------------")
        print("Terima kasih telah menggunakan sistem perpustakaan.")
        break
    else:
        print("----------------------------------------------------------------------------")
        print("Pilihan tidak valid. Silakan coba lagi.")
