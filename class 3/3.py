from datetime import  datetime
my_file = open("newpy.txt", mode= 'a')
my_file.write(f"izackush : {datetime.now()}\n")


my_file.close()
with open('newpy.txt', 'r') as f:
    for line in f:
        print(line)
my_file.close()
