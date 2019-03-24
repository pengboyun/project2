import easygui
xingxi = easygui.passwordbox('请输入（A，B，C）')
if xingxi == 'A':
    easygui.boolbox('A类信息')
elif xingxi == 'B':
    easygui.boolbox('B类信息')
elif xingxi == 'C':
    easygui.boolbox('C类信息')
else:
    easygui.buttonbox('无效信息')