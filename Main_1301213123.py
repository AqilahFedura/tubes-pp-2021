'''
Nama : Aqilah Fedura Ilahi
Nim : 1301213123
Kelas : IF-45-12
Nomor dan judul tubes : 8. AYO UJIAN
'''
# Point a : buat dict_kehadiran : key -> NIM , val -> jmlh_kehadiran_mhs
data_kehadiran = dict()

with open("data_kehadiran.txt", "r") as data : # untuk membuka dan menutup file secara langsung.
	
	data_mentah = data.readlines() # isi file di baca baris per baris dan didikan sebuah list.
	
	
	 # tahap cleaning ke 1
	for i in data_mentah:     
		data_process = i.split('\t')  # proses cleaning untuk menghilangkan \t
		
	    
		# tahap cleaning ke 2                                                                                                      
		nim = data_process[0] # variabel baru berupa nim dengan value = data_process[0] -> indeks 0 adalah nim mhs                                      
		jumlah_kehadiran_mentah = ' '.join(data_process[1:]).split() # proses cleaning kedua menggunakan method join() untuk menghilangkan \n
	                                                                 # menthod join() mengubah list -> string
																	 # buat method split() untuk mengubahnya kembali menjadi sebuah list                     
		
		jumlah_kehadiran = 0
        
		for jumlah in jumlah_kehadiran_mentah : # lakukan perulangan untuk mengubah isi data yang awalnya list -> integer  
			jumlah_kehadiran += int(jumlah)     # kenapa diubah jadi integer ? agar nanti bisa menghitung presentase kehadiran mhs.
			
		data_kehadiran[nim] = jumlah_kehadiran # buat dict dengan key -> nim dan value -> jumlah kehadiran mhs.
		

# point b : buat fungsi report = buat nampilin mhs yang boleh ikut ujian/tidak boleh ikut ujian.
# catatan : mhs yang boleh ikut ujian : jumlah kehadiran > 75
# jumlah_minggu = 7
# rumus = (jumlah kehadiran mhs/ jumlah minggu)*100

def report() : # fungsi report
	mhs_boleh_ujian = []   # ini berisi list mhs yang boleh ujian.
	mhs_gaboleh_ujian = [] # ini berisi list mhs yang gaboleh ujian.
	total_minggu = 7
	presentase_kehadiran_minimal = 75 # ini dari soal.

	for k_nim, v_jml_kehadiran_mhs in data_kehadiran.items(): # buat pertulangan untuk key dan valuenya.
		                                                      # disini data_kehadiran menggunakan method items().
															  # karena data_kehadiran berupa dict dan method items() dipakai saat perulangan.
		presentase_kehadiran_mhs = (v_jml_kehadiran_mhs/total_minggu) * 100 # rumus untuk menghitung persentase kehadiran mhs
		if presentase_kehadiran_mhs < presentase_kehadiran_minimal:         # pengkondisian untuk menentukan apakah presentase kehadiran mhs < 75 atau sebaliknya.
			mhs_gaboleh_ujian.append(k_nim) # jika presentase < 75, maka akan masuk kedalam list mhs_gaboleh_ujian.
			                                # disini ada method append() yang gunanya untuk menambahkan suatu nilai ke sebuah list.
		
		else :                              # jika presentase > 75, maka akan masuk kedalam list mhs_boleh_ujian.
			                                # penjelasan sama seperti yang diata.s
			mhs_boleh_ujian.append(k_nim)

	
	print("menampilkan report : ") 
	print("=="*24)                 # print("=="*24) hanya sebagai penghias.
	print("Mahasiswa yang boleh mengikuti ujian : ")
	for mhs_1 in mhs_boleh_ujian:
		print(mhs_1)              # untuk menampilkan nim-nim mhs yang boleh mengikuti ujian.
	print()                       # print() untuk merapikan saja.
	print("Mahasiswa yang tidak boleh mengikuti ujian : ")
	for mhs_0 in mhs_gaboleh_ujian:
		print(mhs_0)             # untuk menampilkan nim-nim mhs yang tidak boleh mengikuti ujian.
	print()
	print("=="*24)

# point c = buat fungsi top buat nampilin mhs yang paling termalas.
def top(): # buat fungsi top.
	print(dict(sorted(data_kehadiran.items(), key=lambda kehadiran: kehadiran[1], reverse=False))) #untuk menampilkan dict mhs berdasarkan jumlah kehadiran yang paling sedikit
	print()
	urutan_mhs_termalas = dict(sorted(data_kehadiran.items(), key=lambda kehadiran: kehadiran[1], reverse=False))
	                      # menggunakan function sorted untuk mengurutkan iterable secara naik/turun.
						  # sorted(iterable, key=fuction, reverse = true/false)
						  # lambda -> anonymous function yang berfungsi jika ingin membuat suatu ekspresi -> kehadiran [1]
						  # reverse -> optional, fungsinya untuk mengurutkan iterable secara naik/turun.

	print("Mahasiswa paling termalas :  ")
	for k_mhs, v in urutan_mhs_termalas.items():
		print(k_mhs) # untuk menampilkan mhs yang paling pemalas sampai terajin.

# point d : membuat main program.
def main (): # buat fungsi main.
	report()
	top()
main()
 # untuk memanggil fungsi-fungsi yang sudah dibuat.
