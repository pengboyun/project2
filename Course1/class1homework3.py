x = 0
for x in range (1,10):
    y = ''
    for i in range(1, 10):
        y = y + str(i) + '*' + str(x) + '=' + str(i*x) + "  "
    print(y)

