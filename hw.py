class Person():
    name = ""
    age = 32
    gender = "male"
    job = "farmer"

    def __init__(self):
        print("Finding out information about the person")

    def ask_information(self):
        self.name = input("What is your name?")
        self.age = input("What is your age?")
        self.gender = input("What is your gender?")
        self.job = input("What is your job?")

    def show_details(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.job)

Josh = Person()

Josh.ask_information()
Josh.show_details()