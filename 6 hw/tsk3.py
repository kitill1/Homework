nwspaper = range(1, 76)
mgzn = range(77, 104)
both = range(21, 34)
a = (mgzn - both)
b = len((nwspaper | a))
print(list(a))