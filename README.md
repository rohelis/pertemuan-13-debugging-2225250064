# Pertemuan 13 - Debugging dan Testing
Nama: Rohelis
NIM: 2225250064
Kelas: 3B

## Kasus
Program Python yang diuji bertugas memproses sekumpulan data nilai mahasiswa. Program ini mencakup tiga fungsi utama:
1. `hitung_rata_rata(nilai)`: Menghitung nilai rata-rata dari list nilai.
2. `status(nilai)`: Menentukan status kelulusan berdasarkan nilai angka.
3. `nilai_tertinggi(nilai)`: Mencari nilai paling tinggi dari sekumpulan data nilai.

## Test Case
| ID | Target Fungsi | Input | Expected | Actual Awal | Status |
|----|---------------|-------|----------|-------------|--------|
| T1 | `hitung_rata_rata` | `[80, 60, 90, 70]` | `75.0` | `70.0` | FAIL |
| T2 | `hitung_rata_rata` | `[100, 80]` | `90.0` | `36.0` | FAIL |
| T3 | `status` | `60` | `Lulus` | `Tidak lulus` | FAIL |
| T4 | `status` | `59` | `Tidak lulus` | `Tidak lulus` | PASS |
| T5 | `nilai_tertinggi` | `[80, 60, 90, 70]` | `90` | `0` | FAIL |

## Bug Report
1. **Bug Fungsi `hitung_rata_rata`**
   - **Gejala:** Hasil perhitungan rata-rata meleset dari nilai sebenarnya saat jumlah elemen list bukan 5.
   - **Lokasi Baris:** `return sum(nilai) / 5`
   - **Akar Penyebab:** Menggunakan pembagi statis angka `5` alih-alih panjang list yang dinamis.
   - **Perbaikan:** Mengganti angka `5` dengan `len(nilai)`.

2. **Bug Fungsi `status`**
   - **Gejala:** Nilai tepat `60` dikategorikan sebagai `"Tidak lulus"`.
   - **Lokasi Baris:** `if nilai > 60:`
   - **Akar Penyebab:** Menggunakan operator strictly greater than (`>`) sehingga batas minimum nilai kelulusan tidak mencakup angka 60.
   - **Perbaikan:** Mengubah operator pembanding dari `>` menjadi `>=`.

3. **Bug Fungsi `nilai_tertinggi`**
   - **Gejala:** Fungsi selalu mengembalikan nilai `0` alih-alih nilai maksimum dalam list.
   - **Lokasi Baris:** `tertinggi = 0` dan `if x < tertinggi:`
   - **Akar Penyebab:** Inisialisasi awal variabel menggunakan `0` dan penggunaan operator `<` yang justru mencari nilai minimum (terkecil), bukan maksimum.
   - **Perbaikan:** Menginisialisasi `tertinggi` dengan elemen pertama list (`nilai[0]`) dan mengubah operator pembanding menjadi `>`.

## Retest
Setelah perbaikan diterapkan, seluruh test case dijalankan kembali dan menghasilkan status pengujian sebagai berikut:

| ID | Target Fungsi | Input | Expected | Actual Akhir | Status |
|----|---------------|-------|----------|--------------|--------|
| T1 | `hitung_rata_rata` | `[80, 60, 90, 70]` | `75.0` | `75.0` | **PASS** |
| T2 | `hitung_rata_rata` | `[100, 80]` | `90.0` | `90.0` | **PASS** |
| T3 | `status` | `60` | `Lulus` | `Lulus` | **PASS** |
| T4 | `status` | `59` | `Tidak lulus` | `Tidak lulus` | **PASS** |
| T5 | `nilai_tertinggi` | `[80, 60, 90, 70]` | `90` | `90` | **PASS** |

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py