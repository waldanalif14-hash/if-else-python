listKota = [
    'Jakarta','Surabaya','Depok','Bekasi','Solo',
    'Jogjakarta','Semarang','Makasar'
]
KotaYangDiCari = input('Kota yang anda cari =')

for i, kota in enumerate(listKota):
    # KITA ubah katanya ke lowercase agar menjadi case insensive
    if kota.lower() == KotaYangDiCari.lower():
        print('Kota yang anda cari berada pada indeks',i)
        break
else:
    print('maaf,kota yang anda cari tidak ada')