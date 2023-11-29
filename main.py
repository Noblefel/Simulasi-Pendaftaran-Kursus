from program import menu, helper, user, kursus, voucher

user.semuaUser = helper.AmbilDataJSON("user.json")
kursus.semuaKursus = helper.AmbilDataJSON("kursus.json")   
kursus.semuaTransaksi = helper.AmbilDataJSON("transaksi.json")    
voucher.semuaVoucher = helper.AmbilDataJSON("voucher.json")

helper.BersihkanLayar()

print('''
\t▒█▀▀▀ ▒█▄░▒█ ▒█▀▀█ ▒█▀▀▀█ ▒█░░░ ▒█░░░ ▒█▀▀█ 
\t▒█▀▀▀ ▒█▒█▒█ ▒█▄▄▀ ▒█░░▒█ ▒█░░░ ▒█░░░ ▒█░▒█ 
\t▒█▄▄▄ ▒█░░▀█ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄█ ▒█▄▄█ ░▀▀█▄
''')

try:
    menu.MenuUtama()
except KeyboardInterrupt:
    helper.BersihkanLayar()
    helper.CetakHeader("Sampai Jumpa!", "-") 