from program import helper as Helper, user as User

semuaKursus:list = None
semuaTransaksi: list = None 

def CetakKursus(judul: str = "Daftar Semua Kursus", listKursus: list = None):  
    '''Membuat tabel terstruktur untuk melihat semua kursus yang tersedia'''
    tabel = Helper.Tabel(judul, [
        "Id", 
        "Judul", 
        "Bidang", 
        "Durasi", 
        "Harga Asli"
    ])

    if listKursus is None:
        listKursus = semuaKursus

    for kursus in listKursus:
        tabel.add_row([
            kursus["id"], 
            kursus["judul"], 
            kursus["bidang"], 
            kursus["durasi"],
            "Rp. {:,}".format(kursus["harga"])
        ])
    print(tabel) 

def CetakKursusMenurutBidang(bidang: str):
    '''Mencetak kursus yang di filter menurut bidang'''

    kursusFiltered = filter(lambda x: x["bidang"] == bidang, semuaKursus)

    CetakKursus("List Kursus Di Bidang " + bidang, kursusFiltered)

def CetakKursusMenurutHarga(n1:int, n2:int = None):
    '''Mencetak kursus yang di fiter menurut range harga'''

    if n2 is None:
        kursusFiltered = filter(lambda x: x["harga"] >= n1, semuaKursus)
        judul = f"List Kursus dengan Harga diatas Rp. {n1:,}+" 
    else:
        kursusFiltered = filter(lambda x: x["harga"] >= n1 and x["harga"] <= n2, semuaKursus)
        judul = f"List Kursus dengan Harga Rp. {n1:,} - {n2:,}" 

    CetakKursus(judul, kursusFiltered)

def CetakKursusYangDiikuti(user: dict):
    '''Mencetak semua kursus yang telah user ikuti'''

    idKursus = []
    for t in semuaTransaksi:
        if t["user_id"] == user["id"]:
            idKursus.append(t["kursus_id"])

    if len(idKursus) == 0:
        Helper.CetakHeader("Anda belum mengikuti kursus apapun", "-")
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
            Helper.CetakHeader("ERROR - Anda telah terdaftar di kursus ini", "-")  
            return 

    harga = kursus["harga"] - potongan

    if harga >= user["saldo"]:
        Helper.CetakHeader("Gagal - Saldo Anda Tidak Cukup", "-")
        return 

    semuaTransaksi.append({
        "id": Helper.BuatId(semuaTransaksi),
        "user_id": user["id"],
        "kursus_id": kursus["id"]
    })

    user["saldo"] -= harga

    for u in User.semuaUser:
        if u["id"] == user["id"]:
            u = user

    Helper.SaveDataJSON("user.json", User.semuaUser)
    Helper.SaveDataJSON("transaksi.json", semuaTransaksi)
    Helper.CetakHeader("SUKSES - mendaftar di kursus ini", "-")  