# operasi komparasi untuk membandingkan 
# output dari komparasi adalah boolean

# operator komparasi
# >, <, >=, <=, ==, !=, is, is not

# is dan is not hanya bisa digunakan untuk membandingkan object
# is dan is not tidak bisa digunakan untuk membandingkan object dengan literal

print("===== is")
x = 5 # ini adalah assignment membuat object
y = 5
print("Nilai x =",x,"id =",hex(id(x)))
print("Nilai y =",y,"id =",hex(id(y)))
hasil = x is y
print("x is y =", hasil)
# setiap object yang dideklarasikan akan disimpan dalam memory yang memiliki address (id)
# python akan menyimpan object di memory yang sama, apabila value yang dimiliki object sama
# dalam case diatas object x dan y memiliki value yg sama yaitu 5
# cara kerja is adalah dengan membandingkan address yang dimiliki oleh dua object
# apabila addres dua object sama, maka akan bernilai true. apabila beda, maka akan bernilai false

print("===== is not")
x = 5 # ini adalah assignment membuat object
y = 5
print("Nilai x =",x,"id =",hex(id(x)))
print("Nilai y =",y,"id =",hex(id(y)))
hasil = x is not y
print("x is y =", hasil)
# is not adalah kebalikan dari is
# apabila address dua object sama, maka bernilai false


#27 Nov 2021 - Python untuk persiapan LKS