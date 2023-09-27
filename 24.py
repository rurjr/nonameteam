text = input('line: ')
def encrytping(line):
    lst = list(line)
    even_symb = []
    not_even_symb = []
    ind = 0
    ind_not_even = 1
    while ind <= (len(lst) - 1):
        even_symb.append(lst[ind])
        ind += 2
    while ind_not_even <= (len(lst) - 1):
        not_even_symb.append(lst[ind_not_even])
        ind_not_even += 2
    tot = even_symb + not_even_symb
    encrytpedword = ''
    for i in tot:
        encrytpedword += i
    print(encrytpedword)
encrytping(text)
print()
a = list('hello')
def descrypt(line):
    lst = list(line)
    not_even_symb = lst[(len(lst)//2)+1:]
    even_symb = lst[:(len(lst)//2)+1]
    lenn = len(not_even_symb)
    indd = 0
    right_word = []
    while lenn != 0:
        right_word.append(even_symb[indd])
        right_word.append(not_even_symb[indd])
        indd += 1
        lenn += -1
    right_word.append(even_symb[-1])
    res = ''
    for i in right_word:
        res += i
    print(res)

descrypt('hloel')



