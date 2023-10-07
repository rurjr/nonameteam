input_tuple = (
    ('a', 23),
    ('b', 37),
    ('c', 11),
    ('d', 29)
)
sorted_tuple = sorted(input_tuple, key=lambda x: x[1])
print(sorted_tuple)
