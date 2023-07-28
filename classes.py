class Robot:
    def __init__(self,name: str,color: str,weight:int):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce(self):
        print(f"my namee is {self.name}")
r1=Robot('Tom','red',30)
r2=Robot('Jerry','blue',40)
r1.introduce()
r2.introduce()

# ADDING RELATIONSHIPS TO VARIOUS OBJECTS AND SETTING STATES

class Person:
    def __init__(self,name:str,personality:str,isSitting:bool,robotowned:Robot):
        self.name=name
        self.personality=personality
        self.isSitting=isSitting
        self.robotowned=robotowned
    def sit_down(self):
        self.isSitting=True
        print(f"{self.name} is_sitting {self.isSitting}")
    def stand_up(self):
        self.isSitting=False
        print(f"{self.name} is_sitting {self.isSitting}")
p1=Person('Alice','aggressive',False,r1)
p2=Person('Becky','talkative',True,r2)
p1.sit_down()
p2.sit_down()
p2.stand_up()