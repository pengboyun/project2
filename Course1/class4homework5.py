import easygui
import random

yes = random.randint(1,10)
easygui.msgbox('猜数游戏，规则：猜1到10的数','猜数游戏','继续')
huida = int(easygui.enterbox('你猜','请输入'))
while True:
    if int(huida) == yes:
        easygui.msgbox(easygui.msgbox('答对了','猜数游戏','继续'))
        yes = random.randint(1, 10)
        huida = int(easygui.enterbox('你猜', '请输入'))

    elif int(huida) > yes:
        easygui.msgbox('大了')
        huida = int(easygui.enterbox('你猜','请输入'))

    elif int(huida) < yes:
        easygui.msgbox('小了')
        huida = int(easygui.enterbox('你猜', '请输入'))


