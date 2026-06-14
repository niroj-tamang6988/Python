a =  int(input("Enter your age "))
print("Your age is: ", a)

if(a>18):
    print("You can vote")
else:
    print("You cannot vote")

    #checking string
a =input("enter first name : ")
b =input("enter second name : ")

if(a==b):
    print("Both are same")
else:
    print("Both are not same")

    #negative/positive

    a = int(input("Enter your number : "))
    if(a>0):
        print("number is positve")
    elif(a==0):
        print("number is zero")
    else:
        print("number is negative")


#nested loop


a= int(input("Enter your number : "))

if(a<0):
    print("Number is negative")
elif(a>0):
    if(a <=10):
        print("Number is between 1-10")
    elif(a >10 and a <=20):
        print("Number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("Number is zerotime.py")
