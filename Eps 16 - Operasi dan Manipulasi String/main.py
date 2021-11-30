# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string
# mengecek apakah ada char atau string terentu didalam object string
d = "d"
status = d in nama_lengkap  # bersifat case sensitive
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "D"
status = d in nama_lengkap  # bersifat case sensitive
print(d + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(10*"awok")

# indexing
print("Index ke-0: " + nama_lengkap[0])
print("Index ke-6: " + nama_lengkap[6])
print("Index ke-(-1): " + nama_lengkap[-1])
print("Index ke-(-8): " + nama_lengkap[-8])
print("Index ke-[0:3]: " + nama_lengkap[0:4])
print("Index ke-[3:8]: " + nama_lengkap[3:8])
print("Index ke-[0,2,4,6,8,10]: " + nama_lengkap[0:10:2])

# item paling kecil
print("Paling kecil: " + min(nama_lengkap))
# item paling besar
print("Paling besar: " + max(nama_lengkap))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))