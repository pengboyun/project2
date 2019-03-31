class multiplication(object):
    def __init__(self):
        self.take_several_times = 0
    def pithy_formula(self):
        x = 0
        for x in range(1,self.take_several_times):
            y = ' '
            for i in range(1, x+1):
                y = y + str(i) + '*' + str(x) + '=' + str(i * x) + '   '
            print(y)

    def addition(self):
        x = 0
        for x in range(1,self.take_several_times):
            y = ''
            for i in range(1, x+1):
                y = y + str(i) + '+' + str(x) + '=' + str(i + x) + '   '
            print(y)

result = multiplication()
result.take_several_times = 10
result.pithy_formula()
result.addition()


