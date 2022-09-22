
max_val = 0

input_lst = [-1, 3, 5, 6, 99, 12, 2]

max_val = 0

for i in range(len(input_lst)):
    if input_lst[i] > max_val:
        max_val = input_lst[i]

print(max_val)