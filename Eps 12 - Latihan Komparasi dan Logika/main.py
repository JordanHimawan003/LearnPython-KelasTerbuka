# latihan komparasi dan logika

# +++++3-----10+++++
inputUser = float(input("Masukkan angka\nkurang dari 3\natau\nlebih dari 10: "))
isKurangDari = inputUser < 3 
print("Kurang dari 3 =",isKurangDari)

isLebihDari =  inputUser > 10
print("Lebih dari 10 =",isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ",isCorrect)
print("\n",10*"=","\n")

# -----3+++++10-----
inputUser = float(input("Masukkan angka\nlebih dari 3\ndan\nkurang dari 10: "))
isLebihDari = inputUser > 3 
print("Kurang dari 3 =",isLebihDari)

isKurangDari =  inputUser < 10
print("Lebih dari 10 =",isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan: ",isCorrect)
print("\n",10*"=","\n")

# -----0+++++5-----8+++++11-----
inputUser = float(input("Masukkan angka\nlebih dari 0\ndan\nkurang dari 5: "))
isLebihDari = inputUser > 0
isKurangDari = inputUser < 5
irisanSatu = isLebihDari and isKurangDari
print("Angka yang anda masukkan: ",irisanSatu)

inputUser = float(input("Masukkan angka\nlebih dari 8\ndan\nkurang dari 11: "))
isLebihDari = inputUser > 8
isKurangDari = inputUser < 11
irisanDua = isLebihDari and isKurangDari
print("Angka yang anda masukkan: ",irisanDua)

irisanGabungan = irisanSatu and irisanDua
print("\nAngka yang anda masukkan: ",irisanGabungan)

# +++++0-----5+++++8-----11+++++
inputUser = float(input("Masukkan angka kurang dari 0: "))
isKurangDariNol = inputUser < 0
print("Angka yang anda masukkan: ",isKurangDariNol)

inputUser = float(input("\nMasukkan angka\nlebih dari 5\ndan\nkurang dari 8: "))
isLebihDari = inputUser > 5
isKurangDari = inputUser < 8
irisan = isLebihDari and isKurangDari
print("Angka yang anda masukkan: ",irisan)

inputUser = float(input("\nMasukkan angka lebih dari 11: "))
isLebihDariSebelas = inputUser > 11
print("Angka yang anda masukkan: ",isLebihDariSebelas)

gabungan = isKurangDariNol and irisan and isLebihDariSebelas
print("\nAngka yang anda masukkan: ",gabungan)