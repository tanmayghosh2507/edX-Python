def get_names():
    elements = []
    print('list any 5 of the first 20 elements in the Period table')
    while len(elements) < 5:
        word = input('Enter the name of an element: ')
        if word.lower() in elements:
            print(word + ' was already entered')
        elif word == '':
            print('empty input')
        else:
            elements.append(word.lower())
    return elements

at_elements = get_names()
# !curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
first20file = open('/Users/Z001LDC/Desktop/test.txt', 'r')
# first20file = open('elements1_20.txt', 'r')

data = []
for i in range(0,20):
    elem = first20file.readline().strip().lower()
    data.append(elem)

found = []
not_found = []
count = 0
for i in range(0,5):
    if at_elements[i] in data:
        found.append(at_elements[i].title())
        count += 1
    else:
        not_found.append(at_elements[i].title())

print('\n' + str(count*20) + '% correct')
print('Found:', end=' ')
print(*found)
print('Not Found:', end=' ')
print(*not_found)

first20file.close()
