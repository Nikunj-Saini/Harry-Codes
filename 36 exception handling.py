a = int(input("enter the number whose table you want:"))
print(f"the multiplication table of {a} is :")
try:
    for i in range(1,11):
         print(f"{int(a)}X{i}= {int(a)*i}")
except:
    print("Invalid input")
print("hi")
