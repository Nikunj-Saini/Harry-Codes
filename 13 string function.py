# strigns are imutable means they cannot be changed
a= "nikunj"
b = "!!!!nikunj!!!!!!!!!"
c =  "nikunj!!!!!"
d = "nikunj &&&&&&&&&&& nikunj %%%%% nikunj"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
# the strip function reomves the thing we want to remove
print(b.rstrip("!"))
print(c.rstrip("!"))
print(c.replace("nikunj","nope"))
print(d.replace("nikunj","nope"))
print("the number of time nikunj is in d is :")
print(d.count("nikunj"))
print(len(d))
print(len(d.center(50)))


nikunj = "welcome to my chanal"
print(nikunj.capitalize())
str = "hello how are you"
print(str.endswith("are",4,13))
print(str.find("are"))
# if not found it will return -1
print(str.find("aree"))
''' if we do not want to get -1 then we can use index also 
   it will end with an error'''






