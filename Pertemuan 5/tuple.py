nama = "Zakki"
mapel = "DDP"
nilai = 80

#ket : 
#if(nilai >= 60):
#ket = "lulus"
#else
#ket = "gagal"
#tuple&list

ket = ("gagal","lulus")[nilai >=60]

print("Nama Mahassiswa\t:",nama,
"\nMata Pelajaran\t:", mapel,
"\nNilai\t\t:",nilai,
"\nKeterangan\t:", ket,
)