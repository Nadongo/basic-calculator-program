def calculator():
    print("Basic Calculator\n")
    
    try:
        #Getting the user input
        num1 = float(input("Enter the first Number: "))
        num2 = float(input("Enter the second Number: "))
        operation = input("Enter an operation (+, - , *, /) : ")
        
        #performing calculation
        if operation == "+":
            result = num1 + num2
            print(f"\n{num1} + {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"\n{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 - num2
            print(f"\n{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 !=0:
                result = num1 / num2
                print(f"\n{num1} /{num2} = {result}")
            
            else:
                print("\nError: Division by zero is not allowed!!")
        else:
            print("\nInvalid Operation!! Please use +, _, * or /")
    
    except ValueError:
        print("\nError: Please enter value numbers!!")
        
calculator()