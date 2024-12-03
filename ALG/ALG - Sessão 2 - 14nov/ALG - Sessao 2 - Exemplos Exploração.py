# DA 2024/2025
# ALG
# SESSÃO 3 - 15/11/2024
#####################################################################################


# Apresentar a soma de dois valores inteiros dados 
num1=1
num2=4
soma=num1+num2
print(soma)  # imprime o valor da soma
print("A soma é",soma)
print("-------------------------------------------------------")

# __________________________________________________________________________________
# Pedir 2 números inteiros ao utilizador e apresentar a soma deles

# INPUT --> pedir ao utilizador a inserção de dados, neste caso, 2 números n1 e n2 
# INT --> está definir o tipo de dado: é um número inteiro
# PRINT --> para que o resultado apareça visível no terminal!
n1=int(input("Insira o 1º número: \n"))
n2=int(input("Insira o 2º número: \n"))
#  calcula a soma e guarda na variavel "resultado"
resultado=n1+n2
print("Soma=",resultado)


# NOTA: Devemos definir o tipo de dados!
x=input("Escreva a sua idade:")
y=input("escreva um número inteiro:")
print(x+y)


# __________________________________________________________________________________
# Pedir 2 números reais ao utilizador e apresentar a soma deles


# FLOAT --> está definir o tipo de dado: é um número decimal
# \n --> mudar de linha no terminal quando o programa corre
m1=float(input("Insira o 1º número: \n"))
m2=float(input("Insira o 2º número: \n"))
print("Resultado= ", m1+m2)
# Se não vamos reutilizar, não é necessário criar uma terceira variável "soma"