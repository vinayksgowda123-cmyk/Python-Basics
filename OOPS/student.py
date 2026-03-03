class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.grades=[]
    def add_grade(self,grade):
        self.grades.append(grade)    
    def get_average(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        return 0   
student1=student("Alice",20)
student1.add_grade(85)
student1.add_grade(92)
print(student1.get_average())    