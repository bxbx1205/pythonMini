print("welcome to calc enter choice 1 for addition 2 for subtraction 3 for multiply 4 fordivide 5 for power")
choice = input()

if choice=="1":
    print("enter value for a")
    a = int(input())
    print("enter value for b")
    b = int(input())
    print(f"Result is {a+b}")
    
elif choice=="2":
    print("enter value a")
    a = int(input())
    print("enter value b")
    b = int(input())
    print(f"tera javab {a-b}")
    
elif choice=="3":
    a = int(input())
    b = int(input())
    print(f"{a*b}")

elif choice=="4":
    a = int(input())
    b = int(input())
    print(f"{a/b}")
    
elif choice=="5":
    a = int(input())
    b = int(input())
    print(f"{a**b}")
else:
    print("andha hai kya")