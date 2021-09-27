# Module_person
class student:
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age

    def show_me(self) -> None:
        print(f"{self.name} is {self.age} years old.")

if __name__ == '__main__':
    s1 = student('Jesse Cavendish',22)
    s1.show_me()    