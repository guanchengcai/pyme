import random
class equation:
    minimumCalculation = ''
    maximumCalculation = ''
    def __init__(self, minimum, maximum):
        self.minimumCalculation = minimum
        self.maximumCalculation = maximum

class addition(equation):
    def __init__(self, minimum, maximum):
        self.minimumCalculation = minimum*2
        self.maximumCalculation = maximum*2-1

class minus(equation):
    def __init__(self, minimum, maximum):
        self.minimumCalculation = minimum - maximum
        self.maximumCalculation = maximum - minimum

class multiply(equation):
    def __init__(self, minimum, maximum):
        self.minimumCalculation = minimum * minimum
        self.maximumCalculation = maximum * maximum

class division(equation):
    def __init__(self, minimum, maximum):
        self.minimumCalculation = minimum / maximum
        self.maximumCalculation = maximum / minimum




def questionOut(mini, maxi, operation):
    question = ''
    if operation == '+':
        question = addition(mini, maxi)
        return random.randint(question.minimumCalculation, question.maximumCalculation)
    elif operation == '-':
        question = minus(mini, maxi)
        return random.randint(question.minimumCalculation, question.maximumCalculation)
    elif operation == '*':
        question = random.randint(mini,maxi)* random.randint(mini,maxi)
        return question
    elif operation == '/':
        question = random.randint(mini,maxi)/ random.randint(mini,maxi)
        return question
    
level1 = {}
def addEquation(limit,start,level,operation):
    if start < limit:
        for x in range(1,limit+1):
            if operation == '+':
                level[str(x)+"+"+str(start)] = x + start
            elif operation == '-':
                level[str(x)+"-"+str(start)] = x - start
            elif operation == '*':
                level[str(x)+"*"+str(start)] = x * start
            elif operation == '/':
                level[str(x)+"/"+str(start)] = x / start
        addEquation(limit,start + 1,level,operation)
    return level
question1 = {}
def addQuestion(limit,start,level,operation):
    if start < limit:
        for x in range(1,limit+1):
            if operation == '+':
                level[x + start] = str(x)+"+"+str(start)
            elif operation == '-':
                level[x - start] = str(x)+"-"+str(start)
            elif operation == '*':
                level[x * start] = str(x)+"*"+str(start)
            elif operation == '/':
                level[x / start] = str(x)+"/"+str(start)
        addQuestion(limit,start + 1,level,operation)
    return level
yesend = True
state = True
equation = "+"
while state:
    equation = input('what sort of equation you will like?')
    if equation == '+' or equation == '-' or equation == '*' or equation == '/':
        state = False
    else:
        print('enter +, -, * or /')
state = True
while state:
    start = input("starting level?")
    end = input('end on which level?')
    questionInLevel = input('How many questions in a level?')
    if start.isdigit() and end.isdigit() and questionInLevel.isdigit():
        state = False
    else:
        print('please enter a number')
numberOfCorrect = 0
numberOfWrong = 0
for i in range (int(start),int(end)+1):
    maximum = 10 + i*5
    minimum = i * 5 + 1
    question1 = (addQuestion(maximum,minimum,question1,equation))
    level1 = (addEquation(maximum,minimum,level1,equation))
    if yesend == False:
        break
    print ("LEVEL"+str(i))
    for x in range(int(questionInLevel)):
        if yesend == False:
            break
        y = questionOut(minimum,maximum,equation)
        print (question1.get(y) + "=")
        #print (question1)
        a = y
        z = input()
        if z.isalnum():
            if z == "skip" or z == "Skip":
                break
            elif z == "end":
                yesend = False
            elif z.isdigit() == False:
                print('nonononononono')
                numberOfWrong += 100000
            elif int(a) != int(z):
                print ("wrong!")
                numberOfWrong +=1
                print (a)
            else:
                print ("correct!")
                numberOfCorrect += 1
        else:
            print('nonononononono')
            numberOfWrong +=100000
    question1 = {}
    level1 = {}
print('the end, thank you for playing')
print(f'you got {numberOfCorrect} correct and {numberOfWrong} errors.')