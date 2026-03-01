# def text():
#     print('\'Dont let the noise of others\' opinions\n   drown out your own inner voice.\n      Steve Jobs')
# text()

# def numbers(num1, num2):
#     for i in range(num1, num2):
#         if i % 2 != 0:
#             print(i)
# numbers(3,23)


# def line(length,direction,symbol):
#     if direction == 1:
#         print(symbol * length)
#     elif direction == 0:
#         for i in range(length):
#             print(symbol)
#     else:print('no')        
# line(3,0,"#")


# def num(a,c,b,d):
#     return max(a,c,b,d)
# print(num(1,2,3,4))


# def num(a):
#     if a <= 1:
#         return False
#     for i in range(2, a):
#         if a % i == 0:
#             return False
#     return True
# print(num(2))


def sum(a):
    num = str(a)
    sum1 = int(a[0]) + int(a[1]) + int(a[2])
    sum2 = int(a[3]) + int(a[4]) + int(a[5])
    if sum1 != sum2:
        return False
    elif sum1 == sum2:
        return True
    else:return 'ni'

print(sum(123456))




