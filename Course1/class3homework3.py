import easygui
import random
ran = random.randint(1,8)
uesr_input = easygui.buttonbox(str(ran)+'+3=?','皮皮看你会不会？',(str(ran+3),str(ran+2),str(ran+4)))
if str(uesr_input) == ran + 3:
    easygui.msgbox('答对了')
else:
    easygui.msgbox('皮皮头不会！')
