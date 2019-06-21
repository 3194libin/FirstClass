class student:

    def __init__(self,id,sex,age):
        self.id = id
        self.sex = sex
        self.age = age
    def run(self):
        print("我跑的很快！")

    def climb(self):
        print("我很小的时候就会爬！")

    def sleep(self):
        print("我特别爱睡觉")

class HigherStudent(student):
    pass
s = HigherStudent(2017,'woman',18)
s.run()