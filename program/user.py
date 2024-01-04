from program import helper as Helper  
 
user: dict = None
semuaUser: list = None

def Login(nama: str, password: str) -> bool:
    '''Mencoba untuk mengautentikasikan user'''
    global semuaUser, user 

    if len(semuaUser) == 0:
        Helper.CetakHeader("⛔ Program belum memiliki user, silahkan Registrasi", "-")
        return False
    
    for u in semuaUser:
        if u["nama"] == nama and u["password"] == password:
            user = u
            return True

    Helper.CetakHeader("⛔ Nama atau Password Salah!", "-")
    return False

def SudahLogin() -> bool:
    '''Cek apakah user sudah login atau belum'''
    return user is not None

def Logout():
    global user
    user = None
    Helper.CetakHeader("Logout Berhasil", "-")

def Registrasi(nama: str, pendidikan: str, alamat: str, password:str, passwordUlang:str) -> bool:
    '''Fungsi untuk menyimpan data user baru'''
    global semuaUser
    
    if len(nama.replace(" ", "")) == 0 or len(password.replace(" ", "")) == 0:
        Helper.CetakHeader("⛔ Gagal - Input tidak boleh kosong", "-")
        return False
    
    for u in semuaUser:
        if nama == u["nama"]:
            Helper.CetakHeader("⛔ Gagal - Nama Telah Dipakai", "-")
            return False

    if password == passwordUlang:
        semuaUser.append({
            "id": Helper.BuatId(semuaUser),
            "nama": nama, 
            "pendidikan": pendidikan,
            "alamat": alamat,
            "password": password, 
            "saldo": 0,
        })

        Helper.SaveDataJSON("user.json", semuaUser)
        Helper.CetakHeader("✅ Registrasi Berhasil!", "-")
        return True
    else:
        Helper.CetakHeader("⛔ Gagal - Password tidak sama!", "-")
        return False
    
def GantiNama(nama: str) -> bool:
    global semuaUser, user

    if len(nama.replace(" ", "")) == 0:
        Helper.CetakHeader("⛔ Gagal - Input tidak boleh kosong", "-")
        return False

    for u in semuaUser:
        if u["id"] != user["id"]:
            if u["nama"] == nama:
                Helper.CetakHeader("⛔ Gagal - Nama Telah Dipakai", "-")
                return False
    
    user["nama"] = nama

    for u in semuaUser:
        if u["id"] == user["id"]:
            u = user

    Helper.SaveDataJSON("user.json", semuaUser)
    Helper.CetakHeader("✅ Ganti Nama Berhasil", "-")
    return True

def GantiPendidikan(pendidikan: str) -> bool:
    global semuaUser, user  
    
    user["pendidikan"] = pendidikan

    for u in semuaUser:
        if u["id"] == user["id"]:
            u = user

    Helper.SaveDataJSON("user.json", semuaUser)
    Helper.CetakHeader("✅ Ganti Tingkat Pendidikan Berhasil", "-")
    return True

def GantiAlamat(alamat: str) -> bool:
    global semuaUser, user  
    
    user["alamat"] = alamat

    for u in semuaUser:
        if u["id"] == user["id"]:
            u = user

    Helper.SaveDataJSON("user.json", semuaUser)
    Helper.CetakHeader("✅ Ganti Alamat Berhasil", "-")
    return True

def GantiPassword(pwLama: str, pwBaru: str) -> bool:
    global semuaUser, user

    if len(pwLama.replace(" ", "")) == 0 or len(pwBaru.replace(" ", "")) == 0:
        Helper.CetakHeader("⛔ Gagal - Input tidak boleh kosong", "-")
        return False

    if Verifikasi(pwLama, "Password Lama Salah") == False:
        return False
    
    user["password"] = pwBaru

    for u in semuaUser:
        if u["id"] == user["id"]:
            u = user

    Helper.SaveDataJSON("user.json", semuaUser)
    Helper.CetakHeader("✅ Ganti Password Berhasil", "-")
    return True

def TopUpSaldo(pw: str, saldo: int = 0) -> bool:
    global semuaUser, user
    
    if Verifikasi(pw) == False:
        return False
    
    if type(saldo) == str:
        Helper.CetakHeader("⚠️\tERROR - Saldo harus berupa nomor dan tidak boleh kosong", "-")
        return False
        
    if saldo < 1000 :
        Helper.CetakHeader("⚠️\tERROR - Saldo tidak boleh kurang dari 1000", "-")
        return False
        
    user["saldo"] += saldo

    for u in semuaUser:
        if u["id"] == user["id"]:
            u = user

    Helper.SaveDataJSON("user.json", semuaUser)
    Helper.CetakHeader("✅ Top Up Saldo Berhasil", "-")
    return True

def Verifikasi(pw: str, kalimat: str = "Password Anda Salah") -> bool:
    if pw == user["password"]:
        return True
    
    Helper.CetakHeader("⛔ Gagal - " + kalimat, "-")
    return False