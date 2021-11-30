# operasi string dengan built in method

## merubah case dari string
salam = "bro!"
print("Normal = " + salam)
upper = salam.upper()
print("Upper = " + salam)

alay ="aKu KeCe AbIeZzZZZZzzzZ"
print("Normal = " + alay)
lower = alay.lower()
print("Lower = " + lower)

## pengecekan dengan isX method
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lowercase = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is uppercase = " + str(apakah_upper))

# isalpha() - untuk mengecek semua huruf
# isalnum() -  untuk mengecek alphanumeric
# isdecimal() - numeric
# isspace() - spasi, tab, dan newline
# istitle() - semua kata dimulai kapital

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()     # output boolean
print(judul + " is title = " + str(cek_judul))

## pengecekan komponen startswith() dan endswith() - case sensitive 
cek_start = "Parkjisung Oppa".startswith("Parkjisung")
print("Start = " + str(cek_start))

cek_end = "Parkjisung Oppak".endswith("Oppak")
print("End = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ' '.join(pisah)
print(pisah)
print(gabungan)

##alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(10,":")
print("'" + tengah + "'")

# kebalikannya strip()
tengah = tengah.strip(":")      # menghilangkan tanda :
print("'" + tengah + "'")

