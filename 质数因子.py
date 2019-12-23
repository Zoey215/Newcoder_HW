data = int(input())
nums = []
for i in range(2, data//2 + 1):
    while data % i == 0:
        nums.append(i)
        data = data/i
if nums:
    print(' '.join(map(str, nums))+' ')
else:
    print(str(data)+' ')

