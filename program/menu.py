from program import helper as Helper, user as User, kursus as Kursus, voucher as Voucher

def MenuUtama():   
    pilihanKedua = "Profil" if User.SudahLogin() else "Login " 

    Helper.CetakHeader("PENDAFTARAN KURSUS - MENU UTAMA")   
    Helper.CetakList([
        "> 1. 📚 Kursus",
        "> 2. 👤 " + pilihanKedua,  
        "> 3. 📝 Panel Admin",
        "> 4. 🚪 Exit" 
    ])
    pilihan = Helper.Pilih()

    Helper.BersihkanLayar()
    
    if pilihan == 1:  
        MenuKursus()
    elif pilihan == 2: 
        if pilihanKedua == "Profil":
            MenuProfil()
        else: 
            MenuAutentikasi()
    elif pilihan == 3:
        MenuAdmin()
    elif pilihan == 4:  
        Helper.CetakHeader("👋 Sampai Jumpa", "-")
        exit()
    else:
        Helper.CetakHeader("⚠️\tERROR: Pilihan Invalid!", "-")
        MenuUtama()

def MenuAutentikasi(): 
    Helper.CetakHeader("MENU AUTENTIKASI - Login atau Registrasi")
    Helper.CetakList([
        "> 1. 👤 Login",
        "> 2. ⏏️  Registrasi Akun"
    ])

    pilihan = Helper.Pilih()

    Helper.BersihkanLayar()
    
    if pilihan == 1:
        MenuLogin()
    elif pilihan == 2:
        MenuRegistrasi()
    else:
        Helper.CetakHeader("⚠️\tERROR: Pilihan Invalid!", "-")
        MenuAutentikasi()

def MenuLogin(): 
    Helper.CetakHeader("LOGIN - Masukan Kredensial Anda") 

    nama = Helper.Pilih("Nama: ", False, False)
    password = Helper.Pilih("Password: ", False, False, True)

    Helper.BersihkanLayar()

    if User.Login(nama, password):
        Helper.CetakHeader("✅ Login Berhasil!", "-")
        MenuUtama()
    else:
        MenuLogin()

def MenuRegistrasi():
    Helper.CetakHeader("⏏️  REGISTRASI - Silahkan Daftar Akun Anda") 
    nama = Helper.Pilih("Nama: ", False, False) 
    pendidikan = Helper.Pilih("Tingkat Pendidikan: ", False, False)
    alamat = Helper.Pilih("Masukan Alamat: ", False, False)
    password = Helper.Pilih("Password: ", False, False, True)
    passwordUlang = Helper.Pilih("Ulangi Password: ", False, False, True)

    Helper.BersihkanLayar() 

    if User.Registrasi(nama, pendidikan, alamat, password, passwordUlang):
        MenuUtama()
    else: 
        MenuRegistrasi() 

def MenuProfil():
    Helper.CetakHeader("PROFIL USER")

    tipe = "Admin" if User.user["is_admin"] else "Pengguna"

    Helper.CetakList([
        "ID User:  " + str(User.user["id"]),
        "Nama:  " + User.user["nama"],
        "Tingkat Pendidikan:  " + User.user["pendidikan"],
        "Alamat:  " + User.user["alamat"],
        "Saldo: Rp. {:,}".format(User.user["saldo"]),
        "Tipe User: " + tipe 
    ])

    Helper.CetakList([
        "> 1. 📜 Ganti Nama", 
        "> 2. 📜 Ganti Password",
        "> 3. 📜 Ganti Pendidikan",
        "> 4. 📜 Ganti Alamat",
        "> 5. 💰 Top Up Saldo",
        "> 6. 🚪 Logout",
    ])

    pilihan = Helper.Pilih()
    Helper.BersihkanLayar()
    if pilihan == 1:
        MenuProfilGantiNama()
    elif pilihan == 2:
        MenuProfilGantiPassword()
    elif pilihan == 3:
        MenuProfilGantiPendidikan()
    elif pilihan == 4:
        MenuProfilGantiAlamat()
    elif pilihan == 5:
        MenuTopUpSaldo() 
    elif pilihan == 6:
        User.Logout()
        MenuUtama()
    else:
        Helper.CetakHeader("⚠️\tERROR - Pilihan Invalid", "-")
        MenuProfil()

