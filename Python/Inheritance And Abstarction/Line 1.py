class Person(object):

    def __init__(self,name,idnumber):
        self.name= name
        self.idnumber= idnumber
    def display(self):
        print("Name :", self.name,)
        print("ID Number :", self.idnumber)

class Employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary= salary
        self.post= post

        Person.__init__(self,name,idnumber)# super().__init__(name,idnumber)

a = Employee('Ricky', 68679264, 18392092, "Intern")
    
a.display()