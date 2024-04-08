class Car():
  def __init__(self, name, make, model):
       self.name = name
       self.make = make
       self.model = model
  def start(self):
        return print('Над ', self.name, ' , марки ', self.make, ' и модели  ', self.model, ' начался тест драйв')
  def stop(self):
        return print('Над ', self.name, ' , марки ', self.make, ' и модели  ', self.model, ' закончился тест драйв')
Car1 = Car('Скрепыш', 'Nissan', 'Skyline GT-R')
print(Car1.start())
print(Car1.stop())




