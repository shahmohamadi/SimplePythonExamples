# basic read/write methods for files
my_file = open('Sample.txt', 'r')
data = my_file.read()
print(data)

# data2 = my_file.readline() # uncomment for reading line by line
# print(data2)

# data3 = my_file.readlines() # uncomment for returning a list containing the lines
# i = 0
# for line in data3:
#     i = i + 1
#     print('line ', i, 'is ', line)

# my_file = open('Sample.txt', 'w') # uncomment for write in Sample file
# my_file.write('look I can write here!\n')
# my_file.write('and still writing\n')

# return position of cursor in file
print(my_file.tell())

# set position to specific place
my_file.seek(28)
print(my_file.readline())

my_file.close()

