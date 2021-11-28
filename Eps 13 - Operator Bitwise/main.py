# melakukan operasi bitwise

a = 9
b = 5

# bitwise OR (|)
c = a | b
print("\n=====OR=====")
print("Nilai: ",a,", binary: ",format(a, '08b')) #format() berfungsi untuk mengubah format suatu value
print("Nilai: ",b,", binary: ",format(b, '08b'))
print("------------------------------ (|)")
print("Nilai: ",c,", binary: ",format(c, '08b'))

# bitwise AND (&)
c = a & b
print("\n=====AND=====")
print("Nilai: ",a,", binary: ",format(a, '08b'))
print("Nilai: ",b,", binary: ",format(b, '08b'))
print("------------------------------ (&)")
print("Nilai: ",c,", binary: ",format(c, '08b'))

# bitwise XOR (^)
c = a ^ b
print("\n=====XOR=====")
print("Nilai: ",a,", binary: ",format(a, '08b'))
print("Nilai: ",b,", binary: ",format(b, '08b'))
print("------------------------------ (^)")
print("Nilai: ",c,", binary: ",format(c, '08b'))

# bitwise NOT (~)
c = ~a
print("\n=====NOT=====")
print("Nilai: ",a,", binary: ",format(a, '08b'))
print("------------------------------ (~)")
print("Nilai: ",c,", binary: ",format(c, '08b'))

# shifting
# shift right
c = a >> 2
print("\n=====SHIFT RIGHT=====")
print("Nilai: ",a,", binary: ",format(a, '08b'))
print("------------------------------ (>>)")
print("Nilai: ",c,", binary: ",format(c, '08b'))

# shift left
c = a << 1
print("\n=====SHIFT LEFT=====")
print("Nilai: ",a,", binary: ",format(a, '08b'))
print("------------------------------ (<<)")
print("Nilai: ",c,", binary: ",format(c, '08b'))