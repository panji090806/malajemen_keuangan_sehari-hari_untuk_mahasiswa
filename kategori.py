from utils import baca_csv, tulis_csv

FILE = 'data/kategori.csv'

def lihat_kategori():
    data = baca_csv(FILE)

    if not data:
        print("📂 Belum ada kategori pengeluaran.")
        return

    print("\n📁 Daftar Kategori Pengeluaran:")
    count = 0
    for item in data:
        if 'kategori' in item and item['kategori'].strip():
            print(f"🔹 {item['kategori']}")
            count += 1
        else:
            print("⚠️ Baris kategori rusak atau kosong, dilewati.")

    print(f"📦 Total kategori valid: {count}")

def tambah_kategori(nama):
    nama = nama.strip()
    if not nama:
        print("⚠️ Nama kategori tidak boleh kosong.")
        return

    data = baca_csv(FILE)

    # Cek duplikat nama (case-insensitive)
    if any(item.get('kategori', '').lower() == nama.lower() for item in data):
        print(f"⚠️ Kategori '{nama}' sudah tersedia.")
        return

    data.append({'kategori': nama})
    tulis_csv(FILE, data, ['kategori'])
    print(f"✅ Kategori '{nama}' berhasil ditambahkan.")
