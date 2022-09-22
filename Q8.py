lst = ["&&", "&", "&&&", "&&&&"]
ans = True
word = lst[0]
for i in lst:
    if i != lst:
        ans = False
print(ans)