class Tier:
    def __init__(self, alter: int, gewicht: int):
        self.alter = alter
        self.gewicht = gewicht

class Saeugetier(Tier):
    def __init__(self, alter: int, gewicht: int, winterschlafend: bool):
        super().__init__(alter, gewicht)
        self.winterschlafend: bool = winterschlafend

s1 = Saeugetier(10, 125, True)
print(s1.alter, s1.gewicht, s1.winterschlafend)
assert (s1.gewicht == 125)
assert (s1.alter == 10)
assert (s1.winterschlafend)

print('**************************************************')

class Kraftfahrzeug:
    def __init__(self, gewicht_tonnen: float, anzahl_raeder: int):
        self.gewicht_tonnen: float = gewicht_tonnen
        self.anzahl_raeder: int = anzahl_raeder

class Kraftrad(Kraftfahrzeug):
    def __init__(self, gewicht_tonnen: float):
        super().__init__(gewicht_tonnen, 2)

krad = Kraftrad(0.7)
print(krad.gewicht_tonnen)
print(krad.anzahl_raeder)

class PKW(Kraftfahrzeug):
    def __init__(self, gewicht_tonnen: float, sitz_anzahl: int):
        super().__init__(gewicht_tonnen, 4)
        self.sitz_anzahl: int = sitz_anzahl

pkw = PKW(1.6, 5)
print(pkw.anzahl_raeder)

class LKW(Kraftfahrzeug):
    def __init__(self, gewicht_tonnen: float, zuladung_tonnen: float):
        super().__init__(gewicht_tonnen, 6)
        self.zuladung_tonnen = zuladung_tonnen

lkw = LKW(5.8, 42.0)
print(lkw.gewicht_tonnen + lkw.zuladung_tonnen)
print(lkw.anzahl_raeder)

print('**************************************************')

print('Enums:\n')

from enum import Enum

class BaseColors(Enum):
    Red = 'red'
    Blue = 'blue'
    Green = 'green'

print(BaseColors.Green.name, '--', BaseColors.Green.value)
#gibt Schlüssel und dazugehörigen Wert aus: Green -- green

print(BaseColors('blue')) #gibt Schlüssel für 'blue' aus: BaseColors.Blue

rgb_color = {
    BaseColors.Red: 255,
    BaseColors.Blue: 81,
    BaseColors.Green: 125
}

print(rgb_color[BaseColors.Green])
print(rgb_color[BaseColors.Blue])
print(rgb_color[BaseColors.Red])