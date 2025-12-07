def calc1(n1,n2):
    sum1=n1+n2
    diff1=n1-n2
    prd1=n1*n2
    div1=n1/n2
    div2=n1//n2
    rem1=n1%n2
    exp1=n1**n2
    return (sum1,diff1,prd1,div1,div2,rem1,exp1)
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
sum1,diff1,prd1,div1,div2,rem1,exp1=calc1(n1,n2)
print(f"Sum={sum1},Difference={diff1},Product={prd1},Float Quotient={div1},Integer Quotient={div2},Remainder={rem1},Exponential={exp1}")
