from program import menu 
import json
import os 
import prettytable
import textwrap 
import pwinput
from emoji import emoji_count

# Settings
lebarDefault = 58 
indentasiDefault = 4

def BersihkanLayar():
    os.system('cls') 

def CetakGaris(garis: str = "=", lebar: int = lebarDefault):
    '''Mencetak garis seperti "========="'''
    print(" " * indentasiDefault + garis * lebar) 

def CetakGarisJustified(kalimat: str = "", lebar: int = lebarDefault):
    '''Mencetak baris dengan batas "|" kanan kiri yang teratur'''

    lebar = lebar - emoji_count(kalimat)

    string = " " * indentasiDefault + f"|   {kalimat.ljust(lebar - 6)} |"
    print(string)

def CetakHeader(kalimat: str, garis: str = "=", lebar: int = lebarDefault, indentasi: int = indentasiDefault):
    '''Mencetak header dengan garis'''
 
    CetakGaris(garis, lebar)
    print(" " * indentasi + kalimat.center(lebar))
    CetakGaris(garis, lebar)

def CetakList(pilihan: list, lebar: int = lebarDefault):
    '''Mencetak list pilihan dibawah header'''

    CetakGarisJustified(lebar=lebar)
    for p in pilihan:
        CetakGarisJustified(p, lebar=lebar) 
    CetakGarisJustified(lebar=lebar)
    CetakGaris(lebar=lebar)
 
def CetakParagraph(paragraph: str, lebar:int = lebarDefault, indentasi: int = indentasiDefault):
    '''Mencetak paragraph panjang yang akan dibreak ke garis baru secara teratur'''
    
    listString = textwrap.wrap(paragraph, lebar - 4, initial_indent=" " * indentasi, subsequent_indent=" " * indentasi)
    print("\n".join(listString))

def Pilih(string: str = "Masukan Pilihan Anda: ", ubahKeInt: bool = True, tips: bool = True, password: bool = False) -> str | int:
    '''Fungsi input() yang dimodifikasi''' 

    if tips:
        print(" " * indentasiDefault + "'menu' untuk kembali ke menu utama")
        print(" " * indentasiDefault + "'exit' untuk keluar program \n")

    if password:
        pilihan = pwinput.pwinput(" " * indentasiDefault + string)
    else:
        pilihan = input(" " * indentasiDefault + string)

    if pilihan == "menu":
        BersihkanLayar()
        menu.MenuUtama()
        return
    elif pilihan == "exit":
        BersihkanLayar()
        CetakHeader("👋 Sampai Jumpa!", "-")
        exit()

    if ubahKeInt is False:
        return pilihan

    try:
        pilihanInt = int(pilihan)
    except ValueError:
        return pilihan
 
    return pilihanInt

def AmbilDataJSON(namaFile: str) -> any:
    '''Ambil data dari file .json di dalam folder "data"'''

    path = os.path.realpath(__file__)
    path = path.replace('program', 'data')
    path = path.replace('helper.py', "") + namaFile

    try:
        jsonFile = open(path)
        data = json.load(jsonFile)
        jsonFile.close()
    except FileNotFoundError: 
        BersihkanLayar()
        CetakHeader(f"⚠️\tERROR - File {namaFile} tidak ditemukan" )
        exit()
    except json.decoder.JSONDecodeError as j: 
        SaveDataJSON(namaFile, [])
        data = []

    return data
 
def SaveDataJSON(namaFile: str, data: any):
    '''Safe data ke file .json di dalam folder "data"'''

    path = os.path.realpath(__file__)
    path = path.replace('program', 'data')
    path = path.replace('helper.py', "") + namaFile 
    
    with open(path, "w") as jsonFile:
        json.dump(data, jsonFile, indent=4) 

def Tabel(judul: str, headings: list) -> prettytable.PrettyTable:
    '''Membuat tabel terstruktur dengan package prettytable'''

    tabel = prettytable.PrettyTable(headings)
    tabel.padding_width = 2
    tabel.align = "l"
    tabel.title = judul
    
    return tabel

def BuatId(l: list, key: str = "id") -> int:
    if len(l) == 0:
        return 1
    
    return l[-1][key] + 1 