#membuat tipe data koleksi

koleksi_data_str = ["pisang","mangga","jambu","semangka"]

koleksi_data_int = [200, 300, 400, 500]

koleksi_data_mix = ["reza kecap", 100, True, "reza kecap"]

print("koleksi data string:",koleksi_data_str)

print("koleksi data integer:",koleksi_data_int)

print("koleksi data cadmpuran:",koleksi_data_mix)

nama_nama_hewan = ["semut","babi", "anjing"]

list_nilai_uts = [56,92,80,78]

nama_teman_sebangku = ["pajri" , "ilal aseli", "bandar apran", "angga UB"]

print("nama nama hewan:", nama_nama_hewan)

print("nilai uts saya", list_nilai_uts)

print("nama teman sebangku", nama_teman_sebangku)

# tampilkan data koleksi dengan indeks

# data ke 2 nama hewan 

print("nama hewan data ke-2:", nama_nama_hewan[1])

# data pertama nilai uts

print("data pertama nilai uts:", list_nilai_uts[0])

# data terakhir nama teman sebangku

print("data terakhir nama teman sebangku:", nama_teman_sebangku[3])

# tambahkan 1 data disetiap data koleksi

nama_nama_hewan.append("asep")
list_nilai_uts.append(100)
nama_teman_sebangku.append("sucipto")

# ubahlah data terakhir nilai

list_nilai_uts[-1] = 50
print(list_nilai_uts)

# ubahlah data ke-3 nama hewan

nama_nama_hewan[2] = "shiroko"
print(nama_nama_hewan)