motor_yang_tersedia = ('yz','crf','husqvarna','ktm')
motor_yang_dicari = input('masukan nama motor yang anda cari:')

if (motor_yang_dicari in motor_yang_tersedia):
    print('motor yang anda cari tersedia!')
else:
    print('motor yang anda cari tidak tersedia!')