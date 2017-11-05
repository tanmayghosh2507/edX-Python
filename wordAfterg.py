quote = input()

word = ''
for character in quote:
    character = character.lower()
    if character.isalpha():
        word = word + character
    else:
        if word[0] > 'g':
            print(word.upper())
            word = ''
        else:
            word = ''
