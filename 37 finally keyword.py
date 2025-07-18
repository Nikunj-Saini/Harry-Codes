# try:
#     l = [1,5,6,7]
#     i = int(input("enter the index"))
#     print(l[i])
#
# except:
#     print("something went wrong")
# finally:
#     print(" i am always with you ")

def function1():
    try:
        l = [1,5,6,7]
        i = int(input("enter the index"))
        print(l[i])
        return 1

 except:
    print(  "something went wrong")
    return 0
finally:
    print(" i am always with you ")
    x = function1()
    print(x)