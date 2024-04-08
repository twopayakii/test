class Soda:
    def __init__(self, dobavka = None):
        self.dobavka = dobavka
    def show_my_drink(self):
        if self.dobavka:
            print(f'Газировка и {self.dobavka}')
        else:
            print('Обычная газировка')

s1 = Soda(input('Введите добавку, иначе нажмите Enter: '))
s1.show_my_drink()
