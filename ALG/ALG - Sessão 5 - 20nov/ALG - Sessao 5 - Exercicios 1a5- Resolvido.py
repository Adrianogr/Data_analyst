# DA 2024/2025
# ALG
# SESSÃO 5 - 20/11/2024
##################################################################################################



# EXERCÍCIO 1
# Escreva um programa que receba 2 valores do utilizador e retorne o maior entre eles.

#RESOLUÇÃO:
'''
a=int(input("Digite um número:"))
b=int(input("Digite outro número:"))
if a<b:
    print(f"O maior dos dois números é {b}.")
elif a>b:
    print(f"O maior dos dois números é {a}.")
else:
    print(f"Os dois números são iguais!")
'''
#_________________________________________________________________________________________________
# EXERCÍCIO 2
# Escreva um programa que verifique se um número inteiro positivo, dado pelo utilizador, é par ou ímpar.


'''
a=int(input("Digite um número inteiro positivo:"))
if a%2==0:
    print(f"O {a} número é par.")
else:
    print(f"O {a} número é ímpar.")


#NOTA:

n=10%2
print(f"Resto da divisao de 10 por 2={n}")
'''

#_________________________________________________________________________________________________
# EXERCÍCIO 3
# Constrói um algoritmo que, após receber o valor de 2 números inteiros inseridos pelo utilizador, devolvam a sua soma, subtração, multiplicação e divisão. 
        # (NOTA: A subtração e a divisão não são comutativas, ou seja,se trocar a ordem dos números não se obtém obrigatoriamente o mesmo número. No exercício, considere o maior a subtrair/dividir pelo menor.) 
# Deverá indicar ainda se os 2 números são pares ou impares. 


# resolução do Bernardo

a = int(input('Insira o primeiro número: '))
b = int(input('Insira o segundo número: '))

print(f'A soma dos dois números é {a+b}')
print(f'A subtração dos dois números é {a-b}')
print(f'A multiplicação dos dois números é {a*b}')
print(f'A divisão do número maior pelo menor é {round(max(a,b)/min(a,b),3)}')

if a%2 == 0:
    print(f'{a} é par')
else:
    print(f'{a} é ímpar')

if b%2 == 0:
    print(f'{b} é par')
else:
    print(f'{b} é ímpar')


#_________________________________________________________________________________________________
# EXERCÍCIO 4

# Cria um programa que leia o valor introduzido pelo utilizador. O valor introduzido corresponde à nota em % de um teste. 
# A mensagem devolvida para o ecrã deverá respeitar o seguinte intervalo: 
'''
0 a 49% escreve NEGATIVA
50% a 89% escreve POSITIVA
90% a 100% escreve PARABÉNS, EXCELENTE!
'''

# Lê o valor introduzido pelo utilizador
nota = float(input("Introduza a nota em percentagem (0-100): "))

# Avalia a nota e imprime a mensagem correspondente
if 0 <= nota < 50:
    print("NEGATIVA")
elif 50 <= nota < 90:
    print("POSITIVA")
elif 90 <= nota <= 100:
    print("PARABÉNS, EXCELENTE!")
else:
    print("Por favor, introduza uma percentagem entre 0 e 100.")



#_________________________________________________________________________________________________
# EXERCÍCIO 5
#Utilize a estrutura SE para fazer um programa que retorne o nome de um produto a partir do código do mesmo. Considere os seguintes códigos:
#       • 001 - Parafuso;
#       • 002 - Porca;
#       • 003 - Prego;
#       • Para qualquer outro código indicar “Não definido”.

def ex5():
    cod = int(input("Qual o código do produto? "))

    if cod == 1:
        print('001 - Parafuso')
    elif cod == 2:
        print('002 - Porca')
    elif cod == 3:
        print('003 - Prego')
    else:
        print('Não definido')

# Refaça o exercício anterior usando a estrutura LER-CASO.
def ex5_alt():
    cod = int(input("Qual o código do produto? "))

    match cod:
        case 1:
            print('001 - Parafuso')
        case 2:
            print('002 - Porca')
        case 3:
            print('003 - Prego')
        case _:
            print('Não definido')

#_________________________________________________________________________________________________
# DESAFIO!
# Pretende-se criar um algoritmo que troque o valor de 2 variáveis. Como podemos fazer esta operação?


x = 20
y = 10

print(f"Antes da troca: x = {x}, y = {y}")

# Usa uma variável auxiliar para trocar os valores
auxiliar = x  # Armazena o valor de x na variável auxiliar             ( x --> auxiliar)
x = y         # Atribui o valor de y a x                               ( y --> x )
y = auxiliar  # Atribui o valor armazenado na variável auxiliar a y    ( auxiliar --> y )

print(f"Depois da troca: x = {x}, y = {y}")


#_________________________________________________________________________________________________
# EXERCÍCIO 6 
# Crie um programa em Python que permita calcular o resultado de uma operação aritmética entre dois números, com base em um menu de seleção. O programa deve permitir as seguintes operações:
'''
Soma: Retorna a soma dos dois números inseridos.
Subtração: Retorna a subtração do primeiro número pelo segundo.
Multiplicação: Retorna o produto dos dois números.
Divisão: Retorna o quociente do primeiro número pelo segundo, caso o divisor seja diferente de zero.
Sair: Encerra o programa.
'''
#Restrições do exercício:
# Deve usar a estrutura match-case e as condições if-else.
# Não é permitido usar ciclos (for, while) nem variáveis globais.
# O programa deve calcular apenas uma operação por execução. Para realizar outra operação, o programa deverá ser reiniciado.

# --- > RESOLVIDO EM FICHEIRO SEPARADO





