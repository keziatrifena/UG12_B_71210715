count=0
hasil=0
output = ""
bil= int(input("Masukkan banyak bilangan: "))
while count <int(bil):
    count = count+1
    n = count
    if count%7==0:
        n = 0 
    elif count%3==0:
        n = count * - 1 
    hasil = hasil + n
    if n>1 or n==0:
        output +=" + " + str(n)
    else:
       output += " " + str(n) 
print(output)
print("Hasil perhitungan diatas ialah", hasil)
