daftar_nama = []

while True:
    print("\n=== MENU ===")
    print("1. Tambah nama")
    print("2. Hapus nama")
    print("3. Tampilkan semua nama")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        daftar_nama.append(nama)
        print("Nama berhasil ditambahkan.")

    elif pilihan == "2":
        nama = input("Masukkan nama yang ingin dihapus: ")
        if nama in daftar_nama:
            daftar_nama.remove(nama)
            print("Nama berhasil dihapus.")
        else:
            print("Nama tidak ditemukan.")

    elif pilihan == "3":
        if len(daftar_nama) == 0:
            print("Belum ada nama yang tersimpan.")
        else:
            print("\nDaftar Nama:")
            for n in daftar_nama:
                print("- " + n)

    elif pilihan == "4":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")
