# latihan konversi temperatur

# konversi celcius ke satuan lain
# print("\nPROGRAM KONVERSI TEMPERATUR\n")

# celcius = float(input("Masukkan suhu dalam Celcius: "))
# print("Suhu adalah",celcius,"Celcius")

# # reamur
# reamur = (4/5) * celcius
# print("Suhu adalah",reamur,"Reamur")

# # fahrenheit
# fahrenheit = ((9/5) * celcius) + 32
# print("Suhu adalah",fahrenheit,"Fahrenheit")

# # kelvin
# kelvin = celcius + 23
# print("Suhu adalah",kelvin,"Kelvin")

# konversi fahrenheit ke kelvin
fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
celcius = 5/9 * (fahrenheit-32)
kelvin = celcius + 273
print("Suhu",fahrenheit,"Fahrenheit =",kelvin,"Kelvin")

# konversi kelvin ke fahrenheit
k = float(input("Masukkan suhu dalam Kelvin: "))
c = k - 273
f = ((9/5) * c) + 32
print("Suhu",k,"Kelvin =",f,"Fahrenheit")


#27 Nov 2021 - Python untuk persiapan LKS