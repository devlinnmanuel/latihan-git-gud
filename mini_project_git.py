"""
Mini Project Git Collaboration - Kalkulator Sederhana

Deskripsi:
Project ini dibuat untuk latihan kolaborasi menggunakan Git dan GitHub.
Setiap anggota tim akan berkontribusi dengan menambahkan atau menyelesaikan
fungsi-fungsi kalkulator yang masih kosong (TODO). Tujuan utama project ini
adalah untuk mempraktikkan:

- Membuat branch untuk fitur tertentu
- Melakukan commit perubahan
- Melakukan merge atau pull request
- Menangani merge conflict jika terjadi
- Berkolaborasi pada satu file yang sama secara aman dan terstruktur

Setiap fungsi dalam file ini sengaja dibiarkan belum lengkap agar dapat
dibagi kepada anggota tim untuk dikerjakan secara paralel.
"""

def add(a, b):
    # TODO: Tambahkan kode untuk operasi penjumlahan
    pass


def subtract(a, b):
    # TODO: Tambahkan kode untuk operasi pengurangan
    pass


def multiply(a, b):
    # TODO: Tambahkan kode untuk operasi perkalian
    pass


def divide(a, b):
    # TODO: Tambahkan pengecekan pembagi nol dan operasi pembagian
    pass


def modulus(a, b):
    # TODO: Tambahkan kode untuk operasi modulus
    pass


def power(a, b):
    # TODO: Tambahkan kode untuk operasi pangkat
    pass


def main():
    print("=== Mini Project Git: Kalkulator ===")
    print("Pilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Modulus")
    print("6. Pangkat")

    choice = input("Masukkan pilihan (1-6): ")

    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))

    if choice == "1":
        print("Hasil:", add(a, b))
    elif choice == "2":
        print("Hasil:", subtract(a, b))
    elif choice == "3":
        print("Hasil:", multiply(a, b))
    elif choice == "4":
        print("Hasil:", divide(a, b))
    elif choice == "5":
        print("Hasil:", modulus(a, b))
    elif choice == "6":
        print("Hasil:", power(a, b))
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
