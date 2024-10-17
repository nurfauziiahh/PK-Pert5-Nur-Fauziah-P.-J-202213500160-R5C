# untuk menghitung perkalian dua bilangan tanpa operator *
def perkalian(a, b):
    hasil = 0
    for _ in range(abs(b)):
        hasil += a
    return hasil if b >= 0 else -hasil

# untuk menghitung pemangkatan dua bilangan tanpa operator **
def pemangkatan(base, exp):
    hasil = 1
    for _ in range(abs(exp)):
        hasil = perkalian(hasil, base)
    return hasil if exp >= 0 else 1 / hasil

# untuk memeriksa apakah suatu bilangan adalah prima
def is_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input dan pengujian fungsi
print("=== Program Perkalian, Pemangkatan, dan Bilangan Prima ===")

# Menghitung perkalian
a = int(input("Masukkan bilangan pertama untuk perkalian: "))
b = int(input("Masukkan bilangan kedua untuk perkalian: "))
print(f"{a} * {b} = {perkalian(a, b)}")

# Menghitung pemangkatan
base = int(input("Masukkan bilangan dasar untuk pemangkatan: "))
exp = int(input("Masukkan pangkat: "))
print(f"{base} ** {exp} = {pemangkatan(base, exp)}")

# Memeriksa bilangan prima
n = int(input("Masukkan bilangan untuk memeriksa apakah prima: "))
if is_prima(n):
    print(f"{n} adalah bilangan prima.")
else:
    print(f"{n} bukan bilangan prima.")