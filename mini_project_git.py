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
    return a+b


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    return a * b


def divide(a, b):
    result = a / b
    return result


def modulus(a, b):
    return a % b


def power(a, b):
    result = a ** b
    return result


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
