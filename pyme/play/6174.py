print('6174 math black hole is when you enter a 4 digit number that doesn\'t have the same number on each digit, then you arrange the number from the biggest to the smallest, minus it by the arrangement of the number from the smallest to the biggest, and continue the process with the number you got, and eventually, you will get 6174')
number = input('enter a 4 digit number  ')
state = True
while state:
    if len(number) == 4 and number.isdigit() == True and not number[0] == number [1] == number [2] == number [3]:
        state = False
    else:
        number = input('enter a 4 digit number  ')

number = str(number)

def Calculator(num,dictionary):
    group = [num[0],num[1],num[2],num[3]]
    group.sort()
    a = int(str(group[0])+str(group[1])+str(group[2])+str(group[3]))
    group.sort(reverse=True)
    b = int(str(group[0])+str(group[1])+str(group[2])+str(group[3]))
    answer = str(b - a)
    dictionary[str(b)+' - '+str(a)] = answer
    if answer == '6174':
        return dictionary
    else:
        Calculator(answer,dictionary)

answer = {}

Calculator(number,answer)

for x,y in answer.items():
    print(x + ' = ' + y)