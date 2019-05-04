import random,time
class A():
    def __init__(self,n,m):
        self.n = n
        self.m = m
    def give(self):
        return '价值'+self.m+'的'+self.n

n = input('What your name?')
print('欢迎来到幸运大抽奖，'+n)
a = [ A('computer','10000'),
      A('金币','6666'),
      A('空调','5555')]
u = random.randint(0,2)
time.sleep(2.50)
if u == 0:
    print('恭喜'+n+'获得一等奖🥇'+a[0].give())
elif u == 1:
    print('恭喜'+n+'获得二等奖🥈'+a[1].give())
elif u == 2:
    print('恭喜'+n+'获得三等奖🥉'+a[2].give())

