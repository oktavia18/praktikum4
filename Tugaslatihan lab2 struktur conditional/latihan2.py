# Minta pengguna untuk memasukkan tiga bilangan
bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))

# Inisialisasi list untuk menyipan bilangan-bilangan tersebut
bilangan = [bilangan1, bilangan2, bilangan3]

# Mengurutkan bilangan dari yang terkecil ke yang terbesar
bilangan.sort()

# Menampilkan hasil pengurutan
print("Bilangan-bilangan yang telah diurutkan: ", bilangan)