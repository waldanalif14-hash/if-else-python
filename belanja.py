jumlah_item = int(input("Masukkan jumlah item belanja: "))

harga_list = []

for i in range(jumlah_item):
    harga = int(input(f"Masukkan harga item ke-{i+1}: "))
    harga_list.append(harga)

total = sum(harga_list)

if total >= 300000:
    total_akhir = total * 0.9  
else:
    total_akhir = total

print("\n=== Rincian Belanja ===")
print("Daftar harga:", harga_list)
print(f"Total sebelum diskon: {total}")
print(f"Diskon: 10%")
print(f"Total akhir: {total_akhir}")
