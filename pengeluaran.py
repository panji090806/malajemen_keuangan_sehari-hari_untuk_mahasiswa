from utils import append_csv, baca_csv

FILE = 'data/pengeluaran.csv'

def tambah_pengeluaran(tanggal, kategori, jumlah, keterangan):
    jumlah_bersih = jumlah.strip().replace(".", "")  # hapus titik
    if not jumlah_bersih.isdigit():
        print("⚠️ Jumlah tidak valid. Gunakan angka tanpa huruf. Contoh: 250000")
        return

    data = {
        'tanggal': tanggal.strip(),
        'kategori': kategori.strip(),
        'jumlah': jumlah_bersih,
        'keterangan': keterangan.strip()
    }

    append_csv(FILE, data, data.keys())
    print("✅ Pengeluaran berhasil dicatat.")

def tampilkan_pengeluaran():
    data = baca_csv(FILE)
    if not data:
        print("📂 Data pengeluaran masih kosong.")
        return
    print("\n📋 Daftar Pengeluaran:")
    for i, item in enumerate(data, 1):
        if not all(k in item for k in ['tanggal', 'kategori', 'jumlah', 'keterangan']):
            print(f"⚠️ Baris ke-{i} rusak, tidak lengkap: {item}")
            continue
        if not item['jumlah'].replace(".", "").isdigit():
            print(f"⚠️ Baris ke-{i} jumlah tidak valid: {item['jumlah']}")
            continue

        # Format jumlah agar tampil rapi
        jumlah_format = f"{int(item['jumlah']):,}".replace(",", ".")
        print(f"{i}. {item['tanggal']} | {item['kategori']} | Rp {jumlah_format} | {item['keterangan']}")
