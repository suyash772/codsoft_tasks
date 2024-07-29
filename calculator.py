import math
print()
print("********** TASK 1= Degine a Calculator with basic arithmetic operations  *********")
print()
print("*"*200)
print("                                                 ~~~~~~~~~~~~~~~~~~~~MINI CALCULATOR~~~~~~~~~~~~~~~~~~                              ")
print("*"*200)
print()

num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
print()
print("*"*200)
print()

print("press 1 for ADDITION \npress 2 for SUBSTRACTION \npress 3 for MULTIPLICATION \npress 4 for DIVISION \npress 5 for POWER"
      " \npress 6 for SQURE_ROOT \npress 7 for factorial")
print()
print("*"*200)
print()

choice= int(input("Enter your choice from 1 to 8: "))
print()
print("*"*200)
print()

if choice==1:
    print("ADDITION of this numbers is:",num1+num2)

elif choice==2:
    print("SUBSTRACTION of this number is:",num1-num2)

elif choice==3:
    print("MULTIPLICATION of this numbers is:",num1*num2)

elif choice==4:
    print("DIVISION of this numbers is:",num1/num2)

elif choice==5:
    x=float(input("Enter a number: "))
    y=float(input("Enter another number: "))
    print("POWER of number is:",(x**y))

elif choice==6:
    int = float(input("Enter the number: "))
    print("SQUARE ROOT of this numbers is:",math.sqrt(int))

elif choice==7:
    num = int(input("Enter the number: "))
    print("factorial of this numbers is:",math.factorial(num))

else:
    print("Invalid choice")

print()
print("*"*200)
print("                                             ~~~~~~~~~~~~~~~~~THANNK YOU~~~~~~~~~~~~~~~~~~~                                             ")
print("*"*200)