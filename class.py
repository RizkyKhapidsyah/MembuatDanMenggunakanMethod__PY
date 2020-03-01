#Class
class mahasiswa():
    nama = 'Dessy Puspita Sari'

    def belajar(self):
        print(self.nama, 'sedang Belajar')

    def makan(self):
        print(self.nama, "makan di kelas")

    def gender(self, jenis):
        print(self.nama, 'adalah seorang', jenis)



#Main Program
Mahasiswa1 = mahasiswa() #Instance = Class
Mahasiswa2 = mahasiswa()

Mahasiswa1.nama = 'Rizky Khapidsyah'

print(Mahasiswa1.nama)
print(Mahasiswa2.nama)

Mahasiswa1.belajar()
Mahasiswa2.belajar()

Mahasiswa1.makan()
Mahasiswa2.makan()

Mahasiswa1.gender("Laki-Laki")
Mahasiswa2.gender("Perempuan")
