def my_print(output):
    if output > 5:
        print(output)
    else:
        print("output smaller then 5")


def numtoword(num):
    if num > 4 or num < 0:
        return "out of range"
    dic = {0: "zero", 1: "one", 2: "two", 3: 'three', 4: "four"}
    return dic.get(num)
