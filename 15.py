n = int(input('how many items do you want to buy?  '))
def totalprice(n):
    if n < 10:
        print('total price: ' + str( 12* n))
    elif n >= 10 and n<= 99:
        print('total price: ' + str(10 * n))
    else:
        print('total price:' + str(7 * n))
totalprice(n)
