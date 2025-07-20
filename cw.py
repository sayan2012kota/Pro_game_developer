class Student():

    name = ""
    age = 15

    def __init__(self):
        print("Checking the details of the student")

    def ask_details(self):
        self.name = input("What is your name?")
        self.age = input("What is your age?")

    def display_details(self):
        print(self.name)
        print(self.age)

Arjun = Student()
print(Arjun.age)

Arjun.ask_details()
Arjun.display_details()

Dhruv = Student()

Dhruv.ask_details()
Dhruv.display_details()
