import random


def array_print(list):
    x = 0
    h = ''
    print(h)
    while x < 10:
        h = h + '  '+ str(list[x])
        x = x + 1
    print(h)

money_list=[]

y = 0
while y != 10:
    money_list.append(random.randint(0,1000))
    y = y + 1

array_print(money_list)
a = 0
while a > 10:
    a = 0
    g = 0
    if g < money_list[a]:
        g = money_list[a]
    a = a + 1
    print(g)

array_print(money_list)