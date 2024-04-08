class rating():
    def __init__(self, number: int):
        self.number=number
        if number < 3:
            print('Проект нуждается в доработке')
        elif number >=3 and number < 4:
            print('Запуск стартапа прошел неплохо')
        else:
            print('Запуск стартапа прошел успешно')
number = rating(int(input('Введите рейтинг: ')))