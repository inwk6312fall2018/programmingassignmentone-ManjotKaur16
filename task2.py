a=172
b=192
c=10

def new_config(file):
    d=[]    
    fin=open(file)
    for line in fin:
        line=line.strip()
        for word in line.split():
            d.append(word)
    for word in d:
        if word==a:     #comapre the word with a
            word=word.replace(a,z) #replace a by z
        elif word == b:
            word=word.replace(y,z)

new_config("running-config.cfg")
