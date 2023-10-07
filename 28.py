nums = [1,1,1,2,2,3]
k = 2

dictionary = {}
for i in nums:
    if i in dictionary:
        dictionary[i] = dictionary[i] + 1
    else:
        dictionary[i] = 1

max = [0]*k

for item in dictionary:
    for i in range(k):
        if dictionary[item] > max[i]:
            max[i] = dictionary[item]
            break

for i in range(k):
    for item in dictionary:
        if dictionary[item] == max[i]:
            print(item)
            break
