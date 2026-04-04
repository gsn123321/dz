import random
import string

name = input("Введіть базове ім'я: ")

num = random.randint(100, 9999)
variant1 = name + str(num)

separators = ['_', '.', '-']
sep = random.choice(separators)
letters = ''.join(random.choices(string.ascii_lowercase, k=3))
variant2 = name + sep + letters

prefixes = ['Pro', 'Super', 'Ultra']
prefix = random.choice(prefixes)

name_cap = name.capitalize()

digits = ''.join(random.choices(string.digits, k=2))
mixed = list(name_cap + digits)
random.shuffle(mixed)
mixed_name = ''.join(mixed)

variant3 = prefix + mixed_name

print("Згенеровані нікнейми:")
print("1 (Цифровий):", variant1)
print("2 (Літерний):", variant2)
print("3 (Елітний):", variant3)




