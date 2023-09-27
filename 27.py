import itertools
array = [1,3,2,2]
def summ(array,n):
    res = []
    paris = list(itertools.combinations(array,2))
    three = list((itertools.combinations(array,3)))
    four = list((itertools.combinations(array,4)))
    tot = paris + three + four
    for i in tot:
        if sum(i) == n:
            res.append(i)
    print(res)


summ(array,4)
