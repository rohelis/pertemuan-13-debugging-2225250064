def hitung_rata_rata(nilai):
    # Mengganti pembagi statis 5 menjadi len(nilai)
    return sum(nilai) / len(nilai)


def status(nilai):
    # Mengubah operator > menjadi >=
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    # Inisialisasi dengan elemen pertama dan ubah operator < menjadi >
    tertinggi = nilai[0]
    for x in nilai:
        if x > tertinggi:
            tertinggi = x
    return tertinggi


# Pengujian dengan data awal
nilai = [80, 60, 90, 70]
print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))