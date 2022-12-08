#Zadanie 1
a = int(input("Podaj podstawę trójkąta: "))
h = int(input("Podaj wysokość trójkąta: "))

b = (a * h)/2

c = int(input("Zgadnij pole trójkąta: "))

if b > c:
    print("Pole trójkąta jest większe, niż podałeś")

elif b < c:
    print("Pole trójkąta jest mniejszę, niż podałeś")

else:
    print("Zgadłeś!")

# Zadanie 2
while True:
  a = str(input("Zdeklaruj płeć k/m?: "))
  if a == 'm':
        print("Witaj mężczyzno!")
        break
  if a == 'k':
        print("Witaj kobieto!")
        break
  else:
        print("Możesz wybrać tylko 'k' albo 'm'")
        continue

