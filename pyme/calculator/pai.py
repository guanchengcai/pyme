def Pi():
    pai = 0
    i1 = 1
    i3 = 0
    i4 = -1
    while i1 <= 100000:
        if i1 == 1:
            i2 = 3
        else:
            i2 = 4/(i3*(i3 + 1)*(i3 + 2)*i4)     
        i4
        pai = pai + (i2)
        i3 = i3 + 2
        i1 = i1+1
    return (pai)

print(Pi())