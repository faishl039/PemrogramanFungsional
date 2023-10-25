def konversi_menit(minggu=0, hari=0, jam=0, menit=0):
    total_menit = ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)
    return total_menit

data = ["3 minggu 2 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
output_data = []

for data_item in data:
    data_split = data_item.split()
    minggu = int(data_split[0])
    hari = int(data_split[2])
    jam = int(data_split[4])
    menit = int(data_split[6])
    hasil_konversi = konversi_menit(minggu, hari, jam, menit)
    nilai_integer = list(filter(str.isdigit, data_split))
    output_data.append(hasil_konversi)

print("outputData =", output_data)