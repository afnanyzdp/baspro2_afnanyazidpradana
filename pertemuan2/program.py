umur = int(input("Masukkan Usia Anda: "))

if umur <= 5:
    print("anda adalah balita")
elif umur > 5 and umur <= 13:
    print("anda termasuk Anak-anak")
elif umur > 13 and umur <= 25:
    print("anda termasuk remaja")
elif umur > 25 and umur <= 35:
    print("anda termasuk Dewasa")
elif umur > 35 and umur <= 55:
    print("anda termasuk Orang tua")
else:
    print("anda termasuk lansia")