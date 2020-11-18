import random


class Rectangle:
    # Atributy na úrovni třídy
    default_color = 'khaki'
    default_size = 3
    default_name = "Petříček"
    # Metoda pro inicializaci objektu (konstruktor)
    def __init__(self, x, y, a, b, name):
        # self zastupuje samotný objekt
        # Atributy na úrovni objektu
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.name = Rectangle.default_name
        self.color = Rectangle.default_color

    # Magická metoda pro výpis textové informace o objektu
    def __str__(self):
        return f'Obdélník začíná na pozici ({self.x}, {self.y}) a rozšiřuje se na ose x o {self.a} a na ose y o {self.b}'

    # Magická metoda pro porovnávání objektů
    def __eq__(self, other):
        # Zjistí totožně umístěné objekty
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    # metoda pro zjištění obsahu
    def __gt__(self):
        return  self.a * self.b

    # Magická metoda pro součet obsahů dvou objektů
    def __add__(self, other):
        return self.__gt__() + other.__gt__()

    #zjistí, jestli má 1. objekt větší obsah
    def __sub__(self, other):
        # Provede zjištění vzdálenosti dvou objektů
        return self.__gt__() > other.__gt__()

    #? Tady bude statická (třídní) metoda random_color(), která vygeneruje náhodou barvu rgb zapsanou hexadecimálně
    @staticmethod
    def random_codename():
        return ''.join([str(random.randint(0, 255))[2:] for i in range(5)])

    #? Tady bude metoda třídy random_pos(), která bude na základě zadaných argumentů určujících platný rozsah hodnot
    #? vytvářet náhodně umístěné body

    @classmethod
    def random_pos(cls, min=1, max=20):
        return cls(random.randrange(min, max), random.randrange(min, max), random.randrange(min, max), random.randrange(min, max), "")

    # Metoda objektu, která (symbolicky v podobě textu) "vykreslí" daný objekt
    def draw(self):
        # Argument self zastupuje samotný objekt
        print(f'Začínající bod (x:{self.x}, y:{self.y}), rozměry a:{self.a}, b:{self.b}, barva: {self.color}, jméno: {self.name}')

    #? Tady bude metoda objektu change_color(), která bude na základě zadaného argumentu nastavovat barvu objektu
    def change_name(self, name):
        self.name = name


class infoRectangle(Rectangle):
    def __init__(self, x, y, a, b, name, url):
        super().__init__(x, y, a, b, name)
        self.name = name
        self.url = url
    def draw(self):
        super().draw()
        print (f'URL: {self.url}')
#? Ověř fungování všech magických metod na příkladech objektů bod1 a bod2
print(f'{"*".ljust(80,"*")}\nOvěř fungování všech magických metod na příkladech objektů bod1 a bod2')
obdelnik1 = Rectangle(0, 0, 2, 3, "")
obdelnik2 = Rectangle(0, 5, 2, 1, "")
obdelnik8 = infoRectangle(1,2,3,4, "a", "asdasd.asd.vz")
obdelnik8.draw()
print(Rectangle.__str__(obdelnik1))
print(Rectangle.__eq__(obdelnik1, obdelnik2))
print(Rectangle.__gt__(obdelnik1))
print(Rectangle.__add__(obdelnik1, obdelnik2))
print(Rectangle.__sub__(obdelnik2, obdelnik1))
obdelnik1.draw()
obdelnik1.change_name("Jitřenka")
obdelnik1.draw()
obdelnik1.change_name(Rectangle.random_codename())
obdelnik1.draw()
obdelnik2.draw()
obdelnik2 = Rectangle.random_pos()
obdelnik2.draw()
#? Vytvoř do proměnné body seznam 5 objektů na náhodných pozicích v rozmezí -10 až 10
print(f'{"*".ljust(80,"*")}\nVytvoř do proměnné body seznam 5 objektů na náhodných pozicích v rozmezí -10 až 10')

#? Pro každý objekt seznamu body proveď jeho symbolické vykreslení metodou draw()
print(f'{"*".ljust(80,"*")}\nPro každý objekt seznamu body proveď jeho symbolické vykreslení metodou draw()')

#? Zjisti, který objekt v seznamu body má největší vzdálenost od počátku
print(f'{"*".ljust(80,"*")}\nZjisti, který objekt v seznamu body má největší vzdálenost od počátku')

#? Zjisti, mezi kterými objekty v seznamu body je nejkratší vzdálenost
print(f'{"*".ljust(80,"*")}\nZjisti, mezi kterými objekty v seznamu body je nejkratší vzdálenost')
