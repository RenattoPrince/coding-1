class student:

    grade=10
    name="Steve"
    def intro(self):
        print("hello. I am a student")

    def details(self):
            print("My name is", self.name)
            print("I study in ghrade", self.grade)
ob=student()
ob.intro()
ob.details()