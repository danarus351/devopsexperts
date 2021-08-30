my_file = open("newpy.txt", mode='r')
file_read = my_file.readlines()
for line in file_read:
    print(line)
my_file.close()