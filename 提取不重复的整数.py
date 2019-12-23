a = input()
new = ''
for i in range(len(a)-1, -1, -1):
    if a[i] not in new:
        new = new + a[i]
print(new)
