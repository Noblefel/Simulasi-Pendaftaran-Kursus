import pwinput

class Menu:
    def __init__(self, helper, user, kursus):
        self.h= helper
        self.u = user
        self.k = kursus

    def pilih(self, s="Masukan Pilihan Anda: ", ubah_int=True, tips=True, password=False):
        if tips:
            print("    'menu' untuk kembali ke menu utama")
            print("    'exit' untuk keluar program \n")

        if password:
            p = pwinput.pwinput("    " + s)
        else:
            p = input("    " + s)

        if p == "menu":
            self.h.bersihkan_layar()
            self.menu_utama()
            return
        elif p == "exit":
            self.h.bersihkan_layar()
            self.h.header("👋 Sampai Jumpa!", "-")
            exit()

        if ubah_int is False:
            return p

        try:
            pilihan_int = int(p)
        except ValueError:
            return p

        return pilihan_int

    def mulai(self):
        self.h.bersihkan_layar()
        try:
            self.menu_utama()
        except KeyboardInterrupt:
            self.h.bersihkan_layar()
            self.h.header("👋 Sampai Jumpa!", "-")

    def menu_utama(self):
        self.h.pilihan("Menu Utama", [
            "> 1. 📚 Kursus",
            "> 2. 👤 " + ("Profil" if self.u.sudah_login() else "Login"),  
            "> 3. 📝 Panel Admin",
            "> 4. 🚪 Exit" 
        ])

        p = self.pilih()
        self.h.bersihkan_layar()
        if p == 1:  
            self.menu_kursus()
        elif p == 2: 
            if self.u.sudah_login():
                self.menu_profil()
            else: 
                self.menu_autentikasi()
        elif p == 3:
            self.menu_admin()
        elif p == 4:  
            self.h.header("👋 Sampai Jumpa", "-")
            exit()
        else:
            self.h.header("⚠️\tERROR: Pilihan Invalid!", "-")
            self.menu_utama()

    def menu_autentikasi(self):
        self.h.pilihan("Menu Autentikasi", [
            "> 1. 👤 Login",
            "> 2. ⏏️  Registrasi Akun"
        ])

        p = self.pilih()
        self.h.bersihkan_layar()
        if p == 1:
            self.menu_login()
        elif p == 2:
            self.menu_registrasi()
        else:
            self.h.header("⚠️\tERROR: Pilihan Invalid!", "-")
            self.menu_autentikasi()

    def menu_login(self):
        self.h.header("Login - Masukan Kredensial Anda", "-")
        nama = self.pilih("Nama: ", False, False)
        password = self.pilih("Password: ", False, False, True)
        self.h.bersihkan_layar()

        if self.u.login(nama, password):
            self.h.header("✅ Login Berhasil!", "-")
            self.menu_utama()
        else:
            self.menu_login()

    def menu_registrasi(self):
        self.h.header("⏏️  REGISTRASI - Silahkan Daftar Akun Anda") 
        nama = self.pilih("Nama: ", False, False) 
        password = self.pilih("Password: ", False, False, True)
        self.h.bersihkan_layar() 

        if self.u.registrasi(nama, password):
            self.menu_utama()
        else: 
            self.menu_registrasi() 

    def menu_profil(self): 
        self.h.pilihan("Profil User", [
            "ID User:  " + str(self.u.u["id"]),
            "Nama:  " + self.u.u["nama"],
            "Tingkat Pendidikan:  " + self.u.u["pendidikan"],
            "Alamat:  " + self.u.u["alamat"],
            "Saldo: Rp. {:,}".format(self.u.u["saldo"]),
            "Tipe User: " + ("Admin" if self.u.u["admin"] else "Pengguna")
        ])

        self.h.pilihan("", [
            "> 1. 📜 Ganti Nama", 
            "> 2. 📜 Ganti Password",
            "> 3. 📜 Ganti Pendidikan",
            "> 4. 📜 Ganti Alamat",
            "> 5. 💰 Top Up Saldo",
            "> 6. 🚪 Logout",
        ])

        p = self.pilih()
        self.h.bersihkan_layar()
        if p == 1:
            self.menu_profil_edit_nama()
        elif p == 2:
            self.menu_profil_edit_password()
        elif p == 3:
            self.menu_profil_edit_pendidikan()
        elif p == 4:
            self.menu_profil_edit_alamat()
        elif p == 5:
            self.menu_profil_topup() 
        elif p == 6:
            self.u.logout()
            self.menu_utama()
        else:
            self.h.header("⚠️\tERROR - Pilihan Invalid", "-")
            self.menu_profil()

    def menu_profil_edit_nama(self):
        self.h.header("Edit Nama")
        nama = self.pilih("Masukan nama baru: ", False, False)
        self.h.bersihkan_layar()

        if self.u.edit("nama", nama):
            self.menu_profil()
        else:
            self.menu_profil_edit_nama()

    def menu_profil_topup(self):
        self.h.header("💰 Top Up Saldo") 
        saldo = self.pilih("Masukan saldo: ", tips=False)
        self.h.bersihkan_layar()

        if self.u.edit("saldo", saldo):
            self.menu_profil()
        else:
            self.menu_profil_topup()

    def menu_profil_edit_password(self):
        self.h.header("Edit Password") 
        pw = self.pilih("Masukan password baru: ", False, False, True)
        self.h.bersihkan_layar()

        if self.u.edit("password", pw):
            self.menu_profil()
        else:
            self.menu_profil_edit_password()

    def menu_profil_edit_pendidikan(self):
        self.h.header("Edit Pendidikan")
        pnd = self.pilih("Masukan tingkat pendidikan baru: ", False, False)
        self.h.bersihkan_layar()

        if self.u.edit("pendidikan", pnd):
            self.menu_profil()
        else:
            self.menu_profil_edit_pendidikan()

    def menu_profil_edit_alamat(self):
        self.h.header("Edit Alamat")
        alamat = self.pilih("Masukan alamat baru: ", False, False)
        self.h.bersihkan_layar()

        if self.u.edit("alamat", alamat):
            self.menu_profil()
        else:
            self.menu_profil_edit_nama()

    def menu_admin(self):
        if self.u.sudah_login() is False or self.u.u["admin"] != 1: 
            self.h.header("⚠️  ERROR - Hanya admin yang bisa mengakses panel ini", "-")
            self.menu_utama()

        self.h.pilihan("Menu Admin", [
            "> 1. 📚 Tambah Kursus", 
            "> 2. 📚 Edit Kursus", 
            "> 3. 🔙 Kembali ke Menu Utama"
        ])

        p = self.pilih()
        self.h.bersihkan_layar()
        if p == 1:
            self.menu_admin_buat_kursus() 
        elif p == 2:
            self.menu_admin_edit_kursus()  
        elif p == 3:
            self.menu_utama()
        else:  
            self.h.header("⚠️\t ERROR: Pilihan Invalid!", "-")
            self.menu_admin()

    def menu_admin_buat_kursus(self):
        self.h.header("📚 Masukan Data Kursus Yang Baru")
        judul = self.pilih("Judul: ", False, False)
        bidang = self.pilih("Bidang: ", False, False)
        desk = self.pilih("Deskripsi: ", False, False)
        rating = self.pilih("Rating (1 - 5): ", tips=False)
        harga = self.pilih("Harga : Rp. ", tips=False)
        self.h.bersihkan_layar()

        if self.k.buat(judul, bidang, desk, rating, harga):
            self.menu_admin()
        else: 
            self.menu_admin_buat_kursus()

    def menu_admin_edit_kursus(self, kursus: dict = None):
        if kursus is None:
            self.h.header("Select Kursus terlebih dahulu")
            j = self.pilih("Masukan judul kursus: ", False, tips=False)
            kursus = self.k.ambil(j)
            self.h.bersihkan_layar()
            if kursus is None:
                self.h.header(f"⚠️\tERROR: Kursus {j} tidak ditemukan", "-")
                self.menu_admin_edit_kursus()

        self.h.pilihan("Edit Kursus", [
            "ID:  " + str(kursus["id"]),
            "Judul: " + kursus["judul"],
            "Bidang: " + kursus["bidang"], 
            "Harga: Rp. {:,}".format(kursus["harga"]),
            "Rating: " + "⭐" * kursus["rating"],
            "Deskripsi: " + kursus["deskripsi"]
        ])
        self.h.pilihan("",[
            "> 1. 📝 Ganti Judul",
            "> 2. 📝 Ganti Bidang",
            "> 3. 📝 Ganti Harga",
            "> 4. 📝 Ganti Rating",
            "> 5. 📝 Ganti Deskripsi",
            "> 6. ⛔ Hapus Kursus",
            "> 7. 🔙 Kembali ke Menu Admin",
        ])
        
        p = self.pilih(tips=False)
        self.h.bersihkan_layar()
        if p == 1:
            self.menu_admin_edit_kursus_judul(kursus) 
        elif p == 2: 
            self.menu_admin_edit_kursus_bidang(kursus) 
        elif p == 3: 
            self.menu_admin_edit_kursus_harga(kursus) 
        elif p == 4: 
            self.menu_admin_edit_kursus_rating(kursus)
        elif p == 5: 
            self.menu_admin_edit_kursus_desk(kursus)  
        elif p == 6: 
            self.k.hapus(kursus["judul"])
            self.menu_admin()
        elif p == 7: 
            self.menu_admin()
        else:
            self.h.header("⚠️\tERROR - Pilihan Invalid", "-")
            self.menu_admin_edit_kursus(kursus)

    def menu_admin_edit_kursus_judul(self, kursus: dict):
        self.h.header("Edit Judul Kursus")
        j = self.pilih("Masukan judul baru: ", False, False)
        self.h.bersihkan_layar()
        if self.k.edit(kursus, "judul", j):
            self.menu_admin_edit_kursus(kursus)
        else:
            self.menu_admin_edit_kursus_judul(kursus)

    def menu_admin_edit_kursus_bidang(self, kursus: dict):
        self.h.header("Edit Bidang Kursus")
        b = self.pilih("Masukan bidang: ", False, False)
        self.h.bersihkan_layar()
        if self.k.edit(kursus, "bidang", b):
            self.menu_admin_edit_kursus(kursus)
        else:
            self.menu_admin_edit_kursus_bidang(kursus)

    def menu_admin_edit_kursus_harga(self, kursus: dict):
        self.h.header("Edit harga kursus")
        h = self.pilih("Masukan harga baru: ", tips=False)
        self.h.bersihkan_layar()
        if self.k.edit(kursus, "harga", h):
            self.menu_admin_edit_kursus(kursus)
        else:
            self.menu_admin_edit_kursus_harga(kursus)

    def menu_admin_edit_kursus_rating(self, kursus: dict):
        self.h.header("Edit rating kursus")
        r = self.pilih("Masukan rating baru (1-5): ", tips=False)
        self.h.bersihkan_layar()
        if self.k.edit(kursus, "rating", r):
            self.menu_admin_edit_kursus(kursus)
        else:
            self.menu_admin_edit_kursus_rating(kursus)

    def menu_admin_edit_kursus_desk(self, kursus: dict):
        self.h.header("GANTI DESKRIPSI KURSUS")
        desk = self.pilih("Masukan deskripsi baru: ", False, False)
        self.h.bersihkan_layar()
        if self.k.edit(kursus, "deskripsi", desk):
            self.menu_admin_edit_kursus(kursus)
        else:
            self.menu_admin_edit_kursus_desk(kursus)

    def menu_kursus(self):
        self.h.pilihan("Menu Kursus", [
            "> 1. 📚 List Semua Kursus",
            "> 2. 📚 List Kursus Berdasarkan Bidang",
            "> 3. 📚 List Kursus Berdasarkan Harga",
            "> 4. 📚 List Kursus Berdasarkan Rating",
            "> 5. 📓 Detail & Daftar Kursus",
            "> 6. 📓 Kursus Yang Saya Ikuti", 
        ])

        p = self.pilih()
        self.h.bersihkan_layar()
        if p == 1:
            self.k.cetak()
            self.menu_kursus()
        elif p == 2:
            self.menu_kursus_bidang()
        elif p == 3:
            self.menu_kursus_harga()
        elif p == 4:
            self.menu_kursus_rating()
        elif p == 5:
            self.menu_kursus_detail() 
        elif p == 6:
            self.menu_kursus_terdaftar()
        else:
            self.h.header("⚠️\t ERROR: Pilihan Invalid!", "-")
            self.menu_kursus()

    def menu_kursus_bidang(self):
        self.h.pilihan("Bidang kursus yang tersedia", [
            "> 1. 💳 Bisnis",
            "> 2. 🤝 Humaniora",
            "> 3. 🚑 Kesehatan",
            "> 4. 🏫 Pendidikan",
            "> 5. 🔬 Sains",
            "> 6. 🎨 Seni",
        ])

        p = self.pilih()
        self.h.bersihkan_layar()
        if p == 1:
            self.k.cetak("Bisnis", k="bidang")
        elif p == 2:
            self.k.cetak("Humaniora", k="bidang")
        elif p == 3:
            self.k.cetak("Kesehatan", k="bidang")
        elif p == 4:
            self.k.cetak("Pendidikan", k="bidang")
        elif p == 5:
            self.k.cetak("Sains", k="bidang")
        elif p == 6:
            self.k.cetak("Seni", k="bidang")
        else:
            self.h.header("⚠️\tERROR: Bidang Invalid", "-")
            self.menu_kursus_bidang()
        
        self.menu_kursus()

    def menu_kursus_harga(self):  
        self.h.pilihan("Select range harga", [
            "> 1. Rp. 0 - Rp. 100,000",
            "> 2. Rp. 100,000 - Rp. 200,000",
            "> 3. Rp. 200,000 - Rp. 300,000",
            "> 4. Rp. 300,000+"
        ])

        p = self.pilih()
        self.h.bersihkan_layar()
        if p == 1:
            self.k.cetak(0, 100000, k="harga", judul="Semua kursus di harga 0 - Rp. 100,000")
        elif p == 2:
            self.k.cetak(100000, 200000, k="harga", judul="Semua kursus di harga Rp. 100,000 - Rp. 200,000")
        elif p == 3:
            self.k.cetak(200000, 300000, k="harga", judul="Semua kursus di harga Rp. 200,000 - Rp. 300,000")
        elif p == 4:
            self.k.cetak(300000, k="harga", judul="Semua kursus di atas harga Rp. 300,000")
        else:
            self.h.header("⚠️\tERROR - Pilihan Invalid", "-")
            self.menu_kursus_harga()

        self.menu_kursus()

    def menu_kursus_rating(self):
        self.h.pilihan("Select rating", [
            "> 1. ⭐⭐⭐⭐⭐",
            "> 2. ⭐⭐⭐⭐",
            "> 3. ⭐⭐⭐",
            "> 4. ⭐⭐",
            "> 5. ⭐"
        ])

        p = self.pilih()
        self.h.bersihkan_layar()
        if p == 1:
            self.k.cetak(5, k="rating")
        elif p == 2:
            self.k.cetak(4, k="rating")
        elif p == 3:
            self.k.cetak(3, k="rating")
        elif p == 4:
            self.k.cetak(2, k="rating")
        elif p == 5:
            self.k.cetak(1, k="rating")
        else:
            self.h.header("⚠️\tERROR - Pilihan Invalid", "-")
            self.menu_kursus_rating()

        self.menu_kursus()
            
    def menu_kursus_detail(self, kursus: dict = None):
        if kursus is None:
            self.h.header("Select Kursus terlebih dahulu")
            j = self.pilih("Masukan judul kursus: ", False, tips=False)
            kursus = self.k.ambil(j)
            self.h.bersihkan_layar()
            if kursus is None:
                self.h.header(f"⚠️\tERROR: Kursus {j} tidak ditemukan", "-")
                self.menu_kursus_detail()
    
        self.h.pilihan("Detail Kursus", [
            "ID:  " + str(kursus["id"]),
            "Judul: " + kursus["judul"],
            "Bidang: " + kursus["bidang"], 
            "Harga: Rp. {:,}".format(kursus["harga"]),
            "Rating: " + "⭐" * kursus["rating"],
            "Deskripsi: " + kursus["deskripsi"]
        ])
        self.h.pilihan("", [
            "> 1. 📝 Daftar",
            "> 2. 🔙 Kembali ke Menu Kursus",
        ])
        
        p = self.pilih(tips=False)
        self.h.bersihkan_layar()
        if p == 1:
            self.menu_kursus_daftar(kursus)
        elif p == 2: 
            self.menu_kursus()
        else:
            self.h.header("⚠️\tERROR - Pilihan Invalid", "-")
            self.menu_kursus_detail(kursus)

    def menu_kursus_daftar(self, kursus: dict):
        if self.u.sudah_login() is False:
            self.h.header("⚠️\tERROR - Anda Perlu Login Untuk Mendaftar", "-")
            self.menu_kursus_detail(kursus)

        self.h.header("DAFTAR KURSUS", "-")
        self.h.pilihan("",[
            "ID:  " + str(kursus["id"]),
            "Judul: " + kursus["judul"],
            "Bidang: " + kursus["bidang"], 
            "Harga: Rp. {:,}".format(kursus["harga"]),
            "Apakah anda yakin ingin mendaftar di kursus ini?"
        ])  
        self.h.pilihan("",[
            "> 1. ✅ Ya",
            "> 2. 🔙 Tidak",
        ])

        p = self.pilih(tips=False)
        self.h.bersihkan_layar()
        if p == 1: 
            self.k.daftar(kursus) 
            self.menu_kursus_detail(kursus) 
        elif p == 2:
            self.menu_kursus_detail(kursus)
        else:
            self.h.header("⚠️\tERROR - Pilihan Invalid", "-")
            self.menu_kursus_daftar(kursus)

    def menu_kursus_terdaftar(self):
        if self.u.sudah_login() is False:
            self.h.header("⚠️\tERROR - Anda Perlu Login Untuk Melihat Ini", "-")
            self.menu_kursus()

        self.k.cetak(k="terdaftar", judul="Semua kursus yang terdaftar")
        self.h.pilihan("",[  "> 1. 🔙 Kembali ke Menu Kursus"])
        self.pilih()
        self.h.bersihkan_layar()
        self.menu_kursus()