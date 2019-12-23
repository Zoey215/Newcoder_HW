def gcd1(i, j):
    while j:
        i, j = j, i % j
    return i


def lcm1(m, n):
    return m * n // gcd1(m, n)


while True:
    try:
        a, b = map(int, input().split())
        print(lcm1(a, b))
    except:
        break
