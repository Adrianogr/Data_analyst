# Exemplo 1

'''
a=5
b=6
if a>b:
    print(f"O maior valor é {a}")
else:
    print(f"O maior valor é {b}")
'''

# Exemplo 2

'''
a=int(input("Insira o valor a:"))
b=int(input("Insira o valor b:"))
if a>b:
    print(f"O maior valor é {a}")
elif a<b:
    print(f"O maior valor é {b}")
else:
    print(f"Os valores são iguais!")
'''


# Exemplo 3
numero=int(input("Escreve um nº inteiro positivo: "))
match numero:
    case 1:
        print("Um")
    case 2: 
        print("Dois")
    case _:
        print("Outro")