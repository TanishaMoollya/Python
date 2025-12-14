fh=open("in1.txt","r")
start=int(fh.readline())
end=int(fh.readline())
print(f"----- Printing multiplication tables from {start} to {end} -----")
for i in range(start,end+1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()
    