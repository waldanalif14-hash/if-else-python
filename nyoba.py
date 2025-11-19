input_nilai = input("Masukkan list nilai mahasiswa : ")

nilai_list = [int(n.strip()) for n in input_nilai.split(",")]

def kategori(n):
    if n >= 85:
        return "A"
    elif 70 <= n <= 84:
        return "B"
    elif 55 <= n <= 69:
        return "C"
    else:
        return "D"

for n in nilai_list:
    print(f"Nilai {n} = Kategori {kategori(n)}")
