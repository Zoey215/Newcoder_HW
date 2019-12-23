n = int(input())
d = {}
for i in range(n):
    line = input().split()
    if int(line[0]) in d.keys():
        d[int(line[0])] = d[int(line[0])]+int(line[1])
    else:
        d[int(line[0])] = int(line[1])
for i in sorted(d.keys()):
    print(i, d[i])



