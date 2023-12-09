import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.
# Pertanyaan 2:
# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.
persentase_bonus = 0.05  # Mengubah bonus_persen menjadi 0.05 untuk mewakili 5%
bonus = lambda gaji: persentase_bonus * gaji

for index, row in df.iterrows():
    gaji = row['Gaji']
    tambahan_bonus = bonus(gaji)
    df.at[index, 'Gaji_Setelah_Peningkatan'] = gaji + tambahan_bonus

print(df)

# Pertanyaan 3:
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.
df['Gaji_Diatas_30th'] = df['Gaji']

for index, row in df.iterrows():
    gaji = row['Gaji']
    if row['Usia'] > 30:
        df.at[index, 'Gaji_Diatas_30th'] = gaji * 1.02

# Pertanyaan 4:
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

print("=========Seluruh DataFrame yang Telah Diperbaharui=========")
print(df)

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.