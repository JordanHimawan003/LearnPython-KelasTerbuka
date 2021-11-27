# not, or, and, xor

# NOT
print("=====NOT")
a = False
c = not a
print("Data a =", a)
print("Data c =", c)

# OR (jika salah satu true, maka hasilnya adalah true)
print("=====OR")
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)
a = True
b = False
c = a or b
print(a," OR",b,"=",c)
a = False
b = True
c = a or b
print(a,"OR",b," =",c)
a = True
b = True
c = a or b
print(a," OR",b," =",c)

# AND (jika semua true, maka bernilai true)
print("=====AND")
a = False
b = False
c = a and b
print(a,"AND",b,"=",c)
a = True
b = False
c = a and b
print(a," AND",b,"=",c)
a = False
b = True
c = a and b
print(a,"AND",b," =",c)
a = True
b = True
c = a and b
print(a," AND",b," =",c)

# XOR (bernilai true jika salah satu true)
print("=====XOR")
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=",c)
a = True
b = False
c = a ^ b
print(a," XOR",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"XOR",b," =",c)
a = True
b = True
c = a ^ b
print(a," XOR",b," =",c)