def MenuProfilGantiNama():
    Helper.CetakHeader("GANTI NAMA")
    nama = Helper.Pilih("Masukan nama baru: ", False, False)
    Helper.BersihkanLayar()
    if User.GantiNama(nama):
        MenuProfil()
    else:
        MenuProfilGantiNama()

def MenuTopUpSaldo():
    Helper.CetakHeader("💰 TOP UP SALDO")
    pw = Helper.Pilih("Masukan Password Anda: ", False, False, True)
    saldo = Helper.Pilih("Masukan saldo: ", tips=False)

    Helper.BersihkanLayar()
    if User.TopUpSaldo(pw, saldo):
        MenuProfil()
    else:
        MenuTopUpSaldo()

def MenuProfilGantiPassword():
    Helper.CetakHeader("GANTI PASSWORD")
    pwLama = Helper.Pilih("Masukan password lama: ", False, False, True)
    pwBaru = Helper.Pilih("Masukan password baru: ", False, False, True)
    Helper.BersihkanLayar()
    if User.GantiPassword(pwLama, pwBaru):
        MenuProfil()
    else:
        MenuProfilGantiPassword()

def MenuProfilGantiPendidikan():
    Helper.CetakHeader("GANTI PENDIDIKAN")
    pendidikan = Helper.Pilih("Masukan tingkat pendidikan baru: ", False, False)
    Helper.BersihkanLayar()
    if User.GantiPendidikan(pendidikan):
        MenuProfil()
    else:
        MenuProfilGantiNama()

def MenuProfilGantiAlamat():
    Helper.CetakHeader("GANTI ALAMAT")
    alamat = Helper.Pilih("Masukan alamat baru: ", False, False)
    Helper.BersihkanLayar()
    if User.GantiAlamat(alamat):
        MenuProfil()
    else:
        MenuProfilGantiNama()

def MenuAdmin():
    if User.SudahLogin() is False: 
        Helper.CetakHeader("⚠️  ERROR - Hanya admin yang bisa mengakses panel ini", "-")
        MenuUtama()

    if User.user["is_admin"] != 1:
        Helper.CetakHeader("⚠️  ERROR - Hanya admin yang bisa mengakses panel ini", "-")
        MenuUtama()

    Helper.CetakHeader("MENU ADMIN")

    Helper.CetakList([
        "> 1. 📚 Tambah Kursus", 
        "> 2. 📚 Edit Kursus", 
        "> 3. 🎫 Tambah Voucher",  
        "> 4. 🎫 Edit Voucher",  
        "> 5. 🔙 Kembali ke Menu Utama"
    ])

    pilihan = Helper.Pilih()
    Helper.BersihkanLayar()

    if pilihan == 1:
        MenuAdminTambahKursus() 
    elif pilihan == 2:
        MenuAdminEditKursus()
    elif pilihan == 3:
        MenuAdminTambahVoucher() 
    elif pilihan == 4:
        MenuAdminEditVoucher()
    elif pilihan == 5:
        MenuUtama()
    else:  
        Helper.CetakHeader("⚠️\t ERROR: Pilihan Invalid!", "-")
        MenuKursus() 

def MenuAdminTambahKursus():
    Helper.CetakHeader("📚 Masukan Data Kursus Yang Baru")
    judul = Helper.Pilih("Judul: ", False, False)
    bidang = Helper.Pilih("Bidang: ", False, False)
    deskripsi = Helper.Pilih("Deskripsi: ", False, False)
    rating = Helper.Pilih("Rating (1 - 5): ", tips=False)
    harga = Helper.Pilih("Harga : Rp. ", tips=False)

    Helper.BersihkanLayar() 
    if Kursus.BuatKursus(judul, bidang, deskripsi, rating, harga):
        MenuAdmin()
    else: 
        MenuAdminTambahKursus() 

