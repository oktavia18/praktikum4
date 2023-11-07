# minta pengguna untuk memasukan tiga bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))

# Inilisiasi variabel untuk bilangan terbesar
bilangan_terbesar = bilangan1

# Periksa variabel untuk bilangan kedua lebih besar dari bilangan_terbesar
if bilangan2 > bilangan_terbesar:
    bilangan_terbesar = bilangan2

# Periksa variabel untuk bilangan ketiga lebih besar dari bilangan_terbesar
if bilangan3 > bilangan_terbesar:
    bilangan_terbesar = bilangan3

# tampilkan bilangan terbesar
print("Bilangan terbesar adalah:", bilangan_terbesar) 