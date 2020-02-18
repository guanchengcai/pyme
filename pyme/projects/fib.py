def findfibnum(count):
    li=[]
    for x in range(1,count+1):
        if x == 1 or x == 2:
            li.append(1)
        else:
            li.append(li[-1] + li[-2])
    return li

while True:
    z = input()
    if z.isdigit():
        if int(z) > 0:
            break
print(*findfibnum(int(z)))



