class animals():
     def __init__(self,name,voice, age):
         self.name = name
         self.voice = voice
         self.age = age
     def animal(self) -> None:
        print('Имя: ', self.name, ' Издает звук: ', self.voice, 'Возраст: ', self.age)

dog = animals('Спайк', 'Гав!ГАВ!', '5')
dog.animal()
cat = animals('Том', 'Мяуумяу', '1')
cat.animal()
pig = animals('Скрепыш', 'ХРЮХРЮЮЮЮ', '6')
pig.animal()
mouse = animals('Джерри', '..пииии..', '3')
mouse.animal()
