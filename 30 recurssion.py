# def factorial(n):
#      if (n==0 or n==1):
#          return 1
#      else:
#          return n * factorial(n-1)
# print(factorial(8))


def fibonacci(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

for n in range(15):
    print(fibonacci(4))
