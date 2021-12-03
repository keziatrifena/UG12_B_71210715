n = int(input("Input : "))

for s in range(n):
    for i in range(n):
        if i==(n-1) or s==(n-1) or i+s+1==n:
            print("*",end=" ")
        else:
            print(end="  ")
    print()

#i=tegak 
#s=tidur