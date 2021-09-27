# 1、定义一个学生类，包括id、name、score、age四个属性
#    包含study()方法
#    调用创建好的学生类，创建两个学生对象：
#    1) id:1001,name:Allen,score:90,age:18
#    2) id:1002,name:宝儿姐,score:100,age:20
#    3) 调用其中一个对象的study()方法
class Student:
    # 这里的 -> None 可有可无
    def __init__(self,id:int = 0,name:str = ' ',score:int = 0,age:int = 0) -> None:
        self.id = id
        self.name = name
        self.score = score
        self.age = age

    def study(self,course:str = ' '):
        print(f"{self.name} is studying {course}")

    def show_me(self):
        print(f"{self.name}'s id is {self.id}, score is {self.score}, age is {self.age}.")
        

s1 = Student(1001,'Allen',90,18)
s2 = Student(1002,'宝儿姐',100,20)
s1.study('Python')
s2.show_me()