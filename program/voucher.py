from program import helper as Helper   

semuaVoucher: list = None

def AmbilVoucher(kode: str) -> dict:
    if len(kode) == 0:
        Helper.CetakHeader("⚠️\tERROR - Kode Voucher tidak boleh kosong", "-")
        return 

    for v in semuaVoucher:
        if v["kode"] == kode:
            if v["sisa"] <= 0:
                Helper.CetakHeader("⚠️\tERROR - Kode Voucher ini telah habis", "-")
                return
            
            return v
        
    Helper.CetakHeader("⛔ Gagal - Kode Voucher Tidak Ditemukan", "-")

def AmbilVoucherData(kode: str) -> dict | bool:  
    for v in semuaVoucher:
        if v["kode"] == kode: 
            return v 
    return False


def HitungPotongan(voucher: dict, harga: int) -> float :
    potongan = harga * voucher["potongan"]
    return round(potongan, 2)

def GunakanVoucher(voucher: dict):
    global semuaVoucher

    for v in semuaVoucher:
        if v["kode"] == voucher["kode"]:
            v["sisa"] -= 1

    Helper.SaveDataJSON("voucher.json", semuaVoucher)

def BuatVoucher(nama: str, kode: str, potongan: int, sisa: int) -> bool:
    '''Fungsi untuk menyimpan data kursus baru'''
    global semuaVoucher
    
    if len(nama.replace(" ", "")) == 0 or len(kode.replace(" ", "")) == 0:
        Helper.CetakHeader("⛔ Gagal - Input tidak boleh kosong", "-")
        return False 
    
    if type(potongan) == str or type(sisa) == str:
        Helper.CetakHeader("⚠️\tERROR - Potongan atau Sisa harus berupa nomor dan tidak boleh kosong", "-")
        return False

    if potongan < 0 or potongan > 100:
        Helper.CetakHeader("⛔ Gagal - Potongan harus diantara 1 sampai 100%", "-")
        return False 
    
    if sisa < 0:
        Helper.CetakHeader("⛔ Gagal - Sisa penggunaan tidak boleh negatif", "-")
        return False 

    for v in semuaVoucher:
        if kode == v["kode"]:
            Helper.CetakHeader("⛔ Gagal - Kode Telah Digunakan oleh Voucher lain", "-")
            return False

    semuaVoucher.append({ 
        "nama": nama, 
        "kode": kode,
        "potongan": potongan / 100,
        "sisa": sisa, 
    })

    Helper.SaveDataJSON("voucher.json", semuaVoucher)
    Helper.CetakHeader(f"✅ Voucher telah disimpan - dengan kode {kode}", "-")
    return True 

def GantiNama(voucher: dict, nama: str) -> bool:
    global semuaVoucher

    if len(nama.replace(" ", "")) == 0:
        Helper.CetakHeader("⛔ Gagal - Input tidak boleh kosong", "-")
        return False
    
    for v in semuaVoucher:
        if v["kode"] == voucher["kode"]:
            v["nama"] = nama

    Helper.SaveDataJSON("voucher.json", semuaVoucher)
    Helper.CetakHeader("✅ Ganti Nama Voucher Berhasil", "-")
    return True

def GantiKode(voucher: dict, kode: str) -> bool:
    global semuaVoucher

    if len(kode.replace(" ", "")) == 0:
        Helper.CetakHeader("⛔ Gagal - Input tidak boleh kosong", "-")
        return False
    
    for v in semuaVoucher:
        if v["kode"] == kode:
            Helper.CetakHeader("⛔ Gagal - Kode telah digunakan oleh voucher lain", "-")
            return False
        
    for v in semuaVoucher:
        if v["kode"] == voucher["kode"]:
            v["kode"] = kode

    Helper.SaveDataJSON("voucher.json", semuaVoucher)
    Helper.CetakHeader("✅ Ganti Kode Voucher Berhasil", "-")
    return True

def GantiPotongan(voucher: dict, potongan: float) -> bool:
    global semuaVoucher

    if type(potongan) == str:
        Helper.CetakHeader("⚠️\tERROR - Potongan harus berupa nomor dan tidak boleh kosong", "-")
        return False

    if potongan < 0 or potongan > 100:
        Helper.CetakHeader("⛔ Gagal - Potongan harus diantara 1 sampai 100%", "-")
        return False 
    
    for v in semuaVoucher:
        if v["kode"] == voucher["kode"]:
            v["potongan"] = potongan / 100

    Helper.SaveDataJSON("voucher.json", semuaVoucher)
    Helper.CetakHeader("✅ Ganti Potongan (%) Voucher Berhasil", "-")
    return True

def GantiSisa(voucher: dict, sisa: int) -> bool:
    global semuaVoucher

    if type(sisa) == str:
        Helper.CetakHeader("⚠️\tERROR - Sisa harus berupa nomor dan tidak boleh kosong", "-")
        return False
    
    if sisa < 0:
        Helper.CetakHeader("⛔ Gagal - Sisa tidak boleh negatif", "-")
        return False 

    for v in semuaVoucher:
        if v["kode"] == voucher["kode"]:
            v["sisa"] = sisa

    Helper.SaveDataJSON("voucher.json", semuaVoucher)
    Helper.CetakHeader("✅ Ganti Sisa Penggunaan Berhasil", "-")
    return True

def HapusVoucher(voucher: dict):
    global semuaVoucher 
    
    newVoucher = filter(lambda v: v["kode"] != voucher["kode"], semuaVoucher)

    semuaVoucher = newVoucher

    Helper.SaveDataJSON("voucher.json", list(newVoucher))
    Helper.CetakHeader("✅ Voucher Berhasil Dihapus", "-")
    return True