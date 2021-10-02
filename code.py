introduction = input("Give your introduction: ")
characterCount = 0
words = 1

for count in introduction:
    characterCount = characterCount+1
    if(count == ' '):
        words = words+1
print(words)
print(characterCount)
