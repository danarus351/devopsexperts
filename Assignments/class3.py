import codecs
# assignment 1 + 2
try:
    a = 1/0
except ZeroDivisionError as zre:
    print("Zero Dicision not allowd!")

# assignment 3
# yes the code is legal

# assignment 4
# any expction that rasie


# assignment 5
# that there is no filtering between the handling of the exception

# assignment 6
# IOError read write error
# ZeroDivisionError dividing by zero

# assignment 7 + 8

file = open('dan.txt','w')
file = open('dan.txt','a')
file.write("dan\n")
file.close()

# assignment 9
file = open('dan.txt','r')
print(file.read())
file.close()

# assignment 10

file = codecs.open('dan.txt', 'a', 'utf-8')
heb = "\nדן ארוס"
file.write(heb)
file.close()
file = codecs.open('dan.txt', 'r', 'utf-8')
print(file.read())
file.close()