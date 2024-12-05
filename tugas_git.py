data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {
            "padi": 1200,
            "jagung": 800,
            "kedelai": 500
        }
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {
            "padi": 1500,
            "jagung": 900,
            "kedelai": 450
        }
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {
            "padi": 1100,
            "jagung": 750,
            "kedelai": 600
        }
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {
            "padi": 1300,
            "jagung": 850,
            "kedelai": 550
        }
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {
            "padi": 1400,
            "jagung": 950,
            "kedelai": 480
        }
    }
}

# 1. Tampilkan seluruh data dari data_panen termasuk nama lokasi dan hasil panen masing-masing.
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    print("Hasil Panen:")
    for komoditas, hasil in data['hasil_panen'].items():
        print(f"- {komoditas}: {hasil}")
    print()  

# 2. Tampilkan jumlah hasil panen jagung dari lokasi2
jumlah_jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"*Jumlah hasil panen jagung di lokasi2: {jumlah_jagung_lokasi2}")

# 3. Tampilkan nama lokasi dari lokasi3.
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"*Nama lokasi 3: {nama_lokasi3}")

# 4 & 5
# 4. Masukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda:
# 5. Buat variabel terpisah untuk menyimpan jumlah hasil panen padi dan kedelai dari setiap lokasi.
hasil_padi = {}
hasil_kedelai = {}

for lokasi, data in data_panen.items():
    hasil_padi[lokasi] = data['hasil_panen']['padi']
    hasil_kedelai[lokasi] = data['hasil_panen']['kedelai']

print("*Hasil Panen Padi:", hasil_padi)
print("*Hasil Panen Kedelai:", hasil_kedelai)

# 6. Buat Percabangan Jika jumlah hasil panen padi lebih dari 1300 atau jagung lebih dari 800 di suatu lokasi, maka lokasi tersebut memerlukan perhatian khusus. Jika tidak, maka lokasi tersebut dalam kondisi baik.
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']

    if padi > 1300 or jagung > 800:
        print(f" {lokasi} memerlukan perhatian khusus.")
    else:
        print(f" {lokasi} dalam kondisi baik.")

#ilham rizky fauli
#152023220
#tugas pak diash