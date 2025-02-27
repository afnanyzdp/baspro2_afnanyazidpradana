import math

def luaslingkaran(jarijari):
    return math.pi * jarijari ** 2

jarijari = float(input("Masukkan jari jari lingkaran: "))

if jarijari > 0:
    luas =luaslingkaran(jarijari)
    print(f"lingkaran dengan jari jari {jarijari} adalah {luas:.2f}")
