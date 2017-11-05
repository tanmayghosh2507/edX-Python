poem = input("enter a saying or poem: ")
create_list = poem.split()

length = len(create_list)

for index in range(length):
    if len(create_list[index]) <= 3:
        create_list[index] = create_list[index].lower()
    elif len(create_list[index]) >= 7:
        create_list[index] = create_list[index].upper()


def word_mixer(word_list):
    word_list.sort()
    new_list = []
    while len(word_list) > 5:
        new_list.append(word_list[-5])
        word_list.pop(-5)
        new_list.append(word_list[0])
        word_list.pop(0)
        new_list.append(word_list[-1])
        word_list.pop(-1)

    return new_list

print(*word_mixer(create_list), sep=' ')




