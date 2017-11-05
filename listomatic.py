def list_o_matic(list, word):
    if word == '':
        word = list.pop()
        return word + ' popped from the list\n'
    else:
        if word in list:
            list.remove(word)
            return '1 instance of ' + word + ' removed from the list\n'
        else:
            list.append(word)
            return '1 instance of ' + word + ' appended to the list\n'


list = ['cat','goat','cow', 'cat']

while len(list) != 0:
    print('look at all the animals ' + str(list))
    word = input("enter the name of the animal: ")
    if word == 'quit' or word == 'Quit':
        print('Goodbye!')
        quit()
    else:
        print(list_o_matic(list, word))

print('Goodbye')
quit()