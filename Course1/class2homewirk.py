import easygui
x = 0
while True:
    Answer = easygui.enterbox('请输入分数')
    if Answer >= '90':
        easygui.ccbox('晚餐加鸡腿！！！')
    if Answer < '90':
        easygui.ccbox('再做5张卷子！！！')

