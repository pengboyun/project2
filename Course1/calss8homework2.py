#找最大公因数
def common_factor(num1,num2):
    result = 0
    xx = 0
    if num2 > num1:
        xx = num1
    elif num1 > num2:
        xx = num2

    for i in range(xx):
        x = num1 % (xx-i)
        y = num2 % (xx-i)
        if x == 0 and y == 0:
            result = xx-i
            break
    return result






#-------调用范例----------
temp = common_factor(100,10)
print('最大公因数是'+str(temp))














#找质数
num1 = 10
for i in range(num1):
    print(i+1)
    for j in range(i):
        print('j:  '+str(j))
    #x = num1 % (i+1)
    #if x != 0:
    #    print(x)