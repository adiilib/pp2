class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base
    def total_salary(self):
        return self.base

class Manager(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name, base)
        self.bonus = bonus
    def total_salary(self):
        return self.base * (1 + self.bonus / 100)

class Developer(Employee):
    def __init__(self, name, base, projects):
        super().__init__(name, base)
        self.projects = projects
    def total_salary(self):
        return self.base + 500 * self.projects

data = input().split()
role, name, base = data[0], data[1], int(data[2])
emp = Manager(name, base, int(data[3])) if role=="Manager" else \
      Developer(name, base, int(data[3])) if role=="Developer" else \
      Employee(name, base)

print(f"Name: {emp.name}, Total: {emp.total_salary():.2f}")
