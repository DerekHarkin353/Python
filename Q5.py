phrase = "Look before you leap."

a = True
i = 0
while i < len(phrase) - 1:
    if phrase[i] == phrase[i + 1]:
        a = False
    i += 1
print(a)