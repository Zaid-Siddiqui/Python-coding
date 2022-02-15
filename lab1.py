X = int(input("Enter your value: ")) 
print(X)

if X>=5:
     a=(((X**2)-(5*X))**0.5)
     print("Value of a :",a)
     
     b=float(X+(X**2)+1)
     print("Value of b :",b)

     if (a>=b):
         express1=((a**2)-b+a*b)
         print("Expression 1 is :",express1)
     else:
         express2=((a-(b/20))**0.5)
         print("Expression 2 is :",express2)
else :
     print("Wrong value Entered. Computation is not possible. ")
     print("Enter value greater than 4 ") 