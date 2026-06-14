num1 = int(input("Enter your first number : "))
num2 =int(input("Enter your second number : "))

action = input("Enter your action : ")

match action:
    case '+':
        print("Addition is : ", num1 + num2)

    case '-':
        print("sub is : ", num1 - num2)
    
    case '*':
        print("Multiply is : ", num1*num2)
    case _:
        print("action is not available")
        