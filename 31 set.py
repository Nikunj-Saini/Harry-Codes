# s = {5,8,8,225,}
# print(type(s))
#
# hi = {"nikunj",48,True,5.5,48}
# print(hi)
# nikunj = {}
# print(type(nikunj))

# this is for union
# cities = {"Tokyo", "Delhi"}
# cities2 = {"Tokyo", "nikunj"}
# cities3 = cities.update(cities2)
# print(cities)


# tis is for interseiton
cities = {"Tokyo", "nikunj",}
cities2 = {"Tokyo", "Seoul",}
# cities3 = cities.intersection(cities2)
cities3 = cities.intersection_update(cities2)
print(cities)
