#y+[y/4]+[c/4]-2c+[26(m+1)/10]+d-1
import math


def calculateDate(year,m,y,c,days):
    d = 0
    w = y + math.floor(y/4) + math.floor(c/4) - 2*c + math.floor(26*(m+1)/10) + d - 1
    if int(year)%4 == 0:
        if int(year)%100 == 0:
            pass
        else:
            days[11] = 29
    return int(w)%7, days


y2 = 0
def header(year, day, m):
    print('___________________________________________')
    if m == 13 or m == 14:
        m = (m%12)
    print('|                 '+str(year)+'年   '+str(m)+'月            |')
    print('-------------------------------------------')
    dayday = ['日','一','二','三','四','五','六']
    print('',end='|')
    for x in range((7)):
        y = dayday[((int(day)+x)%7)]
        print('{:_^4}'.format(y),end='|')
    print('')
    print('|-----------------------------------------|')
    return int(day)

def PrintDate(year,m,y,c):
    z = 1
    day = [31,30,31,30,31,31,30,31,30,31,31,28]
    if m == 1 or m == 2:
        m = m + 12
        y = y - 1    
    week, day = calculateDate(year,m,y,c,day)
    date = header(year,addda, m)
    print('|',end='')
    for y2 in range(((week-date)%7)):
        print('{:_^5}'.format('__'),end='|')
    print('{:_^5}'.format(z),end='|')
    while z < (7-((week-date)%7)):
        z += 1
        print('{:_^5}'.format(z),end='|')
    print('')
    while z < day[(m-3)]:
        print('|',end='')
        for q in range(7):
            if z == day[(m-3)]:
                break
            z += 1
            print('{:_^5}'.format(z),end='|')
        print('')
if __name__ == "__main__":
    week = []
    while True:
        year = input('请输入一个年份：  ')
        if len(year) == 4:
            if year.isdigit:
                year = str(year)
                c = int(year[0:2])-1
                y = int(year[2:4])
                break

    while True:
        month = input('请输入月份：   ')
        if month.isdigit:
            if 0<int(month)<13:
                m = int(month)
                typ = 'one'
                break
            elif int(month) == 0:
                mL = [1,2,3,4,5,6,7,8,9,10,11,12]
                typ = 'all'
                break

    addda = input()
    if typ == 'one':
        PrintDate(year,m,y,c)
    else:
        for b in mL:
            PrintDate(year,b,y,c)
