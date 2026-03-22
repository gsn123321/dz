# try:
#     number = float(input('Enter  number: '))
# except ValueError:
#     print('Unknown exception')
# except Exception:
#     print('Incorrect value')


file_path = "test.txt"

# file = open(file_path, "r")

# file.close()

# with open(file_path, 'a') as f:
#     print("File created successfully!")



# with open("new_file.txt", 'r') as file:
#     all_text = file.read(10)
#     print(all_text)

# with open("new_file.txt", 'r') as file:
#     print(file.readline().strip())
#     print(file.readline().strip())

# with open("new_file.txt", 'r') as file:
#     for line in file:
#         print(line.strip())

# with open("new_file.txt", 'r') as file:
#     lines = file.readlines()
#     print(lines)


file_path = "new_file.txt"

# with open(file_path,'a') as file:
#     file.write("\nhello, tis is line written by code!")


try:
    with open(file_path, 'x'):
        print('File created successfully')
except FileExistsError:
    print('File already exists!')






