list1=[]
def calc2(n1,n2):
    sum1=n1+n2
    list1.append(sum1)
    diff1=n1-n2
    list1.append(diff1)
    div1=n1/n2
    list1.append(div1)
    div2=n1//n2
    list1.append(div2)
    rem1=n1%n2
    list1.append(rem1)
    exp1=n1**n2
    list1.append(exp1)
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
calc2(n1,n2)
print("Result:",list1)