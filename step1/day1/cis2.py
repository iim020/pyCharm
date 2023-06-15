class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("move")

    def speak(self):
        pass


class Dog(Animal): # animal 상속받음
    #오버라이딩
    def speak(self):
        print('bark')


class Duck(Animal):  # Animal 상속
    def speak(self):
        print('quack')


dog = Dog('doggy')
print(dog.name)
dog.speak()
dog.move()
