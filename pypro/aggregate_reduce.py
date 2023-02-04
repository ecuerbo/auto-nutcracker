from functools import reduce
def doSum(x1, x2):
    return x1+x2
x = reduce(doSum,[100,122,33,4,5,6])
print(x)