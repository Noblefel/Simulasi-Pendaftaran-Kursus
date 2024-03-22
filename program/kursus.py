class Kursus:
    def __init__(self, helper, user):
        self.all = helper.read_json("kursus.json")
        self.h = helper
        self.u = user

    def cetak(self, *v, k="", judul="Semua Kursus"):
        if k == "":
            kursus = self.all
        elif k == "harga":
            if len(v) == 1:
                kursus = dict(
                    filter(lambda x: x[1]["harga"] >= v[0], self.all.items()))
                judul = f"List Kursus dengan Harga diatas Rp. {v[0]:,}+"
            else:
                kursus = dict(
                    filter(lambda x: x[1]["harga"] >= v[0] and x[1]["harga"] <= v[1], self.all.items()))
                judul = f"List Kursus dengan Harga Rp. {v[0]:,} - {v[1]:,}"
        elif k == "terdaftar":
            kursus = dict(
                filter(lambda x: self.u.u["id"] in x[1]["siswa"], self.all.items()))
            judul = "List Kursus Yang Telah Saya Ikuti"
            if len(kursus) == 0:
                self.h.header("⛔ Anda belum mengikuti kursus apapun", "-")
                return
        else:
            kursus = dict(filter(lambda x: x[1][k] == v[0], self.all.items()))
            judul = f"List Kursus menurut {k} - {v[0]}"

        tabel = self.h.tabel(judul, [
            "Id",
            "Judul",
            "Bidang",
            "Harga Asli",
            "Rating",
        ])

        for kk, kv in kursus.items():
            tabel.add_row([
                kv["id"],
                kv["judul"],
                kv["bidang"],
                "Rp. {:,}".format(kv["harga"]),
                "⭐" * kv["rating"],
            ])
        print(tabel)

    def ambil(self, judul) -> dict:
        if judul in self.all:
            return self.all[judul]

    def daftar(self, kursus):
        u = self.u.u

        if u["id"] in kursus["siswa"]:
            self.h.header("⛔ Anda telah terdaftar di kursus ini", "-")
            return

        if kursus["harga"] >= u["saldo"]:
            self.h.header("⛔ Gagal - Saldo Anda Tidak Cukup", "-")
            return

        kursus["siswa"].append(u["id"])
        self.all[kursus["judul"]] = kursus
        self.h.write_json("kursus.json", self.all)

        u["saldo"] -= kursus["harga"]
        self.u.all[u["nama"]] = u
        self.u.u = u
        self.h.write_json("user.json", self.u.all)
        self.h.header("✅ Berhasil Mendaftar", "-")

    def buat(self, judul, bidang, desk, rating, harga) -> bool:
        if len(judul.replace(" ", "")) == 0:
            self.h.header("⛔ Gagal - judul tidak boleh kosong", "-")
            return False

        if bidang not in ["Bisnis", "Humaniora", "Kesehatan", "Pendidikan", "Sains", "Seni"]:
            self.h.header("⛔ Gagal - Bidang invalid", "-")
            return False

        if isinstance(rating, str) or isinstance(harga, str):
            self.h.header(
                "⛔ Gagal - Rating atau harga harus berupa nomor", "-")
            return False

        if rating < 0 or rating > 5:
            self.h.header("⛔ Gagal - Rating harus diantara 1 sampai 5", "-")
            return False

        if harga < 0:
            self.h.header("⛔ Gagal - Harga tidak boleh negatif", "-")
            return False

        i = self.all[max(
            self.all, key=lambda x: self.all[x].get('id', 0))]["id"]
        self.all[judul] = {
            "id": i + 1,
            "judul": judul,
            "bidang": bidang,
            "deskripsi": desk,
            "rating": rating,
            "harga": harga,
            "siswa": [],
        }

        self.h.write_json("kursus.json", self.all)
        self.h.header("✅ Kursus Telah Dibuat", "-")
        return True

    def edit(self, kursus, k, v) -> bool:
        if k == "judul":
            if len(v.replace(" ", "")) == 0:
                self.h.header("⛔ Gagal - Judul tidak boleh kosong", "-")
                return False
            new = kursus
            del self.all[kursus["judul"]]
            new["judul"] = v
            self.all[v] = new
        else:
            if k == "bidang":
                if v not in ["Bisnis", "Humaniora", "Kesehatan", "Pendidikan", "Sains", "Seni"]:
                    self.h.header("⛔ Gagal - Bidang invalid", "-")
                    return False
            elif k == "harga":
                if isinstance(v, str):
                    self.h.header("⛔ Gagal - Harga harus berupa nomor", "-")
                    return False
                if v < 0:
                    self.h.header("⛔ Gagal - Harga tidak boleh negatif", "-")
                    return False
            elif k == "rating":
                if isinstance(v, str):
                    self.h.header("⛔ Gagal - Rating harus berupa nomor", "-")
                    return False
                if v < 0 or v > 5:
                    self.h.header(
                        "⛔ Gagal - Rating harus diantara 1 sampai 5", "-")
                    return False
            new = kursus
            new[k] = v
            self.all[kursus["judul"]] = new

        self.h.write_json("kursus.json", self.all)
        self.h.header(f"✅ Edit {k} Berhasil", "-")
        return True

    def hapus(self, judul):
        del self.all[judul]
        self.h.write_json("kursus.json", self.all)
        self.h.header("✅ Kursus Berhasil Dihapus", "-")
