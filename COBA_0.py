nama_program = "Belajar Python"
versi = 1
usia = 22
nama_user = "Azka"
print(f"---Selamat Datang di {nama_program} v{versi} ---")

print(f"Halo {nama_user}, tahun depan usia Anda adalah {usia + 1} tahun.")


nama_user = input("Azka: ")
usia = int(input("22: "))

print(f"Halo {nama_user}, tahun depan usia Anda adalah {usia + 1} tahun.")


harga_daging_1_kilo = 120000
jumlah_kilo = int(input("Masukkan jumlah daging yang ingin dibeli (dalam kilo): "))
total_harga = harga_daging_1_kilo * jumlah_kilo
print(f"Total harga untuk {jumlah_kilo} kilo daging adalah Rp{total_harga}.")