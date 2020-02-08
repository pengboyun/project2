#出题目给玩家计算
#

import random as r
import easygui as e

#计算出正确的结果
def jisuan(n1 , n2 , fu):
  result = 0
  if fu == '➕':
    result = n1 + n2
  elif fu == '➖':
    result = n1 - n2
  elif fu == '✖️':
    result = n1 * n2
  else:
    result = n1 / n2
  return result

#随机输出符号加减乘除
def fuhao():
  x = r.randint(0,3)
  fu = ""
  if x == 0:
    fu = '➕'
  elif x == 1:
    fu = '➖'
  elif x == 2:
    fu = '✖️'
  else:
    fu = '➗'
  return fu

# 判断是否为数字
def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    pass

  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass

  return False


x = 0
g = 0
while True:
  n1 = r.randint(1, 5)
  n2 = r.randint(1, 5)
  n3 = r.randint(1, 5)
  fu1 = fuhao()
  fu2 = fuhao()

  #计算结果
  if (fu1 == '➕' or fu1 == '➖') and (fu2 == '✖️' or fu2 == '➗'):
    result = jisuan(n1,jisuan(n2,n3,fu2),fu1)
  else:
    result = jisuan(jisuan(n1, n2, fu1), n3, fu2)

  #去除皮皮头算不出问题
  if result < 0 or result != int(result):
    continue

  x = x + 1
  if x == 5:
    break

  player = e.enterbox(str(n1)+fu1+str(n2)+fu2+str(n3)+'='+str(result))

#游戏结束，
  if player == None:
    print('你答对了' + str(g) + '道题')
    break
#告诉玩家是否答对
  elif int(player) == int(result):
     e.msgbox('答对了')
     g = g + 1
  else:
    e.msgbox('答错了')



