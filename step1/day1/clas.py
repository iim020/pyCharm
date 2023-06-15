# 클래스
# python 도 객체 지향 프로그래밍(oop)#
#클래스 명은 copwords 방식으로 표기
# 함수, 변수, 속성 - 스네티크 표기법 abc_def
# 클래스 예외는 - 파스칼 표기법 : 첫문자 대문자
class Rectangle:
    count = 0 #클래스 변수
    #inirolizer
    def __init__ (self,width, height):
        self.width = width
        self.height= height
        Rectangle.count +=1
# 인스턴스 메서드
    def calcArea(self):
        area = self.width * self.height
        return area
# 정적메소드  self접근불가
    @statsmodels
    def isSquare():
        print('정적 메소드')
    @classmethod
    def printCount(cls):
        print('클래스메소드')
        print(cls.count)

    # 연산자 오버로딩
    def __add__ (self, other):
        obj = Rectangle(self.width +other.width, self.higth + other.hight)
        return obj

     # 연산자 오버로딩
    def __sub__(self, other):
        obj = Rectangle(self.width + other.width, self.higth + other.hight)
        return obj
    # 인스턴드 a
    a = Rectangle(5,10)
    print(a.calcArea())
    Rectangle.isSquare()
    Rectangle.printCount()
    b = Rectangle(10,10)
    c = a+b
    c = a-b
    print(c.width)
