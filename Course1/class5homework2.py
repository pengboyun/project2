import random


def array_print(list):
    x = 0
    h = ''
    while x < 10:
        h = h + '  '+ str(list[x])
        x = x + 1
    print(h)


num_list = []

y = 0
while y != 10:
    num_list.append(random.randint(1,1000))
    y = y + 1
array_print(num_list)
h = 0
k = 1000
while h < 10:
    if k > num_list[h]:
        k = num_list[h]
        a = h
    h = h + 1

ci = 0
while ci <= 10:
    if num_list[ci] > num_list[ci + 1]:
        cun = num_list[ci]
        num_list[ci + 1] = num_list[ci]
        num_list[ci + 1] = cun
    array_print(num_list)

num_list[0],num_list[a] = num_list[a],num_list[0]

array_print(num_list)