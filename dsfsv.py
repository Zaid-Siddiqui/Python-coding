f = open("test.txt")
a = f.readlines()
f.close()

b = [line.strip() for line in a] # removing new lines \n

f = open("CapitalLines.txt", "a")
f.writelines("\n") # A blank line to separate original text from appended text

count = 1 
for line in a:
    if count % 3 == 0:
        f.writelines(line.upper()) # making every third line in capital case
        f.writelines("\n")
    else:
        f.writelines(line)
        f.writelines("\n")
    count += 1