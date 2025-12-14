f1=open("out1.txt","w")
f2=open("in2.txt","r")
s=f2.readline()
lst=s.split(",")
start=int(lst[0])
end=int(lst[1])
print(f"----- Printing multiplication tables from {start} to {end} -----")
for i in range(start,end+1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
        f1.write(str(i)+"*"+str(j)+"="+str(i*j))
        f1.write("\n")
    print()
    f1.write("\n")
f2.close()
    