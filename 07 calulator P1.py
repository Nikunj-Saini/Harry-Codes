# program for calculator
print("                                MINI---CALCULATOR")
num1 = float(input("enter your first number here:"))
num2 = float(input("enter your second number here:"))
print("  1:ADD \n  2:SUB\n  3:MUL\n  4:DIV")
choice = int(input("enter your choice "))
if choice ==1:
 print(num1 +num2)
elif choice ==2:
 print(num1-num2)
elif choice==3:
 print(num1*num2)
elif choice==4:
 print(num1/num2)
else:
 print("invalid input")









