start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
print(f"----- Printing multiplication tables from {start} to {end} -----")
for i in range(start,end+1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()
    