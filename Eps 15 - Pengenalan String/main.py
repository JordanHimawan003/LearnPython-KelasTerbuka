# membuat string

data = "ini adalah string"
print(data)
print(type(data))

# cara membuat string
'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabs"')
print("'Halo, apa kabs'")
print("Ini adalah hari Jum'at")

# menggunakan tanda \
# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ahmed")

# tab
print("ucup\totong, jauhan")
print("ucup\t\t\totonk, semakin jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua")    #LF - Line Feed. UNIX, MacOS, Linux
print("baris pertama.\rbaris kedua")    #CR - Carriage Return. Commodore, Acorn, Lisp
print("baris pertama.\r\nbaris kedua")  #CRLF - Line Feed Carriage Return. Windows

# string literal atau raw
print('C:\new folder')  #akan salah

#menggunakanr raw string
print(r"C:\new folder")

# multiline literal string
print("""
Nama ucuph
kelas 3 ed
""")

# multiline literal string dan raw
print(r"""
    nama ucup
    kelas 3sd \new wave
    website www.ucup.com/newID
""")