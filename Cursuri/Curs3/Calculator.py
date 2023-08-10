operator1 = input("Adauga primul numar: ")
while operator1.isdigit() is False:
    operator1 = input("Adauga primul numar: ")

operator2 = input("Adauga al doilea numar: ")
while operator2.isdecimal() is False:
    operator2 = input("Adauga al doilea numar: ")

operand = input("Adauga operandul (+, -, *, /): ")

# while operand not in [+, -, *, /]:
#     operand = input("Adauga operandul (+, -, *, /")
while operand not in '+-*/' or len(operand) != 1:
    if len(operand) != 1:
        print("Ai introdus mai multe caracatere: ")
    operand = input("Adauga operandul (+, -, *, /): ")

if operand == "+":
    rezultat = int(operator1) + int(operator2)
elif operand == "-":
    rezultat = int(operator1) - int(operator2)
elif operand == "*":
    rezultat = int(operator1) * int(operator2)
else:
    while operator2.isdigit() is False or int(operator2) == 0:
        operator2 = input(f"Ai introdus valoarea {operator2}. Adauga al doile numar: ")
    rezultat = int(operator1) / int(operator2)

print(f"{operator1} {operand} {operator2} = {rezultat}")