from utils import baca_csv
from collections import defaultdict

def laporan_bulanan():
    pemasukan = baca_csv('data/pemasukan.csv')
    pengeluaran = baca_csv('data/pengeluaran.csv')

    total_masuk = 0
    total_keluar = 0

    for i, item in enumerate(pemasukan, 1):
        jumlah = item.get('jumlah', '').replace(".", "").strip()
        if jumlah.isdigit():
            total_masuk += int(jumlah)
        else:
            print(f"⚠️ Baris pemasukan ke-{i} jumlah tidak valid: {item.get('jumlah')}")

    for i, item in enumerate(pengeluaran, 1):
        jumlah = item.get('jumlah', '').replace(".", "").strip()
        if jumlah.isdigit():
            total_keluar += int(jumlah)
        else:
            print(f"⚠️ Baris pengeluaran ke-{i} jumlah tidak valid: {item.get('jumlah')}")

    selisih = total_masuk - total_keluar

    print("\n📊 Laporan Keuangan Bulanan")
    print("=" * 50)
    print(f"📥 Total Pemasukan  : Rp {total_masuk:,}")
    print(f"📤 Total Pengeluaran: Rp {total_keluar:,}")
    print(f"💰 Selisih           : Rp {selisih:,}")
    print("=" * 50)

def laporan_per_kategori():
    pengeluaran = baca_csv('data/pengeluaran.csv')
    laporan = defaultdict(int)

    total = 0
    for i, item in enumerate(pengeluaran, 1):
        kategori = item.get('kategori', '').strip()
        jumlah = item.get('jumlah', '').replace(".", "").strip()

        if kategori and jumlah.isdigit():
            laporan[kategori] += int(jumlah)
            total += int(jumlah)
        else:
            print(f"⚠️ Baris ke-{i} invalid → {item}")

    if not laporan:
        print("\n📂 Tidak ada data pengeluaran yang valid untuk ditampilkan.")
        return

    print("\n📁 Laporan Pengeluaran per Kategori")
    print("=" * 50)
    for kategori, subtotal in laporan.items():
        print(f"🔹 {kategori:<20} : Rp {subtotal:,}")
    print("=" * 50)
    print(f"🧾 Total Semua Kategori : Rp {total:,}")
