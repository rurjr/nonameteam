num = input('you list,enter like in example(1,2,3):   ')
def work_with_list(num):
    list_of_num = num.split(',')
    last_item = list_of_num[-1]
    list_reversed = list_of_num[::-1]
    m = 5 in list_of_num
    five_in_list = ''
    if m == True:
        five_in_list = 'Yes'
    else:
        five_in_list = 'No'
    number_of_five = 0
    for i in list_of_num:
        if int(i) == 5:
            number_of_five += 1
    remove_last_first = list_of_num[1:-1]
    numbers_lessthan5 = 0
    for i in list_of_num:
        if int(i) < 5:
            numbers_lessthan5 +=1
    print(last_item,list_reversed,five_in_list,number_of_five,remove_last_first,numbers_lessthan5)
work_with_list(num)
