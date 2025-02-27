import math

def menghitung_luas_tabung(jarijari, tinggi):
    return 2 * math.pi * jarijari * (jarijari + tinggi)

jarijari = float(input("masukkan jari-jari tabung: "))
tinggi = float(input("masukkan tinggi tabung: "))

if jarijari > 0 and tinggi > 0:
    luas = menghitung_luas_tabung(jarijari, tinggi)
    print(f"luas permukaan tabung dengan jari-jari {jarijari} dan tinggi {tinggi} adalah {luas:.2f}")