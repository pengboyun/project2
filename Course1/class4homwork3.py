import easygui
class Multiplication(object):
    def __init__(self):
        self.xxxxxxxxxxxxxx=3
    def multiplication_table(self):
        x = 0
        for x in range(1, self.xxxxxxxxxxxxxx):
            y = ''
            for i in range(1, x + 1):
                y = y + str(i) + '*' + str(x) + '=' + str(i * x) + "  "
            print(y)

m = Multiplication()
m.xxxxxxxxxxxxxx = 10
print(m.xxxxxxxxxxxxxx)
m.multiplication_table()