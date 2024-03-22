import json
import os
import prettytable

class Helper:
    def __init__(self, data_path):
        self.lebar = 58
        self.path = data_path

    def bersihkan_layar(self):
        os.system('cls')

    def garis(self, garis="=", kalimat=""):
        if kalimat != "":
            print(f"    |   {kalimat.ljust(self.lebar - 6)}")
        else:
            print("    " + garis * self.lebar)

    def header(self, kalimat, garis="="):
        self.garis(garis)
        print(kalimat.center(self.lebar + 6))
        self.garis(garis)

    def pilihan(self, header, pilihan):
        if header != "":
            self.header(header, "-")
        self.garis()
        print()
        for p in pilihan:
            self.garis(kalimat=p)
        print()
        self.garis()

    def read_json(self, f_name):
        path = os.path.join(self.path, f_name)

        try:
            with open(path, "r") as f:
                data = json.load(f)
        except IOError as e:
            self.bersihkan_layar()
            print(e)
            exit()
        except json.decoder.JSONDecodeError:
            self.write_json(path, [])
            data = []

        return data

    def write_json(self, f_name, data):
        path = os.path.join(self.path, f_name)

        try:
            with open(path, "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            self.bersihkan_layar()
            print(e)
            exit()

    def tabel(self, judul, headings) -> prettytable.PrettyTable:
        tabel = prettytable.PrettyTable(headings)
        tabel.padding_width = 2
        tabel.align = "l"
        tabel.title = judul

        return tabel