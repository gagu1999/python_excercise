# -*- coding: utf-8 -*-

## Animal은 object의 일종이다 (is - a) (네, 조금 헷갈리죠) 추가 점수 부분을 살펴보세요 
class Animal(object):
    def __init__(self):
        print('안녕하세요, 저는 동물입니다.')

## Dog 클래스는 Animal 클래스의 일종이고 self와 name을 매개변수로 하는 __init__을 가진다. (is - a)
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog 클래스는 name이라는 변수를 가진다 (has - a)
        self.name = name
        print(f'저는 {self.name}라는 이름을 가진 개입니다. 동물이죠')

## Cat 클래스는 Animal 클래스의 일종으로 self와 name을 매개변수로 하는 __init__을 가진다.(is -a)
class Cat(Animal):
    
    def __init__(self, name):
        ## Cat은 name이라는 변수를 가진다. (has - a)
        self.name = name
        print(f'저는 {self.name}라는 이름을 가진 고양이입니다. 동물이죠')
        
## Person클래스는 object의 일종이다. (is - a)
class Person(object):

    def __init__(self, name):
        ## Person 클래스는 name이라는 변수를 가진다.
        self.name = name
        print(f'저는 {self.name}이라는 이름의 사람입니다.')
        ## Person은 어떤 종류의 pet을 갖고 있다 (has - a)
        self.pet = None
        print('아직은 애완동물을 가지고 있지 않습니다. 생기면 소개해드릴게요')
## Employee 클래스는 Person 클래스의 일종으로 self, name, salary를 매개변수로 하는 __init__을 가진다 (is - a)
class Employee(Person):
    
    def __init__(self, name, salary):
        ## ?? 음 이 마법은 뭐죠? -> 상속을 받았을때 상위 클래스의 생성자를 안전하게 호출하는 방법이 super(지금 클래스, object).__init__()이다.
        print('안녕하세요, 저는 직장인입니다.')
        print('직장인이기전에 사람이이죠')
        super(Employee, self).__init__(name)
        ## Employee클래스는 salary라는 변수를 가진다. (has - a)
        self.salary = salary
        print(f'직장인으로써 월급은 {self.salary}만큼 받습니다.')

## Fish클래스는 object의 일종이다. (is - a)
class Fish(object):
    def __init__(self):
        print("우하하 나는 물고기다 맛있는 물꼬끼")

## Salmon 클래스는 Fish클래스의 일종이다. (is - a)
class Salmon(Fish):
    def __init__(self):
        super(Salmon, self).__init__()
        print('그중에서도 멋있는 연어 물꼬기!!')

## Halibut클래스는 Fish클래스의 일종이다. (is - a)
class Halibut(Fish):
    def __init__(self):
        super(Halibut, self).__init__()
        print('그중에서도 못생기고 납작한 넙치, 광어 물꼬기!!')
        print('사실 난 환생했엉, 우기명 광어인간으로다가 ㅋㅋㅋ')
## rover는 Dog의 일종이다(is - a)
rover = Dog("Rover")

## satan은 Cat의 일종이다. (is - a) 클래스와 인스턴스 관계
satan = Cat('Satan')

## mary 는 Person의 일종이다. (is - a)
mary = Person('Mary')

## mary는 satan이라는 이름의 pet 변수를 가진다. (has - a)
mary.pet = satan
## frank는 Employee의 일종이다. (is - a)
frank = Employee('Frank', 120000)

## frank는 rover라는 이름의 pet 변수를 가진다. (has - a)
frank.pet = rover

## flipper는 Fish의 일종이다. (is- a)
flipper = Fish()

## crouse는 Salmon의 일종이다. (is-a)
crouse = Salmon()

## harry는 Halibut의 일종이다. (is - a)
harry = Halibut()
