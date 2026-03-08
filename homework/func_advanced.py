def get_discounted_prices(prices: list):
    discounted_prices = []

    for price in prices:
        if price > 100:
            discounted_prices.append(price * 0.8)
    
    return discounted_prices

original_prices = [50 , 120 , 69 , 200 , 300]
result = get_discounted_prices(original_prices)
# print(result)


def recursion():
    print('recursion')
    recursion()

# def func_a():
#     print('a call b')
#     func_b()

# def func_b():
#     print('b call a')
#     func_a()

# def factorial_loop(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial_loop(5))

# def factorial_recursion(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial_recursion(n - 1)

# print(factorial_recursion(5))


def say_hello():
    print('Hello')

func_var = say_hello
# func_var()
# print(type(func_var))


def some_func(callback):
    print('some_func calls its callback')
    callback()

def log_console(message):
    pass

def log_file(message):
    pass

def log_database(message):
    pass

def do_some_work(log_callback):
    print('doing')
    print('done')
    log_callback('logging message')

# do_some_work(log_console)
# do_some_work(log_file)
# do_some_work(log_database)
# some_func(say_hello)


# sum = lambda a , b: a + b

# print(sum(10,12))

# operation = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
# }
# num1 = float(input(': '))
# num2 = float(input(': '))
# action = input('+ , - , * : ')
# if action in operation:
#     print(operation[action](num1, num2))
# else: print('no')



# tax_rate = 0.2

# def calculate_tax_impure(amount):
#     return amount * tax_rate
# print(calculate_tax_impure(10000))

# def calculate_tax_pure(amount, tax_rate):
#     return amount * tax_rate
# print(calculate_tax_pure(10000, 0.3))

# def add_product_impure(cart: list, product:str):
#     cart.append(product)
#     return cart

# def add_product_pure(cart: list, product: str):
#     new_cart = cart.copy()
#     new_cart.append(product)
#     return new_cart

# my_cart = [' apple', 'banana']
# add_product_impure(my_cart, 'orange')
# new_cart = add_product_pure(my_cart, 'orange')
# print(my_cart)
# print(new_cart)

# my_set_1 = {'apple', 'banana'}
# my_set_2 = {'pear', 'orange'}

# union = my_set_1.union(my_set_2)

# my_set_1.update(my_set_2)

# def create_multiplier(factor):
#     def multiplier(num):
#         return num * factor 
#     return multiplier

# doubler = create_multiplier(2)
# tripler = create_multiplier(3)

# print(doubler(4))
# print(tripler(10))

numberds =[10 , 5 , 43 , 67 , 8 , 90 , 99 , 100 , 122]
even_numbers = list(filter(lambda a: a % 2 == 0, numberds))

# print(even_numbers)


discounted_prices = list(map(lambda a: a * 0.8, filter (lambda a: a > 100, original_prices)))
# print(discounted_prices)

def changeupper(func):
    def inner():
        return func().upper()
    return inner 

@changeupper
def my_func():
    return 'Hello Sally!'
@changeupper
def my_func1():
    return 'Bye Sally!'

print(my_func)
print(my_func1)
