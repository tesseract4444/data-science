id1, tpy1, year1, kml, newCar1 = 5, 'Audi A6', 2012, 5000, False

car1 = [5, 'Audi A6', 2012, 5000, False]
car2 = {'id': 5, 'modell': 'Audi A6', 'year': 2012, 'km': 5000, 'new': False}
print(car1)
print(car2)

print('********************************************')

class Car:
    def __init__(self, id: int, typ: str, year: int, km: int, price: int):
        self.id: int = id
        self.typ: str = typ
        self.year: int = year
        self.km: int = km
        self.price: int = price
        self.newCar: bool = km == 0

car = Car(5, 'BMW e92', 2012, 5000, 120000)
print(car.typ)
car.km = car.km + 100
print(car.km)

print('********************************************')

print('Aufgabe: Bucherfassung')
class Book:
    def __init__(self, isbn: str, author: str, title: str, price: float):
        self.isbn: str = isbn
        self.author: str = author
        self.title: str = title
        self.price: float = price

book1 = Book('1234', 'Hansdampf', 'Dudeldummdudeldei', 9.99)
print(book1.title)

print('********************************************')

print('Klassen: Methoden')
'''class Car:
    def drive_to(self, dist, consump, dest):
        self.km = self.km + dist
        self.fuel = self.fuel - consump
        self.place = dest

Car().drive_to(100, 7.5, 'Würzburg')'''

print('********************************************')

print('Aufgabe: Methoden')
class Book:
    def __init__(self, isbn: str, author: str, title: str, price: int, ges_seiten:int):

        self.ges_seiten: int = ges_seiten
        self.gelesen: int = 0

    def lese(self, seiten: int):
        self.gelesen = self.gelesen + seiten

        if self.gelesen > self.ges_seiten:
            self.gelesen = self.ges_seiten
            print('Sie haben das Buch kommplett gelesen!')

print('********************************************')

class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x: float = x
        self.y: float = y
        self.width: float = width
        self.height: float = height

    def __repr__(self) -> str:
        return 'Rect(({}, {}), w: {}, h:{})'.format(self.x, self.y, self.width, self.height)

    def __str__(self) -> str:
        return 'Rechteck(x: {}, y: {}, breite: {}, hoehe: {})'.format(self.x, self.y, self.width, self.height)

    def __eq__(self, other) -> bool:
        return isinstance(other, Rectangle) and\
            self.x == other.x and self.y == other.y and\
            self.width == other.width and self.height == other.height

rect1: Rectangle = Rectangle(1, 2, 3, 4)
print(rect1)
print(repr(rect1))

rect2: Rectangle = Rectangle(1, 2, 3, 4)
print(rect1 == rect2)

print('********************************************')

print('Aufgabe: Spezialmethoden')

class Domino:
    def __init__(self, first: int, second: int):
        self.first = first
        self.second = second

    def __str__(self):
        return '[{}, {}]'.format(self.first, self.second)

    def __repr__(self):
        return 'Domino({}, {})'.format(self.first, self.second)

    def __eq__(self, other):
        return isinstance(other, Domino) and(
            (self.first == other.first and self.second == other.second) or
            (self.first == other.second and self.second == other.first)
        )

print('********************************************')

print('Endgame:')

class GameResult:
    def __init__(self, home_team: str, away_team: str, points_home: int, points_away: int):
        self.home_team = home_team
        self.away_team = away_team
        self.points_home = points_home
        self.points_away = points_away

    def announce(self) -> str:
        result_string: str
        if self.points_home > self.points_away:
            result_string = 'gewonnen'
        elif self.points_home < self.points_away:
            result_string = 'verloren'
        else:
            result_string = 'unentschieden gespielt'
        return f'{self.home_team} hat gegen {self.away_team} '\
               f'mit {self.points_home} : {self.points_away} {result_string}.'

result1 = GameResult('FC Bayern', 'SC Freiburg', 3, 1)
print(result1.announce())