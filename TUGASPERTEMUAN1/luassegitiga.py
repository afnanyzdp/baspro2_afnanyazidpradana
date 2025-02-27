def menghitung_luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

alas = float(input("masukkan alas segitiga: "))
tinggi = float(input("masukkan tinggi segitiga: "))

if alas > 0 and tinggi > 0:
    luas = menghitung_luas_segitiga(alas, tinggi)
    print(f"luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas:.2f}")
