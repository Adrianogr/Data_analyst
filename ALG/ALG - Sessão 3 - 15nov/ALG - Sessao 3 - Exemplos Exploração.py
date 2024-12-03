# DA 2024/2025
# ALG
# SESSÃO 2 - 15/11/2024
###########################################################################################################




# EXERCÍCIO 1
# Crie um algoritmo que após ler dois números inteiros apresenta a sua soma.

'''     revisão da resolução da sessão anterior - ver ficheiro sessao 2    '''

 

# NOTA: -----------------------------------------------------------------------------
# O que for escrito entre ''' e ''' é interpretado como texto e assume outra cor.
# Por exemplo:
'''
m1=float(input("Insira o 1º número: \n"))
m2=float(input("Insira o 2º número: \n"))
print("Resultado= ", m1+m2)
'''


#_________________________________________________________________________________________________________
# EXERCÍCIO 2
# O que retorna este programa?
a = 4
b = 5.2
c= 'a'
d = "vamos escrever um texto"
e = True
print(type(a))  # int
print(type(b))  # float
print(type(c))  # str (string)
print(type(d))  # str
print(type(e))  # bool (booleano)


#_________________________________________________________________________________________________________
# EXERCÍCIO 3
# •Vamos agora criar um programa que tenha operações de input e output, traduzindo o 
# seguinte algoritmo:
'''
variáveis:
   inteiro: idade
   texto: nome
início
   ler idade
   ler nome 
   escrever (“A minha idade é: “ + idade)
   escrever (“O meu nome é “ + nome + “ e a minha idade é “ + idade)
fim
'''

# Resolução: 

idade=int(input("A minha idade é: "))
nome=str(input("O meu nome é: "))
print("A minha idade é",idade)
print("O meu nome é",nome,"e a minha idade é",idade)

# NOTA: alternativa à escrita 
print(f"A minha idade é {idade}")
print(f"O meu nome é {nome} e a minha idade é {idade}")


#_________________________________________________________________________________________________________
# EXERCÍCIO 4
# Faça um programa que receba um valor que é o valor pago,
# um segundo valor que é o preço do produto e retorne o troco a ser dado.

'''  Correcao das resoluções dos formandos na próxima sessão! Bom trabalho :)   '''