m=[]
b=input()
j=int(0)
while b!=".":
    b=b.split()
    for i in b:
        if j==0 and i=="POST":
            m.append(b[1:])
        elif (j==0 and i=="GET"):
            print(str(m[-1]))
        elif (j==0 and i=="DELETE"):
            del m[-1]
        j=j+1
    j=0
    b=input()
print(m)
