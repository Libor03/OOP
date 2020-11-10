import random

'''
Příklad jednoduché třídy Point umožňující vytvářet symbolické grafické objekty - body
'''
class Point:
    # Atribut na úrovni třídy
    default_color = 'red'

    # Metoda pro inicializaci objektu (konstruktor)
    def __init__(self, x, y):
        # self zastupuje samotný objekt
        # Atributy na úrovni objektu
        self.x = x
        self.y = y
        #? Vytvořte atribut objektu color a přiřaďte mu výchozí barvu podle výchozího atributu třídy
        self.color = Point.default_color

    # Magická metoda pro výpis textové informace o objektu
    def __str__(self):
        return f'({self.x}, {self.y})'

    # Magická metoda pro porovnávání objektů
    def __eq__(self, other):
        # Zjistí totožně umístěné objekty
        return self.x == other.x and self.y == other.y

    # Magická metoda pro zjištění, zda je objekt větší (je dál od středu) než druhý
    def __gt__(self, other):
        return self.__sub__(Point.zero()) > other.__sub__(Point.zero())

    # Magická metoda pro součet dvou objektů
    def __add__(self, other):
        # Provede sečtení obou souřadnic a vrátí nový objekt
        return Point(self.x + other.x, self.y + other.y)

    #? Vytvoř magickou metodu, která umožní rozdílem dvou objektů-bodů (jejich odečtením) zjistit jejich vzdálenost
    def __sub__(self, other):
        # Provede zjištění vzdálenosti dvou objektů
        return (abs(self.x - other.x) ** 2 + abs(self.y - other.y) ** 2) ** 0.5

    #? Tady bude statická (třídní) metoda random_color(), která vygeneruje náhodou barvu rgb zapsanou hexadecimálně
    @staticmethod
    def random_color():
        return '#' + ''.join([str(hex(random.randint(0,255)))[2:] for i in range(3)])

    # Metoda třídy, která vytvoří nový objekt-bod na nulových pozicích
    @classmethod
    def zero(cls):
        #? Jaký význam má argument cls ?
        return cls(0, 0)

    #? Tady bude metoda třídy random_pos(), která bude na základě zadaných argumentů určujících platný rozsah hodnot
    #? vytvářet náhodně umístěné body
    @classmethod
    def random_pos(cls, min=0, max=10):
        return cls(random.randrange(min, max), random.randrange(min, max))

    # Metoda objektu, která (symbolicky v podobě textu) "vykreslí" daný objekt
    def draw(self):
        # Argument self zastupuje samotný objekt
        print(f'Bod (x:{self.x}, y:{self.y}), barva: {self.color}')

    #? Tady bude metoda objektu change_color(), která bude na základě zadaného argumentu nastavovat barvu objektu
    def change_color(self, color):
        self.color = color


#? Vytvoř objekt bod1 na pozici x: 8, y: 5
bod1 = Point(8, 5)
print(bod1)
#? Vytvoř objekt bod2 na pozici x: 4, y: 10
bod2 = Point(4, 10)
print(bod2)
#? Změň výchozí barvu na modrou
Point.default_color = "blue"
#? Vytvoř objekt bod3 pomocí metody zero()
bod3 = Point.zero()
bod1.draw()
bod2.draw()
bod3.draw()
#? Ověř datový typ objektu bod1
print(type(bod1))
#? Ověř zda je objekt bod2 instancí třídy Point
print(isinstance(bod2, Point))
#? Proveď změnu barvy objektu bod2 na náhodnou barvu vygenerovanou statickou metodou random_color()
bod2.change_color(Point.random_color())
bod2.draw()

#? Ověř fungování všech magických metod na příkladech objektů bod1 a bod2
print(f'{"*".ljust(80,"*")}\nOvěř fungování všech magických metod na příkladech objektů bod1 a bod2')

print(Point.__str__(bod1))
print(Point.__eq__(bod1, bod2))
print(Point.__gt__(bod2, bod1))
print(Point.__add__(bod1, bod2))
print(Point.__sub__(bod1, bod2))


#? Vytvoř do proměnné body seznam 5 objektů na náhodných pozicích v rozmezí -10 až 10
print(f'{"*".ljust(80,"*")}\nVytvoř do proměnné body seznam 5 objektů na náhodných pozicích v rozmezí -10 až 10')
bod4 = Point.random_pos()
bod5 = Point.random_pos()
body = [bod1, bod2, bod3, bod4, bod5]

#? Pro každý objekt seznamu body proveď jeho symbolické vykreslení metodou draw()
print(f'{"*".ljust(80,"*")}\nPro každý objekt seznamu body proveď jeho symbolické vykreslení metodou draw()')

for l in range(5):
    body[l].draw()

#? Zjisti, který objekt v seznamu body má největší vzdálenost od počátku
print(f'{"*".ljust(80,"*")}\nZjisti, který objekt v seznamu body má největší vzdálenost od počátku')
sos = 0
for q in range(4):
    if( Point.__gt__(body[q], body[q + 1]) == True):
        sos = q

print(f'Bod nejdále od středu je: {body[sos]}')
#? Zjisti, mezi kterými objekty v seznamu body je nejkratší vzdálenost
print(f'{"*".ljust(80,"*")}\nZjisti, mezi kterými objekty v seznamu body je nejkratší vzdálenost')
sos1 = 0
sos2 = 0
lenost = 1000
for q in range(4):
    for w in range(4):
        if (w != q):
            if (w >q):
                if( Point.__sub__(body[q], body[w]) < lenost):
                    sos1 = q
                    sos2 = w


print(f'Nejmenší vzdálenost je mezi body {body[sos1]} a {body[sos2]}')