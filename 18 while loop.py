# i = 0
# while (i<=3):
#     print(i)
#     i = i+1
# print("done with the loop")

# got a new glitch
# n = int(input("enter a number "))
# while(n<=99):
#     print(n)
# print("you won congo to you ")
answer = 40
i = int(input("choose a number between 1 - 50: "))
while(i<1 or i>50):
    print("please enter a valid input")
i = int(input("enter a number: "))
while i!=answer:
    if i<answer:
        print("too low ")
    else:
        print("too high ")
    i = int(input("enter a number: "))
    while (i < 1 or i > 50):
            print("please enter a valid input")
            i = int(input("enter a number: "))
    print("congratulation ")






