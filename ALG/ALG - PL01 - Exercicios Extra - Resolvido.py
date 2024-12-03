# DA 2024/2025
# ALG

# PL01 - Exercícios Extra (até «Estrutras de Decisão e Seleção»)
##################################################################################################


# 1)	Solicite ao utilizador que insira um número qualquer e determine se é positivo, negativo ou zero.

numero = float(input("Insira um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

# 2)	Peça ao utilizador para inserir dois números e determine qual é o maior ou se são iguais.

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))
if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os dois números são iguais.")

# 3)	Solicite a idade de uma pessoa e verifique se é maior ou menor de idade (idade mínima: 18 anos).

idade = int(input("Insira a sua idade: "))
if idade >= 18:
    print("É maior de idade.")
else:
    print("É menor de idade.")

# 4)	Peça ao utilizador para inserir uma temperatura em graus Celsius e classifique como "Frio", "Agradável" ou "Quente", com base nos seguintes critérios:
#         Menor que 15: Frio
#         Entre 15 e 25: Agradável
#         Acima de 25: Quente

temperatura = float(input("Insira a temperatura em graus Celsius: "))
if temperatura < 15:
    print("Está Frio.")
elif 15 <= temperatura <= 25:
    print("Está Agradável.")
else:
    print("Está Quente.")

# 5)	Solicite ao utilizador que insira um número inteiro e determine se é par ou ímpar.

numero = int(input("Insira um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 6)	Peça ao utilizador para inserir um número e verifique se está no intervalo de 10 a 20 (inclusive).

numero = int(input("Insira um número: "))
if 10 <= numero <= 20:
    print("O número está no intervalo de 10 a 20.")
else:
    print("O número está fora do intervalo de 10 a 20.")

# 7) 7)	Solicite ao utilizador que insira um número de 1 a 7 e use match-case para imprimir o dia correspondente (1 = Segunda-feira, 7 = Domingo).

dia = int(input("Insira um número de 1 a 7: "))
match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")
    case _:
        print("Número inválido. Insira um número entre 1 e 7.")

# 8)	Solicite ao utilizador uma nota de 0 a 10 (pode ter casas decimais) e categorize como:
#          0-5: Insuficiente (5 excluído)
#          5-7: Regular (5 incluído e 7 excluído)
#          7-9: Bom (7 incluído e 9 excluído)
#          9-10: Excelente (9 e 10 incluídos)

nota = float(input("Insira a sua nota (0 a 10): "))

if 0 <= nota < 5:
    print("Insuficiente")
elif 5 <= nota < 7:
    print("Regular")
elif 7 <= nota < 9:
    print("Bom")
elif 9 <= nota <= 10:
    print("Excelente")
else:
    print("Nota inválida.")



# 9)	Peça ao utilizador para inserir um ano e determine se é bissexto usando a regra:
#          Ano é bissexto se é divisível por 4 e não por 100, ou se é divisível por 400.

ano = int(input("Insira um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

# 10)	Solicite ao utilizador para inserir o valor de uma compra e aplique o desconto baseado nas seguintes faixas de preço:
#             Até 100€: Sem desconto
#             Entre 101€ e 500€: 10%
#             Acima de 500€: 20%

valor_compra = float(input("Insira o valor da compra em euros: "))
if valor_compra <= 100:
    desconto = 0
elif 101 <= valor_compra <= 500:
    desconto = 0.10 * valor_compra
else:
    desconto = 0.20 * valor_compra

valor_final = valor_compra - desconto
print(f"O valor final da compra, com desconto, é: {valor_final:.2f}€")

# 11) 11)	Faça um programa que receba 3 valores que representarão os lados de um triângulo e verifique se os valores formam um triângulo e classifique esse triângulo como: 
#         Equilátero (3 lados iguais); 
#         Isósceles (2 lados iguais); 
#         Escaleno (3 lados diferentes). 
# De notar que para formar um triângulo: 
#  - Nenhum dos lados pode ser igual a zero; 
#  -Um lado não pode ser maior do que a soma dos outros dois.

l1 = int(input('Qual o valor do lado 1? '))
l2 = int(input('Qual o valor do lado 2? '))
l3 = int(input('Qual o valor do lado 3? '))

if l1 <= 0 or l2 <= 0 or l3 <= 0:
    print('Triângulo impossível, pelo menos um dos lados é 0 ou negativo')
elif l1 >= l2 + l3 or l2 >= l1 + l3 or l3 >= l1 + l2:
    print('Triângulo impossível, pelo menos um dos lados é maior que a soma dos outros 2')
else:
    if l1 == l2 == l3:
        print('Triângulo equilátero')
    elif l1 != l2 != l3:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')