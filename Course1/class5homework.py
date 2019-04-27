import random

money_list=[]

y = 0
while y != 10:
    money_list.append(random.randint(0,1000))
    y = y + 1

x = 0
while x != 10:
    print(str(x)+' - 数组： '+str(money_list[x]))
    x = x + 1



