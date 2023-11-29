from program import helper as Helper, user as User, kursus as Kursus 

def MenuUtama():   
    pilihanKedua = "Profil" if User.SudahLogin() else "Login " 

    Helper.CetakHeader("PENDAFTARAN KURSUS - MENU UTAMA")   
    Helper.CetakList([
        "> 1. Kursus",
        "> 2. " + pilihanKedua,  
        "> 3. Exit" 
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
        exit()
    else:
        Helper.CetakHeader("ERROR: Pilihan Invalid!", "-")
        MenuUtama()

def MenuAutentikasi(): 
    Helper.CetakHeader("MENU AUTENTIKASI - Login atau Registrasi")
    Helper.CetakList([
        "> 1. Login",
        "> 2. Registrasi Akun"
    ])

    pilihan = Helper.Pilih()

    Helper.BersihkanLayar()
    
    if pilihan == 1:
        MenuLogin()
    elif pilihan == 2:
        MenuRegistrasi()
    else:
        Helper.CetakHeader("ERROR: Pilihan Invalid!", "-")
        MenuAutentikasi()

def MenuLogin(): 
    Helper.CetakHeader("LOGIN - Masukan Kredensial Anda") 

    nama = Helper.Pilih("Nama: ", False, False)
    password = Helper.Pilih("Password: ", False, False)

    Helper.BersihkanLayar()

    if User.Login(nama, password):
        Helper.CetakHeader("Login Berhasil!", "-")
        MenuUtama()
    else:
        MenuLogin()

def MenuRegistrasi():
    Helper.CetakHeader("REGISTRASI - Silahkan Daftar Akun Anda") 
    nama = Helper.Pilih("Nama: ", False, False) 
    password = Helper.Pilih("Password: ", False, False)
    passwordUlang = Helper.Pilih("Ulangi Password: ", False, False)

    Helper.BersihkanLayar()

    if User.Registrasi(nama, password, passwordUlang):
        Helper.CetakHeader("Registrasi Berhasil!", "-")
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
        "> 1. Ganti Nama", 
        "> 2. Ganti Password",
        "> 3. Top Up Saldo",
        "> 4. Logout",
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
        Helper.CetakHeader("ERROR - Pilihan Invalid", "-")
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
    Helper.CetakHeader("TOP UP SALDO")
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
        "> 1. List Semua Kursus",
        "> 2. List Kursus Berdasarkan Bidang",
        "> 3. List Kursus Berdasarkan Harga",
        "> 4. Detail & Daftar Kursus",
        "> 5. Kursus Yang Saya Ikuti", 
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
        Helper.CetakHeader("ERROR: Pilihan Invalid!", "-")
        MenuKursus()

def MenuKursusBidang():
    Helper.CetakHeader("BIDANG KURSUS YANG TERSEDIA") 

    Helper.CetakList([
        "> 1. Bisnis",
        "> 2. Humaniora",
        "> 3. Kesehatan",
        "> 4. Pendidikan",
        "> 5. Sains",
        "> 6. Seni",
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
        Helper.CetakHeader("ERROR: Bidang Invalid", "-")
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
        Helper.CetakHeader("ERROR - Pilihan Invalid", "-")
        MenuKursusHarga()

    MenuKursus()
        
def MenuKursusDetail(kursus: dict | None = None):

    if kursus is None:
        Helper.CetakHeader("SEARCH KURSUS TERLEBIH DAHULU")
        id = Helper.Pilih("Masukan ID kursus: ", tips=False)
        kursus = Kursus.AmbilKursus(id)
        Helper.BersihkanLayar()
        if kursus is False:
            Helper.CetakHeader(f"ERROR: Kursus Dengan Id-{id} tidak ditemukan", "-")
            MenuKursusDetail() 
 
    Helper.CetakHeader("DETAIL KURSUS", "-")
    Helper.CetakList([
        "ID:  " + str(kursus["id"]),
        "Judul: " + kursus["judul"],
        "Bidang: " + kursus["bidang"],
        "Durasi: " + kursus["durasi"],
        "Harga: Rp. {:,}".format(kursus["harga"]),
    ])

    Helper.CetakParagraph("Deskripsi: " + kursus["deskripsi"], 100)
    print("\n")
    Helper.CetakGaris()
    Helper.CetakList([
        "> 1. Daftar",
        "> 2. Kembali ke Menu Kursus",
    ])
    
    pilihan = Helper.Pilih()
    Helper.BersihkanLayar()
    if pilihan == 1:
        MenuKursusDaftar(kursus) 
    elif pilihan == 2: 
        MenuKursus()
    else:
        Helper.CetakHeader("ERROR - Pilihan Invalid", "-")
        MenuKursusDetail(kursus)

def MenuKursusDaftar(kursus: dict):
    if User.SudahLogin() is False:
        Helper.CetakHeader("ERROR - Anda Perlu Login Untuk Mendaftar Kursus", "-")
        MenuKursusDetail(kursus)

    Helper.CetakHeader("PENDAFTARAN KURSUS")
    Helper.CetakParagraph("Apakah anda yakin ingin mendaftar di kursus \"{0}\" dengan biaya Rp. {1:,}".format(kursus["judul"], kursus["harga"]), 100)
    Helper.CetakGaris("-")
    Helper.CetakList([
        "> 1. Ya",
        "> 2. Tidak",
    ])

    pilihan = Helper.Pilih(tips=False)
    Helper.BersihkanLayar()
    if pilihan == 1: 
        Kursus.DaftarKursus(kursus, User.user, User.semuaUser)  
 
    MenuKursusDetail(kursus)

def MenuKursusYangUserIkuti():
    if User.SudahLogin() is False:
        Helper.CetakHeader("ERROR - Anda Perlu Login Untuk Melihat Bagian Ini", "-")
        MenuKursus()

    Kursus.CetakKursusYangDiikuti(User.user)
    Helper.CetakGaris()
    Helper.CetakList([ 
        "> 1. Kembali ke Menu Kursus",
    ])

    pilihan = Helper.Pilih()
    Helper.BersihkanLayar()
    MenuKursus()

 