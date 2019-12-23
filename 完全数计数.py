import math
while True:
    try:
        n = int(input())
        count = 0
        for num in range(2, n):
            total = 1
            for i in range(2, int(math.sqrt(num)+1)):
                if num % i == 0:
                    total += i
                    total += num // i
            if total == num:
                count += 1
        print(count)
    except:
        break
