# casting adalah merubah tipe data ke tipe lain

## integer
print("===INTEGER===")
data_int = 9
print("Data = ", data_int, "bertipe ", type(data_int))

data_float = float(data_int)
data_string = str(data_int)
data_bool = bool(data_int) # false jika nilai int = 0
print("Data = ", data_float, "bertipe ", type(data_float))
print("Data = ", data_string, "bertipe ", type(data_string))
print("Data = ", data_bool, "bertipe ", type(data_bool))

## float
print("===FLOAT===")
data_float = 9.8
print("Data = ", data_float, "bertipe ", type(data_float))

data_int = int(data_float) # akan dibulatkan ke bawah
data_string = str(data_float)
data_bool = bool(data_float) # false jika nilai int = 0
print("Data = ", data_int, "bertipe ", type(data_int))
print("Data = ", data_string, "bertipe ", type(data_string))
print("Data = ", data_bool, "bertipe ", type(data_bool))

## boolean
print("===BOOLEAN===")
data_bool = False;
print("Data = ", data_bool, "bertipe ", type(data_bool))

data_int = int(data_bool)
data_string = str(data_bool)
data_float = float(data_bool) # false jika nilai int = 0
print("Data = ", data_int, "bertipe ", type(data_int))
print("Data = ", data_string, "bertipe ", type(data_string))
print("Data = ", data_float, "bertipe ", type(data_float))

## string
print("===STRING===")
data_string = "10"
print("Data = ", data_string, "bertipe ", type(data_string))

data_int = int(data_string) # string harus berupa angka
data_float = float(data_string) # string harus berupa angka
data_bool = bool(data_string) # false jika string kosong
print("Data = ", data_int, "bertipe ", type(data_int))
print("Data = ", data_float, "bertipe ", type(data_float))
print("Data = ", data_bool, "bertipe ", type(data_bool))


#26 Nov 2021 - Python untuk persiapan LKS