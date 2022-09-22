lst_one = [-1, 3, 4, 6, 7, 9]
lst_two = [1, 3]

lst_new = []
for i in lst_one:
    if i in lst_two:
        lst_new.append(i)

print(lst_new)