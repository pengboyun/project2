class Cat():
    type = '猫科'
    def __init__(self,name):
        self.name = name
cat1 = Cat('波斯猫')
cat2 = Cat('加菲猫')
print(Cat.type)
print(cat1.name)
print(cat2.name)