fh=open("in2.txt","r")
s=fh.readline()
lst=s.split(",")
start=int(lst[0])
end=int(lst[1])
print(f"----- Printing multiplication tables from {start} to {end} -----")
for i in range(start,end+1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()

    