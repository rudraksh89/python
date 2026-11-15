f = open("textfile.txt")
data = f.read()
print(data)
f.close

j = open("myfile.txt","w")
st = "Hello how lief going"
j.write(st)
j.close()


#using with , the file is automatically closed
with open("textfile.txt") as f:
  print(f.read())