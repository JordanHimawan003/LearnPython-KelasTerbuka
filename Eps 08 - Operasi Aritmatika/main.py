# operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a, "+", b, "=", hasil)

# operasi kurang -
hasil = a - b
print(a, "-", b, "=", hasil)

# operasi kali *
hasil = a * b
print(a, "*", b, "=", hasil)

# operasi bagi /
hasil = a / b
print(a, "/", b, "=", hasil)

# operasi eskponen **
hasil = a ** b
print(a, "**", b, "=", hasil)

# operasi modulus %
hasil = a % b
print(a, "%", b, "=", hasil)

# operasi floor division //
hasil = a // b
print(a, "//", b, "=", hasil)

# priority precedence
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)

hasil = x ** y * (z + x) / y - y % z // x   # bracket akan diprioritaskan
print(x, "**", y, "*", "(", z, "+", x, ")", "/", y, "-", y, "%", z, "//", x, "=", hasil)


#26 Nov 2021 - Python untuk persiapan LKS