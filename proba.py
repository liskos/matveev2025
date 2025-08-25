def func(x):
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        if x % 12 != 0:
            b = b * (x % 12)
        x = x // 12
    return a, b
k = 0
for i in range(1, 1000000):
    a, b = func(i)
    if a == 2 and b == 12:
        k += 1
print(k)