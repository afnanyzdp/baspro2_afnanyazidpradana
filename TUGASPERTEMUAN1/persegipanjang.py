def menghitung_luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

panjang = float(input("masukkan panjang persegi panjang: "))
lebar = float(input("masukkan lebar persegi panjang: "))

if panjang > 0 and lebar > 0:
    luas = menghitung_luas_persegi_panjang(panjang, lebar)
    print(f"Luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas:.2f}")
