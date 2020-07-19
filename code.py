#program to read the upper and lower limt
h = []

a = int(input())
b = int(input())

for x in range(a, b+1):
    if (x % 7 == 0) and (x % 5 == 0):
        h.append(str(x))

print(h)
print(','.join(h))
print(type(x))
print(type(h))        
