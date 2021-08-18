from pandas import DataFrame
data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}
purchases = DataFrame(data)
print(purchases)
