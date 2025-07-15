k = [44,55,1,5,8,5,45]
print(k)

k.append(99)

k.sort()
print(k)

k.reverse()
print(k)

# another opton for reversing
k.sort(reverse=True)
print(k)

print(k.index(1))

print(k.count(5))

j = k.copy()
j[1] = 5

k.insert(1, 999)
print(k)

j = [455,55,888]
k.extend(j)
print(k)
n = k+j



