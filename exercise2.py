f=open("num.txt")
a=f.readlines()
f.close()


b=[line.strip() for line in a]
f=open("num.txt","a")
f.writelines("\n")

count=1
for line in b:
      if count % 3 ==0:



print ((a))



print (a[1])
for x in a:
    #print(type(x),x)
    print(x.strip())
    print("---------")
    print(a)
    b=[x.strip() for x in a]
    print(b)