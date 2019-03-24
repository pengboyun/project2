import easygui

x = easygui.buttonbox(msg="101*32=?", title="101*32", choices=("3232", "1234", "3456"))
print(type(x))
if x == str(3232):
     easygui.msgbox('答对了！')
else:
     easygui.msgbox('答错了！')
