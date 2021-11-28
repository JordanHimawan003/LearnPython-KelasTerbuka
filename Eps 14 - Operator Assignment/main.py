# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

# aritmatika
a = 5   # adalah assignment
print("Nilai a =",a)

a += 1  # artinya adalah a = a + 1
print("Nilai a += 1, nilai a menjadi",a)

a -= 2  # artinya adalah a = a - 1
print("Nilai a -= 2, nilai a menjadi",a)

a *= 5  # artinya adalah a = a * 1
print("Nilai a *= 5, nilai a menjadi",a)

a /= 2  # artinya adalah a = a / 1
print("Nilai a /= 2, nilai a menjadi",a)

# modulo dan floor division
b = 10
print("\nNilai b =",b)

b %= 3
print("Nilai b %= 3, nilai b menjadi",b)

b = 10
b //= 3
print("Nilai b //= 3, nilai b menjadi",b)

# pangkat atau eksponen
a = 5
print("\nNilai a =", a)

a **= 3
print("Nilai a **= 3, nilai a menjadi",a)

# operasi bitwise
# OR
c = True
print("\nNilai c =",c)
c |= False
print("Nilai c |= False, nilai c menjadi",c)
c = False
print("\nNilai c =",c)
c |= False
print("Nilai c |= False, nilai c menjadi",c)

# AND
c = True
print("\nNilai c =",c)
c &= False
print("Nilai c &= False, nilai c menjadi",c)
c = True
print("\nNilai c =",c)
c &= True
print("Nilai c &= True, nilai c menjadi",c)

# XOR
c = True
print("\nNilai c =",c)
c ^= False
print("Nilai c ^= False, nilai c menjadi",c)
c = True
print("\nNilai c =",c)
c ^= True
print("Nilai c ^= True, nilai c menjadi",c)

# shifting
d = 0b0100
print("\nNilai d =",format(d,'04b'))
d >>= 2
print("Nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 1
print("Nilai d <<= 1, nilai d menjadi",format(d,'04b'))