def MenuAdminEditKursus(kursus: dict | None = None):
    if kursus is None:
        Helper.CetakHeader("SEARCH KURSUS TERLEBIH DAHULU")
        id = Helper.Pilih("Masukan ID kursus: ", tips=False)
        kursus = Kursus.AmbilKursus(id)
        Helper.BersihkanLayar()
        if kursus is False:
            Helper.CetakHeader(f"⚠️\tERROR: Kursus Dengan Id-{id} tidak ditemukan", "-")
            MenuAdminEditKursus() 

    Helper.CetakHeader("EDIT KURSUS", "-")
    Helper.CetakList([
        "ID:  " + str(kursus["id"]),
        "Judul: " + kursus["judul"],
        "Bidang: " + kursus["bidang"], 
        "Harga: Rp. {:,}".format(kursus["harga"]),
        "Rating: " + "⭐" * kursus["rating"],
    ])

    Helper.CetakParagraph("Deskripsi: " + kursus["deskripsi"], 100)
    print("\n")
    Helper.CetakGaris()
    Helper.CetakList([
        "> 1. 📝 Ganti Judul",
        "> 2. 📝 Ganti Bidang",
        "> 3. 📝 Ganti Harga",
        "> 4. 📝 Ganti Rating",
        "> 5. 📝 Ganti Deskripsi",
        "> 6. ⛔ Hapus Kursus",
        "> 7. 🔙 Kembali ke Menu Admin",
    ])
    
    pilihan = Helper.Pilih(tips=False)
    Helper.BersihkanLayar()
    if pilihan == 1:
        MenuAdminEditKursusJudul(kursus) 
    elif pilihan == 2: 
        MenuAdminEditKursusBidang(kursus) 
    elif pilihan == 3: 
        MenuAdminEditKursusHarga(kursus) 
    elif pilihan == 4: 
        MenuAdminEditKursusRating(kursus)
    elif pilihan == 5: 
        MenuAdminEditKursusDeskripsi(kursus)  
    elif pilihan == 6: 
        Kursus.HapusKursus(kursus)
        MenuAdmin()
    elif pilihan == 7: 
        MenuAdmin()    
    else:
        Helper.CetakHeader("⚠️\tERROR - Pilihan Invalid", "-")
        MenuAdminEditKursus(kursus)

def MenuAdminEditKursusJudul(kursus: dict):
    Helper.CetakHeader("GANTI JUDUL KURSUS")
    judul = Helper.Pilih("Masukan judul baru: ", False, False)
    Helper.BersihkanLayar()
    if Kursus.GantiJudul(kursus, judul):
        MenuAdminEditKursus(kursus)
    else:
        MenuAdminEditKursusJudul(kursus)

def MenuAdminEditKursusBidang(kursus: dict):
    Helper.CetakHeader("GANTI BIDANG KURSUS")
    bidang = Helper.Pilih("Masukan bidang: ", False, False)
    Helper.BersihkanLayar()
    if Kursus.GantiBidang(kursus, bidang):
        MenuAdminEditKursus(kursus)
    else:
        MenuAdminEditKursusBidang(kursus)

def MenuAdminEditKursusHarga(kursus: dict):
    Helper.CetakHeader("GANTI HARGA KURSUS")
    harga = Helper.Pilih("Masukan harga baru: ", tips=False)
    Helper.BersihkanLayar()
    if Kursus.GantiHarga(kursus, harga):
        MenuAdminEditKursus(kursus)
    else:
        MenuAdminEditKursusHarga(kursus)

def MenuAdminEditKursusRating(kursus: dict):
    Helper.CetakHeader("GANTI RATING KURSUS")
    rating = Helper.Pilih("Masukan rating baru (1-5): ", tips=False)
    Helper.BersihkanLayar()
    if Kursus.GantiRating(kursus, rating):
        MenuAdminEditKursus(kursus)
    else:
        MenuAdminEditKursusRating(kursus)

def MenuAdminEditKursusDeskripsi(kursus: dict):
    Helper.CetakHeader("GANTI DESKRIPSI KURSUS")
    deskripsi = Helper.Pilih("Masukan deskripsi baru: ", False, False)
    Helper.BersihkanLayar()
    if Kursus.GantiDeskripsi(kursus, deskripsi):
        MenuAdminEditKursus(kursus)
    else:
        MenuAdminEditKursusDeskripsi(kursus)

def MenuAdminTambahVoucher(): 
    Helper.CetakHeader("🎫 Masukan Data Voucher Yang Baru")
    nama = Helper.Pilih("Nama: ", False, False)
    kode = Helper.Pilih("Kode: ", False, False)
    potongan = Helper.Pilih("Potongan (%): ", tips=False)
    sisa = Helper.Pilih("Sisa Penggunaan: ", tips=False) 

    Helper.BersihkanLayar() 
    if Voucher.BuatVoucher(nama, kode, potongan, sisa):
        MenuAdmin()
    else: 
        MenuAdminTambahVoucher() 

