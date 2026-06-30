harga_daging_1_kilo = 120000
total_belanja = 0
var_list = []

while True:
    # Tambahkan nomor pembelian baru ke var_list
    var_list.append(len(var_list) + 1)
    
    # Loop menggunakan for i in var_list untuk pembelian terakhir
    for i in var_list[-1:]:
        print(f"\n===== PEMBELIAN KE-{i} =====")
        jumlah_kilo = int(input("Masukkan jumlah daging yang ingin dibeli (dalam kilo): "))
        total_harga = harga_daging_1_kilo * jumlah_kilo

        if jumlah_kilo > 5:
            diskon = 7000
        elif jumlah_kilo >= 2:
            diskon = 5000
        else:
            diskon = 0

        harga_setelah_diskon = total_harga - diskon
        total_belanja += harga_setelah_diskon

        print(f"Harga per kilo daging: Rp {harga_daging_1_kilo:,}")
        print(f"Jumlah daging yang dibeli: {jumlah_kilo} kilo")
        print(f"Total harga sebelum diskon: Rp {total_harga:,.0f}")
        print(f"Diskon yang diberikan: Rp {diskon:,.0f}")
        print(f"Total harga setelah diskon: Rp {harga_setelah_diskon:,.0f}")
    
    # Tanya apakah cukup
    cukup = input("\nCukup? (ketik 'cukup' untuk selesai): ").lower()
    if cukup == 'cukup':
        break

print(f"\n===== RINGKASAN TOTAL BELANJA =====")
print(f"Total pembelian: {len(var_list)} kali")
print(f"Detail pembelian: {var_list}")
print(f"Total belanja semua pembelian: Rp {total_belanja:,.0f}")