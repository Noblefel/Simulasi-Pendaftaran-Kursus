from program import helper as Helper, user as User

semuaKursus:list = None
semuaTransaksi: list = None 

def CetakKursus(judul: str = "Daftar Semua Kursus", listKursus: list = None):  
    '''Membuat tabel terstruktur untuk melihat semua kursus yang tersedia'''
    tabel = Helper.Tabel(judul, [
        "Id", 
        "Judul", 
        "Bidang",  
        "Harga Asli",
        "Rating",
    ])

    if listKursus is None:
        listKursus = semuaKursus

    for kursus in listKursus:
        tabel.add_row([
            kursus["id"], 
            kursus["judul"], 
            kursus["bidang"], 
            "Rp. {:,}".format(kursus["harga"]),
            "⭐" * kursus["rating"],
        ])
    print(tabel) 

def CetakKursusMenurutBidang(bidang: str):
    '''Mencetak kursus yang di filter menurut bidang'''

    kursusFiltered = filter(lambda k: k["bidang"] == bidang, semuaKursus)

    CetakKursus("List Kursus Di Bidang " + bidang, kursusFiltered)

def CetakKursusMenurutHarga(n1:int, n2:int = None):
    '''Mencetak kursus yang di filter menurut range harga'''

    if n2 is None:
        kursusFiltered = filter(lambda k: k["harga"] >= n1, semuaKursus)
        judul = f"List Kursus dengan Harga diatas Rp. {n1:,}+" 
    else:
        kursusFiltered = filter(lambda k: k["harga"] >= n1 and k["harga"] <= n2, semuaKursus)
        judul = f"List Kursus dengan Harga Rp. {n1:,} - {n2:,}" 

    CetakKursus(judul, kursusFiltered)

def CetakKursusMenurutRating(n: int):
    '''Mencetak Kursus yang di filter menurut rating minimum'''
    
    kursusFiltered = filter(lambda k: k["rating"] == n, semuaKursus)

    CetakKursus(f"List Kursus Dengan Rating {n} Bintang" , kursusFiltered)

def CetakKursusYangDiikuti():
    '''Mencetak semua kursus yang telah user ikuti'''

    user = User.user

    idKursus = []
    for t in semuaTransaksi:
        if t["user_id"] == user["id"]:
            idKursus.append(t["kursus_id"])

    if len(idKursus) == 0:
        Helper.CetakHeader("⛔ Anda belum mengikuti kursus apapun", "-")
        return
    
    kursusYangDiikuti = filter(lambda k: k["id"] in idKursus, semuaKursus)

    CetakKursus("List Kursus Yang Telah Saya Ikuti", kursusYangDiikuti)

def AmbilKursus(id: int) -> dict | bool:
    '''Mengambil data kursus berdasarkan id'''
    for kursus in semuaKursus:
        if kursus["id"] == id:
            return kursus
    return False

def DaftarKursus(kursus: dict, potongan: int | float = 0):
    '''Mendaftarkan user ke suatu kursus''' 
    global semuaTransaksi
    user = User.user

    for t in semuaTransaksi: 
        if t["user_id"] == user["id"] and t["kursus_id"] == kursus["id"]: 
            Helper.CetakHeader("⚠️\tERROR - Anda telah terdaftar di kursus ini", "-")  
            return 

    harga = kursus["harga"] - potongan

    if harga >= user["saldo"]:
        Helper.CetakHeader("⛔ Gagal - Saldo Anda Tidak Cukup", "-")
        return 

    user["saldo"] -= harga

    semuaTransaksi.append({
        "id": Helper.BuatId(semuaTransaksi),
        "user_id": user["id"],
        "kursus_id": kursus["id"]
    })

    for u in User.semuaUser:
        if u["id"] == user["id"]:
            u = user

    Helper.SaveDataJSON("user.json", User.semuaUser)
    Helper.SaveDataJSON("transaksi.json", semuaTransaksi)
    Helper.CetakHeader("✅ SUKSES - mendaftar di kursus ini", "-")  

