a = [] 
b = [] 
c = 0
d = 0
stp = " "


while(stp.upper!= "STOP"):
    nama = str(input("Masukkan nama : "))
    if(nama == "STOP"):
        stp = "STOP"
        break

    else:
        n = int(input("Masukkan nomor kursi "+ nama + " : "))
        
        if(len(b)==0):
            a.insert(d,nama)
            b.insert(d,n)
            d = d + 1

        else:
            for i in range(len(b)):
                if(b[i] == n):
                    lihat = 0
                    break
                else:
                    lihat = 1
            
            if(lihat==1):
                a.insert(d,nama)
                b.insert(d,n)
                d = d + 1
            else:
                print("Mohon maaf kursi tersebut telah terisi!")

print()
print("List kursi yang telah terisi: ")

for i in range (d):
    print("Kursi nomor " + str(b[i]) + " telah diisi oleh " + str(a[i]))