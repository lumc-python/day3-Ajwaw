DNA_sequence=open("challenge.fa","r")
g=c=a=t=0
DNA_sequence.readline()
for line in DNA_sequence:
    line=line.lower()
    for char in line:
        if char=="g":
            g+=1
        if char=="c":
            c+=1
        if char=="a":
            a+=1
        if char=="t":
            t+=1
print("the number of the g's in the gene is:" + str(g))
print("the number of the c's in the gene is:" + str(c))
print("the number of the t's in the gene is:" + str(t))
print("the number of the a's in the gene is:" + str(a))
gc_percentage=(g+c)/(g+c+a+t)*100

print("the gc% in the DNA_sequence is:" + str(gc_percentage)+"%")




        






        
        











    






    







