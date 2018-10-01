myf=open("running-config.cfg")
mylist_intname=[]
for line in myf:
    line=line.strip()
    line=line.split()
if (line[0]=="interface"):
    mylist_intname.append(line[1])
print(mylist_intname)