def MenuAdminEditVoucher(voucher: dict | None = None):
    if voucher is None:
        Helper.CetakHeader("SEARCH VOUCHER TERLEBIH DAHULU")
        kode = Helper.Pilih("Masukan kode voucher: ", False, False)
        voucher = Voucher.AmbilVoucherData(kode)
        Helper.BersihkanLayar()
        if voucher is False:
            Helper.CetakHeader(f"⚠️\tERROR: Voucher Dengan kode {kode} tidak ditemukan", "-")
            MenuAdminEditVoucher() 

    Helper.CetakHeader("EDIT VOUCHER", "-")
    Helper.CetakList([
        "Nama:  " + voucher["nama"],
        "Kode: " + voucher["kode"], 
        "Potongan: {}%".format(voucher["potongan"] * 100),
        "Sisa Penggunaan: {}x".format(voucher["sisa"]),
    ]) 

    Helper.CetakGaris()
    Helper.CetakList([
        "> 1. 📝 Ganti Nama",
        "> 2. 📝 Ganti Kode",
        "> 3. 📝 Ganti Potongan",
        "> 4. 📝 Ganti Sisa Penggunaan",
        "> 5. ⛔ Hapus Voucher",
        "> 6. 🔙 Kembali ke Menu Admin",
    ])
    
    pilihan = Helper.Pilih(tips=False)
    Helper.BersihkanLayar()
    if pilihan == 1:
        MenuAdminEditVoucherNama(voucher) 
    elif pilihan == 2: 
        MenuAdminEditVoucherKode(voucher) 
    elif pilihan == 3: 
        MenuAdminEditVoucherPotongan(voucher) 
    elif pilihan == 4: 
        MenuAdminEditVoucherSisa(voucher) 
    elif pilihan == 5: 
        Voucher.HapusVoucher(voucher)
        MenuAdmin()  
    elif pilihan == 6:  
        MenuAdmin()  
    else:
        Helper.CetakHeader("⚠️\tERROR - Pilihan Invalid", "-")
        MenuAdminEditVoucher(voucher)

def MenuAdminEditVoucherNama(voucher: dict):
    Helper.CetakHeader("GANTI NAMA VOUCHER")
    nama = Helper.Pilih("Masukan nama: ", False, False)
    Helper.BersihkanLayar()
    if Voucher.GantiNama(voucher, nama):
        MenuAdminEditVoucher(voucher)
    else:
        MenuAdminEditVoucherNama(voucher)

def MenuAdminEditVoucherKode(voucher: dict):
    Helper.CetakHeader("GANTI KODE VOUCHER")
    kode = Helper.Pilih("Masukan kode: ", False, False)
    Helper.BersihkanLayar()
    if Voucher.GantiKode(voucher, kode):
        MenuAdminEditVoucher(voucher)
    else:
        MenuAdminEditVoucherKode(voucher)

def MenuAdminEditVoucherPotongan(voucher: dict):
    Helper.CetakHeader("GANTI POTONGAN VOUCHER")
    potongan = Helper.Pilih("Masukan potongan baru (%): ", tips=False)
    Helper.BersihkanLayar()
    if Voucher.GantiPotongan(voucher, potongan):
        MenuAdminEditVoucher(voucher)
    else:
        MenuAdminEditVoucherPotongan(voucher)

def MenuAdminEditVoucherSisa(voucher: dict):
    Helper.CetakHeader("GANTI SISA PENGGUNAAN VOUCHER")
    sisa = Helper.Pilih("Masukan sisa: ", tips=False)
    Helper.BersihkanLayar()
    if Voucher.GantiSisa(voucher, sisa):
        MenuAdminEditVoucher(voucher)
    else:
        MenuAdminEditVoucherSisa(voucher)

def MenuKursus():
    Helper.CetakHeader("MENU KURSUS")

    Helper.CetakList([
        "> 1. 📚 List Semua Kursus",
        "> 2. 📚 List Kursus Berdasarkan Bidang",
        "> 3. 📚 List Kursus Berdasarkan Harga",
        "> 4. 📚 List Kursus Berdasarkan Rating",
        "> 5. 📓 Detail & Daftar Kursus",
        "> 6. 📓 Kursus Yang Saya Ikuti", 
    ])

    pilihan = Helper.Pilih()

    Helper.BersihkanLayar()

    if pilihan == 1:
        Kursus.CetakKursus()
        MenuKursus()
    elif pilihan == 2:
        MenuKursusBidang()
    elif pilihan == 3:
        MenuKursusHarga()
    elif pilihan == 4:
        MenuKursusRating()
    elif pilihan == 5:
        MenuKursusDetail() 
    elif pilihan == 6:
        MenuKursusYangUserIkuti()
    else:
        Helper.CetakHeader("⚠️\t ERROR: Pilihan Invalid!", "-")
        MenuKursus()

