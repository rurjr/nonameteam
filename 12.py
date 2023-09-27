ask = int(input('How many credits have you taken?  '))
def definition(ask):
    if ask <= 23:
        print('you are freshman')
    elif ask >= 24 and ask <= 53:
        print('you are sophomore')
    elif ask >= 54 and ask <= 83:
        print('you are junior')
    else:
        print('you are seniour')
definition(ask)