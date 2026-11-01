# class Employee:
# 	def __init__(self, name, salary):
# 		self.name = name
# 		self.salary = salary

# emp1 = Employee("Teo Mile", 5000)
# emp2 = Employee("Joao", 10000)

# print(emp1.name, emp1.salary)
# print(emp2.name, emp2.salary)


# # Atributos em nivel de classe

# # Create a Player class
# # Create a Player class
# class Player:

#     MAX_POSITION = 10

#     def __init__(self, position):

#         if position <= Player.MAX_POSITION:

#               self.position = position

#         else:

#               self.position = Player.MAX_POSITION
# # Create a player p and print its MAX_POSITION
# # Create Players p1 and p2
# p1 = Player(9)
# p2 = Player(5)

# print("MAX_POSITION of p1 and p2 before assignment:")
# # Print p1.MAX_POSITION and p2.MAX_POSITION
# print(p1.MAX_POSITION)
# print(p2.MAX_POSITION)

# # Assign 7 to p1.MAX_POSITION
# p1.MAX_POSITION = 7

# print("MAX_POSITION of p1 and p2 after assignment:")
# # Print p1.MAX_POSITION and p2.MAX_POSITION
# print(p1.MAX_POSITION)
# print(p2.MAX_POSITION)

# # Metodos de classe, e possivel definir metodos de classe, Eles devem ter escopo, pois nao usam dados da instancia, mas sim da classe. Para definir um metodo de classe, usamos o decorador @classmethod. O primeiro parametro do metodo de classe e a propria classe, por convenção chamamos de cls.

class Person:
  CURRENT_YEAR = 2026
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # Add a class method decorator
  @classmethod
  # Define the from_birth_year method
  def from_birth_year(cls, name, birth_year):
    # Create age
    age = cls.CURRENT_YEAR - birth_year
    # Return the name and age
    return cls(name, age)

bob = Person.from_birth_year("Bob", 1995)
print(bob.age)



# Heranca

class Employee:
    MIN_SALARY = 30000    

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY
        
    def give_raise(self, amount):
        self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
    # Add a keyword to leave this class empty
    pass

# Define a Manager object
mng = Manager("Debbie Lashko", 86500)

# Print mng's name
print(mng.name)


class Employee:
  def __init__(self, name, salary=30000):
    self.name = name
    self.salary = salary

  def give_raise(self, amount):
    self.salary += amount

class Manager(Employee):
  def display(self):
    print("Manager ", self.name)

  def __init__(self, name, salary=50000, project=None):
    Employee.__init__(self, name, salary)
    self.project = project

  # Add a give_raise method
  def give_raise(self, amount, bonus=1.05):
    new_amount = amount * bonus
    Employee.give_raise(self, new_amount)
    
mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)