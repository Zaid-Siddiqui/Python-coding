def my_function():
     with open ('practical 3.txt','r') as f:
     f_contents = f.read()
     print(f_contents, end='')
     
my_function()


f=open("practical 3.txt")
a=f.readlines()
f.close()


b=[line.strip() for line in a]

f=open("practical 3.txt","a")

f.writelines("\n")

count = 1
for line in b:
    if str.upper():
        f.writelines(str.lower())
        f.writelines("\n")
    else:
        f.writelines(str.upper)
        f.writelines("\n")
    count += 1  
      
