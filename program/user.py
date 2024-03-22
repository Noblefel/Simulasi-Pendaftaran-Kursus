class User:
    def __init__(self, helper):
        self.u = None # pengguna sekarang
        self.all = helper.read_json("user.json") # semua User
        self.h = helper

    def sudah_login(self) -> bool:
        return self.u is not None

    def login(self, nama, pw) -> bool:
        if nama in self.all:
            u = self.all[nama]
            if u["password"] == pw:
                self.u = u
                return True

        self.h.header("⛔ Nama atau Password Salah!", "-")
        return False

    def logout(self):
        self.u = None
        self.h.header("Logout Berhasil", "-")

    def registrasi(self, nama, pw) -> bool:
        if len(nama.replace(" ", "")) == 0 or len(pw.replace(" ", "")) == 0:
            self.h.header("⛔ Gagal - Input tidak boleh kosong", "-")
            return False
        if nama in self.all:
            self.h.header("⛔ Gagal - Nama Telah Dipakai", "-")
            return False

        i = self.all[max(self.all, key=lambda x: self.all[x].get('id',0))]["id"]
        self.all[nama] = {
            "id": i + 1,
            "nama": nama,
            "password": pw,
            "pendidikan": "",
            "alamat": "",
            "saldo": 0,
            "admin": 0,
        }
        self.h.write_json("user.json", self.all)
        self.h.header("✅ Registrasi Berhasil", "-")
        return True

    def edit(self, k, v) -> bool:
        if k == "nama": 
            if len(v.replace(" ", "")) == 0:
                self.h.header("⛔ Gagal - Nama baru tidak boleh kosong", "-")
                return False

            if v in self.all:
                self.h.header("⛔ Gagal - Nama Telah Dipakai", "-")
                return False

            del self.all[self.u["nama"]]
        elif k == "password":
            if len(v.replace(" ", "")) == 0:
                self.h.header("⛔ Gagal - Password baru tidak boleh kosong", "-")
                return False
        elif k == "saldo":
            if isinstance(v, str):
                self.h.header("⛔ Gagal - Saldo harus berupa nomor", "-")
                return False
            v += self.u["saldo"] 

        self.u[k] = v
        self.all[self.u["nama"]] = self.u
        self.h.write_json("user.json", self.all)
        self.h.header(f"✅ Edit {k} Berhasil", "-")
        return True