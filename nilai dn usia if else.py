nilai = int(input('masukkan nilai: '))
usia = int(input('masukan usia: '))

if nilai >= 75:
    if (usia < 15):
        print('selamat ya dek, kamu lulus')
    else:
        print('selamat ya kak, kamu lulus')
else:
    if (usia < 15):
        print('mohon maaf dek, kamu tidak lulus')
    else:
         print('mohon maaf kak, kamu tidak lulus')