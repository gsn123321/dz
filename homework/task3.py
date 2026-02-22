# nums = list(map(int, input("через пробіл: ").split()))
# nums1 = set(nums)
# print(nums1)

# import random
# set = {random.randint(1, 20) for _ in range(10)}
# set1 = {random.randint(1, 20) for _ in range(10)}
# print(set)
# print(set1)
# print(set & set1)
# print(set - set1)
# print(set | set1)

word = input("слово: ")
word1 = input("ckjddj: ")
if set(word) == set(word1):
    print('yeah')
else:
    print('no')