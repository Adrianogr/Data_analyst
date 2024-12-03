# DA 2024/2025
# ALG
# SESSÃO 6 - 25/11/2024
##################################################################################################

# EXERCÍCIO 1
# Faça um programa que utilize a estrutura ENQUANTO para ler 20 números, inseridos pelo utilizador, e calcule e exiba a média aritmética deles. 

""""
soma=0
quantidade=5
contador=0
#somar todos os números introduzidos
while contador < quantidade:
    numero=int(input(f"Insira o {contador +1}º número: ")) 
    soma+=numero
    contador+=1
#calcular a média

media=soma/quantidade
print(f"A média dos {quantidade} números é {media:.0f}") """


#Versão 2 (qdt dada pelo utilizador)
""""
soma=0
quantidade=int(input("Escreva a quantidade de números cuja média quer calcular: "))
contador=0
#somar todos os números introduzidos
while contador < quantidade:
    numero=int(input(f"Insira o {contador +1}º número: ")) 
    soma+=numero
    contador+=1
#calcular a média

media=soma/quantidade
print(f"A média dos {quantidade} números é {media:.0f}") """



#_________________________________________________________________________________________________
# EXERCÍCIO 2
# Refaça o exercício anterior, usando um ciclo PARA (FOR).
""""
soma=0
quantidade= 5

for contador in range(quantidade):
    numero=int(input(f"Insira o {contador +1}º número: "))
    soma+=numero
    contador +=1
media= soma/contador

print(f"A média dos {contador} números é {media:.0f}") """



#_________________________________________________________________________________________________
# EXERCÍCIO 3
# Escreve um programa que solicite a inserção de valores inteiros até ser introduzido o valor 0.
# Extra: no final apresentar a quantidade e a soma dos n º inseridos 

""""

soma=0
contador=0

while True:
    num=int(input("Digite mais um número: "))
    if num!=0:
        contador+=1
        soma+=num
    else:
        break #sair do ciclo
print(f"Foram inseridos {contador} números diferentes de zero.")
print(f"A soma dos números transferidos é {soma}") """




#_________________________________________________________________________________________________
# EXERCÍCIO 3
# Crie um programa para gerenciar as notas de uma turma. O programa deve:
# - Solicitar o número de alunos na turma.
# - Para cada aluno, pedir sua nota (de 0 a 20) e mostrar se foi aprovado (nota ≥ 10) ou reprovado.
# - No final, exibir a nota mais alta, a mais baixa e a média da turma.

soma=0
n_alunos= int(input("Digite a quantidade de alunos: "))
nota_baixa=20
nota_alta=0
for _ in range(n_alunos):
    nota=float(input("Imsira a nota do aluno: "))
    if nota >= 10:
        print("Aluno Aprovado")
    else: 
        print("Aluno reprovado")
    soma+=nota 
    if nota>nota_alta:
        nota_alta=nota
    if nota<nota_baixa:
        nota_baixa=nota
    
media=soma/n_alunos
print(f"A média da turma é {media}")
print(f"A nota mais alta é {nota_alta}")
print(f"A nota mais baixa é {nota_baixa}")





