i = 10
while i <= 100:
    j = 2
    while j < 100:
        if i%j == 0:
            break
        j += 1
    if i == j:
        print(i,end=' ')
    i += 1


