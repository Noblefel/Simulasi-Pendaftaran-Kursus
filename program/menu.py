from program import helper as Helper, user as User, kursus as Kursus, voucher as Voucher

def MenuUtama():   
    pilihanKedua = "Profil" if User.SudahLogin() else "Login " 

    Helper.CetakHeader("PENDAFTARAN KURSUS - MENU UTAMA")   
    Helper.CetakList([
        "> 1. 📚 Kursus",
        "> 2. 👤 " + pilihanKedua,  
        "> 3. 🚪 Exit" 
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
    password = Helper.Pilih("Password: ", False, False)

    Helper.BersihkanLayar()

    if User.Login(nama, password):
        Helper.CetakHeader("✅ Login Berhasil!", "-")
        MenuUtama()
    else:
        MenuLogin()

def MenuRegistrasi():
    Helper.CetakHeader("⏏️ REGISTRASI - Silahkan Daftar Akun Anda") 
    nama = Helper.Pilih("Nama: ", False, False) 
    password = Helper.Pilih("Password: ", False, False)
    passwordUlang = Helper.Pilih("Ulangi Password: ", False, False)

    Helper.BersihkanLayar()

    if User.Registrasi(nama, password, passwordUlang):
        MenuUtama()
    else: 
        MenuRegistrasi() 

def MenuProfil():
    Helper.CetakHeader("PROFIL USER")

    Helper.CetakList([
        "ID User:  " + str(User.user["id"]),
        "Nama:  " + User.user["nama"],
        "Saldo: Rp. {:,}".format(User.user["saldo"]) 
    ])

    Helper.CetakList([
        "> 1. 📜 Ganti Nama", 
        "> 2. 📜 Ganti Password",
        "> 3. 💰 Top Up Saldo",
        "> 4. 🚪 Logout",
    ])

    pilihan = Helper.Pilih()
    Helper.BersihkanLayar()
    if pilihan == 1:
        MenuProfilGantiNama()
    elif pilihan == 2:
        MenuProfilGantiPassword()
    elif pilihan == 3:
        MenuTopUpSaldo() 
    elif pilihan == 4:
        User.Logout()
    else:
        Helper.CetakHeader("⚠️\tERROR - Pilihan Invalid", "-")
        MenuProfil()

    MenuUtama()

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
    pw = Helper.Pilih("Masukan Password Anda: ", False, False)
    saldo = Helper.Pilih("Masukan saldo: ", tips=False)

    Helper.BersihkanLayar()
    if User.TopUpSaldo(pw, saldo):
        MenuProfil()
    else:
        MenuTopUpSaldo()

def MenuProfilGantiPassword():
    Helper.CetakHeader("GANTI PASSWORD")
    pwLama = Helper.Pilih("Masukan password lama: ", False, False)
    pwBaru = Helper.Pilih("Masukan password baru: ", False, False)
    Helper.BersihkanLayar()
    if User.GantiPassword(pwLama, pwBaru):
        MenuProfil()
    else:
        MenuProfilGantiPassword()

def MenuKursus():
    Helper.CetakHeader("MENU KURSUS")

    Helper.CetakList([
        "> 1. 📚 List Semua Kursus",
        "> 2. 📚 List Kursus Berdasarkan Bidang",
        "> 3. 📚 List Kursus Berdasarkan Harga",
        "> 4. 📓 Detail & Daftar Kursus",
        "> 5. 📓 Kursus Yang Saya Ikuti", 
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
        MenuKursusDetail() 
    elif pilihan == 5:
        MenuKursusYangUserIkuti()
    else:
        Helper.CetakHeader("⚠️\tERROR: Pilihan Invalid!", "-")
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

    Kursus.CetakKursusYangDiikuti(User.user)
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