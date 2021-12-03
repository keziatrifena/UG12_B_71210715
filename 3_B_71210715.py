kal = str(input("Input :"))
a = len(kal)
print("Output :")

for i in range(a):
    for j in range(a-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(kal[j],end=" ")
    print()
for i in range(a):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(a-i-1):
        print(kal[j],end=" ")
    print()