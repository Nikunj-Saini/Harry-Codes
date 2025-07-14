# def average(a = 9, b = 1):
#     print("the average is ", (a+b)/2)
# average(b = ll8)
# print(average)

def average(*number):
    sum = 0
    for i in number:
        sum=sum +1
    print("average is:",sum / len(number)
average(5, 6, 7, 1)