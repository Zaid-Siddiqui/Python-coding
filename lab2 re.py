
def last_string_letters(string):
    last_string_dict={}
    j=1
    for i in string[len(string)-1]:
        last_string_dict[j]=i
        j=j+1
    return last_string_dict

   
list=[]
dict={}
number=[]
string=[]
j=1
list.extend([5.99,6.7,9,"Hello",77,89.99,2.4,4.7,3.2])

for i in list:
    if(not isinstance(i,str)):
        number.append(i)
    else:
        string.append(i)
number.sort() 
sum=number[0]+number[1]+number[2]+number[3]
print("average of 4 smallest numbers: ",sum/4) 
dict=last_string_letters(string)
print(dict)