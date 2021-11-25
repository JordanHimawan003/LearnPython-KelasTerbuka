## tipe data umum
# tipe data integer : angka satuan tanpa koma
data_integer = 11
print("Data = ", data_integer)
print("- bertipe ", type(data_integer))

# tipe data float : angka dengan koma
data_float = 1.5
print("Data = ", data_float)
print("- bertipe ", type(data_float))

# tipe data string : kumpulan karakter
data_string = "jordaaan"
print("Data = ", data_string)
print("- bertipe ", type(data_string))

# tipe data boolean = data biner, atau true false
data_bool = True
print("Data = ", data_bool)
print("- bertipe ", type(data_bool))


## tipe data khusus
# bilangan kompleks
data_complex = complex(5,6)
print("Data = ", data_complex)
print("- bertipe", type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double, c_char   #mengimpor package C
data_c_double = c_double(10.5)
print("Data = ", data_c_double)
print("- bertipe ", type(data_c_double))


#25 Nov 2021 - Python untuk persiapan LKS