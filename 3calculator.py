def add(x,y):
    return x+y
def subtract(x,y):
    if x>y:
        return x-y
    else:
        return y-x
def multiply(x,y):
    return x*y
def divide(x,y):
    try:
        return x/y
    except:
        print("An exception occurred : Cannot divide by zero")
print("\n\t    CALCULATOR")
print("\t CHOOSE A OPERATOR")
print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.EXIT")
while True:
    x=float(input("Enter the 1st num:"))
    y=float(input("Enter the 2nd num:"))
    choice=int(input("Enter your choice:"))
    if choice==1:
        result=add(x,y)
        print(f"{x}+{y}={result}")
    elif choice==2:
        result=subtract(x,y)
        print(f"{x}-{y}={result}")
    elif choice==3:
        result=multiply(x,y)
        print(f"{x}*{y}={result}")
    elif choice==4:
        result=divide(x,y)
        print(f"{x}/{y}={result}")
    elif choice==5:
        print("Exiting goodbyeee....")
        break
    else:
        print("Invalid Choice!! Please choose between 1-5")
    
    
        
