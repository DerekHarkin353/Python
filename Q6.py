string = "The cow jumped over the moon." 
lst = ["cow", "over"]

for i in lst:
    string = string.replace(i, '*' * len(i))
print(string)