class pet():
    def __init__(self):
        self.name=''
        self.animal_type=''
        self.age=''
    def set_name(self, name):
        self.name = name
    def set_animal_type(self, animal_type):
        self.animal_type=animal_type
    def set_age(self,age):
        self.age=age
    def get_animal_type(self):
        return self.animal_type
pet = pet()
name = input('Введите имя питомца: ')
animal_type = input('Введите тип ващего питомца: ')
age = input('Введите возраст питомца: ')

pet.set_name(name)
pet.set_animal_type(animal_type)
pet.set_age(age)

print('Имя питомца: ', pet.name)
print('Тип питомца: ', pet.get_animal_type())
print('Возраст питомца: ', pet.age)