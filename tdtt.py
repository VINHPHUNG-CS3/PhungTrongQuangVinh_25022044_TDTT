def check(x):
    flag = True
    if x < 2:
        flag = False
    for i in range (2, int(x**0.5) + 1):
        if x % i == 0:
            flag = False
            break
    return flag

a,b = map(int, input().split())

print(check(2), check(3))
