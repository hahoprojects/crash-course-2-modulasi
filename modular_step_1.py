"""
Program menghitung luas segitiga
Luas_segitiga = alas * t / 2
"""


def hitung_luas_segitiga(a, t):
    luas_segitiga = a * t / 2
    return luas_segitiga


print('Hitung luas segitiga:\n')
alas = input('Masukkan alas: ')
tinggi = input('Masukkan tinggi: ')

try:
    Luas = int(hitung_luas_segitiga(int(alas), int(tinggi)))
    print(f'Luas = {Luas}')
except Exception as e:
    print('Error: ', e)
