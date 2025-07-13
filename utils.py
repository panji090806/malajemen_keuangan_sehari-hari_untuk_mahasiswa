import csv
import os

def baca_csv(filepath):
    try:
        with open(filepath, mode='r', newline='', encoding='utf-8') as file:
            data = list(csv.DictReader(file))
        print(f"[DEBUG] Baca {filepath} -> {len(data)} baris")
        return data
    except FileNotFoundError:
        print(f"[DEBUG] File {filepath} tidak ditemukan.")
        return []

def tulis_csv(filepath, data, fieldnames):
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def append_csv(filepath, data, fieldnames):
    file_exists = os.path.isfile(filepath)
    write_header = not file_exists or os.path.getsize(filepath) == 0

    with open(filepath, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(data)
