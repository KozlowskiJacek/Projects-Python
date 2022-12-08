a = float(input("Wprowadź liczbę:\n"))
b = float(input("wprowadz drugą liczbę:\n"))
c = input("Wprowadź znak:\n")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    print(a / b)
elif c == "%":
    print(a % b)
else:
    print("Wprowadzono zły znak")