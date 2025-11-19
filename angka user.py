angka_list = []
for i in range(5):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)

genap = 0
ganjil = 0

for a in angka_list:
    if a % 2 == 0:   
        genap += 1
    else:
        ganjil += 1


print("\n=== Hasil ===")
print("List angka:", angka_list)
print("Jumlah angka genap:", genap)
print("Jumlah angka ganjil:", ganjil)
