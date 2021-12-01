# contoh generic

# string
nama = "ucup"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"boolean {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bil bulat = {angka:d}"   # d untuk angka desimal
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"  # koma untuk memberikan koma
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"   # angka untuk mengambil jumlah angka setelah koma, f untuk tipe data float
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"    # 0 untuk menampilkan 0, 10 untuk jumlah digit, 3 untuk angka setelah koma
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+09.6f}"
print(format_minus, format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persentase = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika dalam bracket
harga = 10000
jumlah = 5
format_string = f"total = {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"
print(format_binary)
print(format_octal)
print(format_hexadecimal)