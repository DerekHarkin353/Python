word = "Celebration"
vowel = ['a', 'e', 'i', 'o', 'u']
i = 0
b = 0
while i < len(word):
    if word[i] in vowel:
        b += 1
    i += 1
print(b)
