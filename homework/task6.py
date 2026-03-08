def func(a, n):
    if n == 0:
        return 1
    else:
        return a * func(a, n - 1)

# print(func(2, 4))


def yaer(a): 
    if a % 100 != 0 and a % 4 == 0:
        return True
    return False

# print(yaer(2024))
def day(day3, month3, year3):
    days = [31, 28 , 31 , 30 , 31 , 30 ,31 , 30, 31 ,30 ,31 ,30 ]
    if yaer(year3):
        days[1] = 29
    day1 = day3
    for i in range(month3 - 1):
        day1 += days[i]
    return day1

# print(day(10, 3, 2023))


def date(d2,m2,y2, d, m, y):
    days1 = day(d2, m2, y2)
    days2 = day(d, m, y)
    ottal = days1
    for i in range(0, y2):
        if yaer(i):
            ottal += 366
        else: ottal += 365
    total1 = days2
    for i in range(0, y):
        if yaer(i):
            total1 += 366
        else: total1 += 365
    return abs(total1 - ottal)

# print(date(1,3,2024,10,3,2024))




import random
nums = [random.randint(1, 100) for _ in range(100)]

def find_min_pos(arr, i=0, min_sum=None, min_pos=0):
    if i > len(arr) - 10:
        return min_pos

    curt_sum = sum(arr[i:i+10])

    if min_sum is None or curt_sum < min_sum:
        min_sum = curt_sum
        min_pos = i

    return find_min_pos(arr, i+1, min_sum, min_pos)


pos = find_min_pos(nums)

print(nums)
print(pos)
print(sum(nums[pos:pos+10]))