def BuatKursus(judul: str, bidang: str, deskripsi: str, rating: int, harga: int) -> bool:
    '''Fungsi untuk menyimpan data kursus baru''' 
    global semuaKursus
    
    if len(judul.replace(" ", "")) == 0 or len(bidang.replace(" ", "")) == 0:
        Helper.CetakHeader("⛔ Gagal - Input tidak boleh kosong", "-")
        return False
    
    if bidang not in ["Bisnis", "Humaniora", "Kesehatan", "Pendidikan", "Sains", "Seni"]:
        Helper.CetakHeader("⛔ Gagal - Bidang invalid", "-")
        return False 
    
    if type(rating) == str or type(harga) == str:
        Helper.CetakHeader("⚠️\tERROR - Rating atau Harga harus berupa nomor dan tidak boleh kosong", "-")
        return False

    if rating < 1 or rating > 5:
        Helper.CetakHeader("⛔ Gagal - Rating harus diantara 1 sampai 5", "-")
        return False 
    
    if harga < 0:
        Helper.CetakHeader("⛔ Gagal - Harga tidak boleh negatif", "-")
        return False 
 
    id = Helper.BuatId(semuaKursus)

    semuaKursus.append({
        "id": id,
        "judul": judul, 
        "bidang": bidang,
        "deskripsi": deskripsi,
        "rating": rating, 
        "harga": harga,
    })

    Helper.SaveDataJSON("kursus.json", semuaKursus)
    Helper.CetakHeader(f"✅ Kursus telah disimpan - dengan id {id}", "-")
    return True 

def GantiJudul(kursus: dict, judul: str) -> bool:
    global semuaKursus

    if len(judul.replace(" ", "")) == 0:
        Helper.CetakHeader("⛔ Gagal - Input tidak boleh kosong", "-")
        return False
    
    for k in semuaKursus:
        if k["id"] == kursus["id"]:
            k["judul"] = judul

    Helper.SaveDataJSON("kursus.json", semuaKursus)
    Helper.CetakHeader("✅ Ganti Judul Berhasil", "-")
    return True

def GantiBidang(kursus: dict, bidang: str) -> bool:
    global semuaKursus

    if bidang not in ["Bisnis", "Humaniora", "Kesehatan", "Pendidikan", "Sains", "Seni"]:
        Helper.CetakHeader("⛔ Gagal - Bidang invalid", "-")
        return False 
    
    for k in semuaKursus:
        if k["id"] == kursus["id"]:
            k["bidang"] = bidang

    Helper.SaveDataJSON("kursus.json", semuaKursus)
    Helper.CetakHeader("✅ Ganti Bidang Berhasil", "-")
    return True

def GantiHarga(kursus: dict, harga: int) -> bool:
    global semuaKursus

    if type(harga) == str:
        Helper.CetakHeader("⚠️\tERROR - Harga harus berupa nomor dan tidak boleh kosong", "-")
        return False
    
    if harga < 0:
        Helper.CetakHeader("⛔ Gagal - Harga tidak boleh negatif", "-")
        return False 
    
    for k in semuaKursus:
        if k["id"] == kursus["id"]:
            k["harga"] = harga

    Helper.SaveDataJSON("kursus.json", semuaKursus)
    Helper.CetakHeader("✅ Ganti Harga Berhasil", "-")
    return True

def GantiRating(kursus: dict, rating: int) -> bool:
    global semuaKursus

    if type(rating) == str:
        Helper.CetakHeader("⚠️\tERROR - Rating harus berupa nomor dan tidak boleh kosong", "-")
        return False
    
    if rating < 1 or rating > 5:
        Helper.CetakHeader("⛔ Gagal - Rating harus diantara 1 sampai 5", "-")
        return False 
    
    for k in semuaKursus:
        if k["id"] == kursus["id"]:
            k["rating"] = rating

    Helper.SaveDataJSON("kursus.json", semuaKursus)
    Helper.CetakHeader("✅ Ganti Rating Berhasil", "-")
    return True

def GantiDeskripsi(kursus: dict, deskripsi: str) -> bool:
    global semuaKursus 
    
    for k in semuaKursus:
        if k["id"] == kursus["id"]:
            k["deskripsi"] = deskripsi

    Helper.SaveDataJSON("kursus.json", semuaKursus)
    Helper.CetakHeader("✅ Ganti Deskripsi Berhasil", "-")
    return True

def HapusKursus(kursus: dict):
    global semuaKursus, semuaTransaksi 
    
    newKursus = filter(lambda k: k["id"] != kursus["id"], semuaKursus)
    newTransaksi = filter(lambda k: k["kursus_id"] != kursus["id"], semuaTransaksi)

    semuaKursus = newKursus
    semuaTransaksi = newTransaksi

    Helper.SaveDataJSON("kursus.json", list(newKursus))
    Helper.SaveDataJSON("transaksi.json", list(newTransaksi))
    Helper.CetakHeader("✅ Kursus Berhasil Dihapus", "-")
    return True