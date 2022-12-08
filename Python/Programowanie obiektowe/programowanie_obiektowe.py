
class Calculator():

    def __init__(self):
        print("Init")

    def dodaj(self, a, b):
        wynik = a + b
        print(wynik)

    def odejmij(self, a, b):
        wynik = a - b
        print(wynik)

calc = Calculator()
calc.liczba = 10
calc.liczba +=5
print(calc.liczba)

