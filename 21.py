text = input('text without punctuation:  ')
def calculate(text):
    splt = text.split(' ')
    sumb = []
    for i in splt:
        for j in i:
            if j not in sumb:
                sumb.append(j)
    print(len(sumb))
calculate(text)