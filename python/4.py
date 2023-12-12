class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

class Tester(Employee):
    def __init__(self, name, skill):
        super().__init__(name)
        self.skill = skill

class Manager(Employee):
    def __init__(self, name, project):
        self.dev = []
        self.tes = []
        super().__init__(name)
        self.project = project
    def addEmployee(self, name, role):
        if role == "Developer":
            language = input(f"Enter language of developer {name} : ")
            d = Developer(name, language)
            self.dev.append(d)
        elif role == "Tester":
            skill = input(f"Enter skill of tester {name} : ")
            t = Tester(name, skill)
            self.tes.append(t)
        print(f"Added Employee {name} with role {role}")
    def deleteEmployee(self, name, role):
        if role == "Developer":
            for i,dev in enumerate(self.dev):
                if dev.name == name:
                    d = self.dev.pop(i)
                    del d
                    break
        elif role == "Tester":
            for i,tes in enumerate(self.tes):
                if tes.name == name:
                    t = self.tes.pop(i)
                    del t
                    break
    def displayEmployee(self):
        for dev in self.dev:
            print(dev.name, dev.language)
        for tes in self.tes:
            print(tes.name, tes.skill)

m = Manager("Hemant", "Computer")
m.addEmployee("Subham", "Developer")
m.addEmployee("Jenil", "Developer")
m.addEmployee("Sahil", "Tester")
m.addEmployee("Swapnil", "Tester")
m.displayEmployee()
m.deleteEmployee("Subham", "Developer")
m.deleteEmployee("Sahil", "Tester")
m.displayEmployee()

