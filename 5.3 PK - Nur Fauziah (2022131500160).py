# Fungsi untuk menghitung IPS
def hitung_ips():
    total_nilai = 0
    total_sks = 0

    # Input jumlah mata kuliah
    jumlah_matkul = int(input("Berapa jumlah mata kuliah? "))

    for i in range(jumlah_matkul):
        nilai = input(f"Nilai mata kuliah ke-{i + 1} (A/B/C/D): ").upper()
        
        if nilai == 'A':
            total_nilai += 4
            total_sks += 1
        elif nilai == 'B':
            total_nilai += 3
            total_sks += 1
        elif nilai == 'C':
            total_nilai += 2
            total_sks += 1
        elif nilai == 'D':
            total_nilai += 1
            total_sks += 1
        else:
            print(f"Nilai '{nilai}' tidak valid. Gunakan A, B, C, atau D.")
            continue  # Abaikan input jika tidak valid

    # Menghitung IPS
    ips = total_nilai / total_sks if total_sks > 0 else 0
    return ips

# Menghitung dan menampilkan IPS
ips_hasil = hitung_ips()
print(f"Nilai IPS anda: {ips_hasil:.2f}")