def MenuKursusBidang():
    Helper.CetakHeader("BIDANG KURSUS YANG TERSEDIA") 

    Helper.CetakList([
        "> 1. 💳 Bisnis",
        "> 2. 🤝 Humaniora",
        "> 3. 🚑 Kesehatan",
        "> 4. 🏫 Pendidikan",
        "> 5. 🔬 Sains",
        "> 6. 🎨 Seni",
    ])

    pilihan = Helper.Pilih()

    Helper.BersihkanLayar()

    if pilihan == 1:
        Kursus.CetakKursusMenurutBidang("Bisnis")
    elif pilihan == 2:
        Kursus.CetakKursusMenurutBidang("Humaniora")
    elif pilihan == 3:
        Kursus.CetakKursusMenurutBidang("Kesehatan")
    elif pilihan == 4:
        Kursus.CetakKursusMenurutBidang("Pendidikan")
    elif pilihan == 5:
        Kursus.CetakKursusMenurutBidang("Sains")
    elif pilihan == 6:
        Kursus.CetakKursusMenurutBidang("Seni")
    else:
        Helper.CetakHeader("⚠️\tERROR: Bidang Invalid", "-")
        MenuKursusBidang()
    
    MenuKursus()

def MenuKursusHarga():
    Helper.CetakHeader("SELECT RANGE HARGA") 

    Helper.CetakList([
        "> 1. Rp. 0 - Rp. 100,000",
        "> 2. Rp. 100,000 - Rp. 200,000",
        "> 3. Rp. 200,000 - Rp. 300,000",
        "> 4. Rp. 300,000+"
    ])

    pilihan = Helper.Pilih()
    Helper.BersihkanLayar()
    if pilihan == 1:
        Kursus.CetakKursusMenurutHarga(0, 100000)
    elif pilihan == 2:
        Kursus.CetakKursusMenurutHarga(100000, 200000)
    elif pilihan == 3:
        Kursus.CetakKursusMenurutHarga(200000, 300000)
    elif pilihan == 4:
        Kursus.CetakKursusMenurutHarga(300000)
    else:
        Helper.CetakHeader("⚠️\tERROR - Pilihan Invalid", "-")
        MenuKursusHarga()

    MenuKursus()

def MenuKursusRating():
    Helper.CetakHeader("SELECT RATING MINIMAL")

    Helper.CetakList([
        "> 1. ⭐⭐⭐⭐⭐",
        "> 2. ⭐⭐⭐⭐",
        "> 3. ⭐⭐⭐",
        "> 4. ⭐⭐",
        "> 5. ⭐"
    ])

    pilihan = Helper.Pilih()
    Helper.BersihkanLayar()
    if pilihan == 1:
        Kursus.CetakKursusMenurutRating(5)
    elif pilihan == 2:
        Kursus.CetakKursusMenurutRating(4)
    elif pilihan == 3:
        Kursus.CetakKursusMenurutRating(3)
    elif pilihan == 4:
        Kursus.CetakKursusMenurutRating(2)
    elif pilihan == 5:
        Kursus.CetakKursusMenurutRating(1)
    else:
        Helper.CetakHeader("⚠️\tERROR - Pilihan Invalid", "-")
        MenuKursusRating()

    MenuKursus()
        
def MenuKursusDetail(kursus: dict | None = None):

    if kursus is None:
        Helper.CetakHeader("SEARCH KURSUS TERLEBIH DAHULU")
        id = Helper.Pilih("Masukan ID kursus: ", tips=False)
        kursus = Kursus.AmbilKursus(id)
        Helper.BersihkanLayar()
        if kursus is False:
            Helper.CetakHeader(f"⚠️\tERROR: Kursus Dengan Id-{id} tidak ditemukan", "-")
            MenuKursusDetail() 
 
    Helper.CetakHeader("DETAIL KURSUS", "-")
    Helper.CetakList([
        "ID:  " + str(kursus["id"]),
        "Judul: " + kursus["judul"],
        "Bidang: " + kursus["bidang"], 
        "Harga: Rp. {:,}".format(kursus["harga"]),
        "Rating: " + "⭐" * kursus["rating"],
    ])

    Helper.CetakParagraph("Deskripsi: " + kursus["deskripsi"], 100)
    print("\n")
    Helper.CetakGaris()
    Helper.CetakList([
        "> 1. 📝 Daftar",
        "> 2. 🔙 Kembali ke Menu Kursus",
    ])
    
    pilihan = Helper.Pilih(tips=False)
    Helper.BersihkanLayar()
    if pilihan == 1:
        MenuKursusDaftar(kursus) 
    elif pilihan == 2: 
        MenuKursus()
    else:
        Helper.CetakHeader("⚠️\tERROR - Pilihan Invalid", "-")
        MenuKursusDetail(kursus)

