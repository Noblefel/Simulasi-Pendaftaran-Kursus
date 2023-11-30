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

def HitungPotongan(voucher: dict, harga: int) -> float :
    potongan = harga * voucher["potongan"]
    return round(potongan, 2)

def GunakanVoucher(voucher: dict):
    global semuaVoucher

    for v in semuaVoucher:
        if v["kode"] == voucher["kode"]:
            v["sisa"] -= 1

    Helper.SaveDataJSON("voucher.json", semuaVoucher)