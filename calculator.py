# SIMPLE CALCULATOR
# ADDITION,SUBSRACTION
# MULTIPLICATION,DIVISION
#MODULO DIVISION
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
op=input("Enter operation: ")
if op=="+":
    print(f"Addition:{a+b}")
elif op=="-":
    print(f"Substraction:{a-b}")
elif op=="*":
    print(f"Multiplication:{a*b}")
elif op=="/":
    if b!=0:
       print(f"Division:{a/b}")
    else:
        print("cannot divide by zero")
elif op=="%":
    print(f"Modulo division:{a%b}")
else:
    print("Invalid operator")