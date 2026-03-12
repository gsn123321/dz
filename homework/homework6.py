# def num(a, b):
#     if b == 0:
#         return a
#     else: return num(b, a % b)
# print(num(18, 12))


# def num(a):
#     a1 = str(a)
#     c = int(a1[0])
#     v = int(a1[1])
#     b = int(a1[2])
#     return c + v + b
# print(num(123))





def num(list, left, right):
    if left >= right:
        return True
    elif list[left] != list[right]:
        return False
    return num(list, left + 1, right - 1)
numbers = [1, 2, 3, 2, 1]
print(num(numbers, 0, 4))







