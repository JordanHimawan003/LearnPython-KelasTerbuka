# input data dari user
# data yang diterima bertipe string

# string
data = input("Masukkan datas: ")
print("Data = ", data, "bertipe ", type(data))

# jika ingin mengambil int
angka = float(input("Masukkan angka: "))
angka = int(input("Masukkan angka:"))
print("Data = ", angka, "bertipe ", type(angka))

# input boolean
binary = bool(int(input("Masukkan nilai bool: "))) # input selain angka akan error
print("Data = ", binary, "bertipe ", type(binary))


#26 Nov 2021 - Python untuk persiapan LKS