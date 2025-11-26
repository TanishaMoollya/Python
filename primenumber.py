list1=[]
n1=int(input("Enter the starting number:"))
n2=int(input("Enter the ending number:"))
for i in range(n1,n2):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count += 1
    if count==2:
        list1.append(i)
print(list1)


