import easygui
import random
ran = random.randint(1, 8)

uesr_input = easygui.enterbox(str(ran)+'+3=?','皮皮看你会不会？' )
if uesr_input == str(ran + 3):
    easygui.msgbox('答对了')
else:
    easygui.msgbox('皮皮头不会！')
    ran = random.randint(1, 8)
