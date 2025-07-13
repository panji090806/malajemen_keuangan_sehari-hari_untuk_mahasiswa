from pemasukan import tambah_pemasukan, tampilkan_pemasukan
from pengeluaran import tambah_pengeluaran, tampilkan_pengeluaran
from kategori import lihat_kategori, tambah_kategori
from laporan import laporan_bulanan, laporan_per_kategori

def garis():
    print("="*60)

def menu():
    garis()
    print("📘 Aplikasi Manajemen Keuangan Mahasiswa")
    garis()
    print("1. Tambah Pemasukan")
    print("2. Tambah Pengeluaran")
    print("3. Lihat Pemasukan")
    print("4. Lihat Pengeluaran")
    print("5. Laporan Bulanan")
    print("6. Laporan per Kategori")
    print("7. Lihat Kategori")
    print("8. Tambah Kategori")
    print("9. Keluar")
    print("10. Tampilkan Isi File CSV")
    garis()

while True:
    menu()
    pilih = input("Pilih menu [1-10]: ").strip()

    if pilih == '1':
        tanggal = input("Tanggal (YYYY-MM-DD): ").strip()
        sumber = input("Sumber Pemasukan: ").strip()
        jumlah = input("Jumlah (Rp): ").strip()
        ket = input("Keterangan: ").strip()
        tambah_pemasukan(tanggal, sumber, jumlah, ket)

    elif pilih == '2':
        tanggal = input("Tanggal (YYYY-MM-DD): ").strip()
        kategori = input("Kategori Pengeluaran: ").strip()
        jumlah = input("Jumlah (Rp): ").strip()
        ket = input("Keterangan: ").strip()
        tambah_pengeluaran(tanggal, kategori, jumlah, ket)

    elif pilih == '3':
        tampilkan_pemasukan()

    elif pilih == '4':
        tampilkan_pengeluaran()

    elif pilih == '5':
        laporan_bulanan()

    elif pilih == '6':
        laporan_per_kategori()

    elif pilih == '7':
        lihat_kategori()

    elif pilih == '8':
        nama = input("Nama Kategori Baru: ").strip()
        tambah_kategori(nama)

    elif pilih == '9':
        print("\n🙏 Terima kasih telah menggunakan Manajemen Keuangan Mahasiswa.")
        break

    elif pilih == '10':
        print("\n📂 Pilih file yang ingin ditampilkan:")
        print("a. pemasukan.csv")
        print("b. pengeluaran.csv")
        print("c. kategori.csv")
        file_pilihan = input("Masukkan pilihan [a/b/c]: ").strip().lower()

        file_map = {
            'a': 'data/pemasukan.csv',
            'b': 'data/pengeluaran.csv',
            'c': 'data/kategori.csv'
        }

        filepath = file_map.get(file_pilihan)

        if not filepath:
            print("⚠️ Pilihan tidak valid.")
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                isi = file.read()
                print(f"\n📄 Isi file {filepath}:\n")
                print(isi)
        except FileNotFoundError:
            print(f"⚠️ File {filepath} tidak ditemukan.")
        except Exception as e:
            print(f"⚠️ Terjadi kesalahan saat membuka file: {e}")

    else:
        print("⚠️ Pilihan tidak tersedia. Silakan pilih antara 1–10.")
