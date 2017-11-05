# !curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt

mean_temp1 = open('/Users/Z001LDC/Desktop/test.txt', 'a+')
# mean_temp1 = open('mean_temp.txt', 'a+')
mean_temp1.write('\nRio de Janeiro,Brazil,30.0,18.0')

mean_temp1.seek(0)
headings = mean_temp1.readline().strip().split(',')

while True:
    line = mean_temp1.readline().strip().split(',')
    if len(line) < 4:
        break
    else:
        print(headings[0].title() + ' of ' + line[0] + ' ' + headings[2] + ' is ' + line[2] + ' Celsius')

mean_temp1.close()