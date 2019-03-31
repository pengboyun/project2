import easygui
class Car(object):
    def __init__(self):
        self.l = '福田'
        self.z = '京'
        self.d = 'N8888'


car = Car()
easygui.msgbox(car.l+'  '+car.z+'  '+car.d)