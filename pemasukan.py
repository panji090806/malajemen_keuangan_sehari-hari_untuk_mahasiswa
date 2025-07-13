from utils import append_csv, baca_csv

FILE = 'data/pemasukan.csv'

def tambah_pemasukan(tanggal, sumber, jumlah, keterangan):
    jumlah_bersih = jumlah.strip().replace(".", "")  # hapus titik
    if not jumlah_bersih.isdigit():
        print("⚠️ Jumlah tidak valid. Gunakan angka tanpa huruf. Contoh: 75000000")
        return

    data = {
        'tanggal': tanggal.strip(),
        'sumber': sumber.strip(),
        'jumlah': jumlah_bersih,
        'keterangan': keterangan.strip()
    }

    append_csv(FILE, data, data.keys())
    print("✅ Pemasukan berhasil dicatat.")

def tampilkan_pemasukan():
    data = baca_csv(FILE)
    if not data:
        print("📂 Data pemasukan masih kosong.")
        return

    print("\n📋 Daftar Pemasukan:")
    for i, item in enumerate(data, 1):
        try:
            tanggal = item.get('tanggal', '').strip()
            sumber = item.get('sumber', '').strip()
            jumlah = item.get('jumlah', '').strip()
            keterangan = item.get('keterangan', '').strip()

            if not all([tanggal, sumber, jumlah, keterangan]):
                raise ValueError("Ada data yang kosong.")

            if not jumlah.replace('.', '').isdigit():
                raise ValueError("Jumlah bukan angka.")

            print(f"{i}. {tanggal} | {sumber} | Rp {jumlah} | {keterangan}")
        except Exception as e:
            print(f"⚠️ Baris ke-{i} error: {e} → {item}")
