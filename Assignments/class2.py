# assignment A
x = 6
y = 9
if x > y:
    print("BIG")
else:
    print('small')

# assignment B
for i in range(5):
    print(i)

# assignment C
season = input("enter number btween 1-4 :")
if season == '1':
    print('Summer')
elif season == '2':
    print('Winter')
elif season == '3':
    print('Fall')
elif season == '4':
    print('Spring')
else:
    print(" The number is not btween 1-4, Goodbye!")

# assignment D
# The loop will run 10 times

# assignment E
age = 25
FirstLetter = 'D'
ShekelDollar = 3.22
abroad = False
ApNum = 5

print(f'this is my age: {age}\n'
      f'This is the first letter of my name: {FirstLetter}\n'
      f'this is the shekel dollar currency: {ShekelDollar}\n'
      f'abroad state: {abroad}\n'
      f'my apartment is number: {ApNum}\n'
      f'the currency and age result is: {float(age) + ShekelDollar}')

# assignment F

phone = input("Please enter phone number:\n")
print(f'phone number: {phone}')


# assignment G

def printHello():
    print('Hello')


def calculate():
    print(5 + 3.2)


# assignment H

def yourName(name: str):
    print(name)


def numdev(num):
    print(num / 2)


yourName("dan")
numdev(5)


# assignment i

def addUp(num1: int, num2: int):
    return num1 + num2


def space(string1: str, string2: str):
    return string1 + " " + string2


print(addUp(5, 4))
print(space('Dan', 'Arus'))

#challange
# assignment K

for range
