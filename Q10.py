num = 18

a = 0
for i in str(num):
    a += int(i)

if num % a == 0:
    print(True)
else:
    print(False)