import easygui,random
ci = 0
num = random.randint(0,10)
easygui.msgbox('请猜一个十到一的数','猜数游戏','好的')
while True:
    A = easygui.passwordbox('猜数游戏','猜数游戏','')
    ci = ci + 1
    if int(A) == num:
        num = random.randint(0, 10)
        if ci <= 3:
            easygui.msgbox('太厉害了，你猜对只用了'+str(ci)+'次')
            ci = 0
        elif ci >= 7:
            easygui.msgbox('继续加油，你猜对用了' + str(ci) + '次')
            ci = 0
        else:
            easygui.msgbox('还不错哟，你猜对用了' + str(ci) + '次')
            ci = 0
    elif int(A) >= num:
        easygui.msgbox('猜的数太大了！')
    elif int(A) <= num:
        easygui.msgbox('猜的数太小了！')