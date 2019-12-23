s = input()
a = []
for i in s:
    if ord(i) in range(128) and i not in a:
        a.append(i)
print(len(a))


