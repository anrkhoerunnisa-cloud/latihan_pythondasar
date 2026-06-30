pricelist = {
    "Ayam": 15000,  # Rp15.000/kg
    "Sapi": 12000,  # Rp12.000/kg
    "Babi": 10000,  # Rp10.000/kg
}


def hitung_diskon(jenis: str, subtotal: float, jumlah_kg: float) -> float:
    # Nested if sesuai ketentuan soal
    if jenis == "Ayam":
        if jumlah_kg >= 5:
            return 0.10 * subtotal
        else:
            return 0.0

    elif jenis == "Sapi":
        if jumlah_kg >= 2:
            return 0.15 * subtotal
        else:
            return 0.0

    elif jenis == "Babi":
        if jumlah_kg >= 3:
            return 0.12 * subtotal
        else:
            return 0.0

    # Seharusnya tidak terjadi karena ada validasi jenis, tapi untuk aman.
    return 0.0


def format_rupiah(nilai: float) -> str:
    # Format tanpa simbol tambahan, gunakan pemisah ribuan
    return f"Rp {nilai:,.0f}"


def main():
    nama = input("Masukkan nama Anda: ").strip()
    if not nama:
        nama = "Pelanggan"
    print(f"Selamat datang, {nama} di Toko Daging Meow!\n")

    items = []
    total_kotor = 0.0
    total_diskon = 0.0

    while True:
        jenis_input = input("Masukkan jenis daging (Ayam/Sapi/Babi) atau ketik 'cukup' untuk selesai: ").strip()

        if jenis_input.lower() == "cukup":
            break

        # Normalisasi input agar case-insensitive.
        jenis = jenis_input.capitalize()

        if jenis not in pricelist:
            print("Jenis daging tidak tersedia❌. Silakan pilih Ayam, Sapi, atau Babi.\n")
            continue

        try:
            jumlah_kg = float(input(f"Masukkan jumlah kilogram untuk {jenis} (boleh desimal): ").strip())
        except ValueError:
            print("Input jumlah kilogram tidak valid. Gunakan angka (mis. 2 atau 2.5).\n")
            continue

        if jumlah_kg <= 0:
            print("Jumlah kilogram harus lebih dari 0.\n")
            continue

        harga_per_kg = pricelist[jenis]
        subtotal = harga_per_kg * jumlah_kg
        diskon = hitung_diskon(jenis, subtotal, jumlah_kg)
        total_setelah_diskon = subtotal - diskon

        items.append(
            {
                "jenis": jenis,
                "kg": jumlah_kg,
                "harga_per_kg": harga_per_kg,
                "subtotal": subtotal,
                "diskon": diskon,
                "total": total_setelah_diskon,
            }
        )

        total_kotor += subtotal
        total_diskon += diskon

        print("\n--- Item ditambahkan ---")
        print(f"Jenis           : {jenis}")
        print(f"Jumlah (kg)     : {jumlah_kg:g}")
        print(f"Harga/kg        : {format_rupiah(harga_per_kg)}")
        print(f"Subtotal        : {format_rupiah(subtotal)}")
        print(f"Diskon          : {format_rupiah(diskon)}")
        print(f"Total item      : {format_rupiah(total_setelah_diskon)}")
        print("-------------------------\n")

    total_bersih = total_kotor - total_diskon

    print("\n==================== NOTA PEMBAYARAN ====================")

    if not items:
        print("Tidak ada pembelian.")
    else:
        print("Detail pembelian:")
        for idx, it in enumerate(items, start=1):
            print(f"  {idx}. {it['jenis']} - {it['kg']:g} kg")
            print(f"     Subtotal : {format_rupiah(it['subtotal'])}")
            print(f"     Diskon   : {format_rupiah(it['diskon'])}")
            print(f"     Total    : {format_rupiah(it['total'])}")

    print("----------------------------------------------------------")
    print(f"Total Kotor     : {format_rupiah(total_kotor)}")
    print(f"Total Diskon    : {format_rupiah(total_diskon)}")
    print(f"Total Bersih    : {format_rupiah(total_bersih)}")
    print("==========================================================")


if __name__ == "__main__":
    main()