def MenuKursusDaftar(kursus: dict):
    if User.SudahLogin() is False:
        Helper.CetakHeader("⚠️\tERROR - Anda Perlu Login Untuk Mendaftar", "-")
        MenuKursusDetail(kursus)

    Helper.CetakHeader("DAFTAR KURSUS", "-")
    Helper.CetakList([
        "ID:  " + str(kursus["id"]),
        "Judul: " + kursus["judul"],
        "Bidang: " + kursus["bidang"], 
        "Harga: Rp. {:,}".format(kursus["harga"]),
        "Apakah anda yakin ingin mendaftar di kursus ini?"
    ])  
    Helper.CetakList([
        "> 1. ✅ Ya",
        "> 2. 🎫 Ya, Gunakan Voucher",
        "> 3. 🔙 Tidak",
    ])

    pilihan = Helper.Pilih(tips=False)
    Helper.BersihkanLayar()
    if pilihan == 1: 
        Kursus.DaftarKursus(kursus) 
        MenuKursusDetail(kursus) 
    elif pilihan == 2:
        MenuGunakanVoucher(kursus)
    elif pilihan == 3:
        MenuKursusDetail(kursus)
    else:
        Helper.CetakHeader("⚠️\tERROR - Pilihan Invalid", "-")
        MenuKursusDaftar(kursus)

def MenuKursusYangUserIkuti():
    if User.SudahLogin() is False:
        Helper.CetakHeader("⚠️\tERROR - Anda Perlu Login Untuk Melihat Ini", "-")
        MenuKursus()

    Kursus.CetakKursusYangDiikuti()
    Helper.CetakGaris()
    Helper.CetakList([ 
        "> 1. 🔙 Kembali ke Menu Kursus",
    ])

    pilihan = Helper.Pilih()
    Helper.BersihkanLayar()
    MenuKursus()

def MenuGunakanVoucher(kursus: dict):
    Helper.CetakHeader("🎫 MASUKAN KODE VOUCHER")    
    kode = Helper.Pilih("Kode: ", False, False) 

    Helper.BersihkanLayar()

    voucher = Voucher.AmbilVoucher(kode)

    if voucher: 
        Helper.BersihkanLayar()
        MenuGunakanVoucherKonfirmasi(kursus, voucher)
    else:
        MenuGunakanVoucher(kursus) 

def MenuGunakanVoucherKonfirmasi(kursus: dict, voucher: dict):
    potongan = Voucher.HitungPotongan(voucher, kursus["harga"])

    Helper.CetakHeader("🎫 KONFIRMASI PENGGUNAAN VOUCHER", "-")
    Helper.CetakList([
        "Kursus: " + kursus["judul"], 
        "Voucher: " + voucher["nama"],
        "Harga Asli: Rp. {:,}".format(kursus["harga"]), 
        "Potongan: {}%".format(voucher["potongan"] * 100) ,
        "Potongan Harga: Rp. {:,}".format(potongan),
        "Total Harga: Rp. {:,}".format(kursus["harga"] - potongan),
        "Apakah anda yakin?"
    ])
    Helper.CetakList([ 
        "> 1. ✅ Ya",
        "> 2. 🔙 Tidak",
    ])

    pilihan = Helper.Pilih()
    Helper.BersihkanLayar()
    if pilihan == 1:
        Voucher.GunakanVoucher(voucher)
        Kursus.DaftarKursus(kursus, potongan)  
        MenuKursusDetail(kursus)
    elif pilihan == 2:
        MenuKursusDaftar(kursus)
    else:
        Helper.CetakHeader("⚠️\tERROR - Pilihan Invalid", "-")
        MenuGunakanVoucherKonfirmasi(kursus, voucher)