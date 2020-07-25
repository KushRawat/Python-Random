def test(lis, k, value):
    if value not in lis:
        lis.reverse()
        print("Value not in list",lis)
    return

a = list(input())
b = int(input())
c = int(input())
print(test(a,b,c))
