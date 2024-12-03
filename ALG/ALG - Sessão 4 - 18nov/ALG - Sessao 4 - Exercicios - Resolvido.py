# DA 2024/2025
# ALG
# SESSÃO 4 - 18/11/2024
###########################################################################################################

# EXERCÍCIO 1
# Constrói um programa em Python
# que leia 3 números e apresenta a sua multiplicação. 

n1=float(input("Insira nº1: \n"))
n2=float(input("Insira nº2: \n"))
n3=float(input("Insira nº3: \n"))
multiplicacao=n1*n2*n3
print ("o resultado é", multiplicacao)


#_________________________________________________________________________________________________________
# EXERCÍCIO 2
# Constrói um algoritmo que execute as seguintes operações: 
'''
Leia o nome de uma pessoa;
Solicite o salário bruto da pessoa;
Calcule o salário líquido de acordo com a seguinte fórmula:

sal_liquido = sal_bruto - sal_bruto*tx_ss - sal_bruto*tx_irs
Assumindo que tx_ss = 0.11 e tx_irs = 0.18
'''
# O programa deverá devolver o nome da pessoa seguido do seu salário líquido.
# De seguida, executa o mesmo em Python.



# RESOLUÇÃO 1
Nome=str(input("Nome: "))
sal_bruto=float(input("Salário Bruto: "))
tx_ss=0.11
tx_irs=0.18
sal_liquido=sal_bruto-sal_bruto*tx_ss-sal_bruto*tx_irs
print(f"A {Nome} tem um salário líquido de: {sal_liquido}")

# RESOLUÇÃO 2
nome=str(input("Escreva seu nome: "))
salario_bruto=float(input("Escreva o salário bruto: "))
sal_liquido = salario_bruto - salario_bruto*0.11 - salario_bruto*0.18
print(nome,"seu salário é",sal_liquido,"euros")







#_________________________________________________________________________________________________________
# EXERCÍCIO 3
# Constrói um algoritmo que devolva o seguinte output: 
'''
Indique o seu nome: Miguel
Quantos dias trabalhou neste mês? 24
Qual o valor do Subsidio diário? 5

O Miguel tem direito a 120 Euros de Subsidio.

'''
# O programa deverá devolver o nome da pessoa seguido do seu salário líquido;
# De seguida, executa o mesmo em Python.

Nome=str(input("Indique o seu nome: "))
Dias=int(input("Quantos dias trabalhou neste mês? "))
diário=int(input("Qual o valor do Subsidio diário? "))
 
print(f"O {Nome} tem direito a {Dias*diário} Euros de Subsidio.")
# OU
# subsidio=Dias*diário
# print(f"O {Nome} tem direito a {subsidio} Euros de Subsidio.")
'



#_________________________________________________________________________________________________________
# EXERCÍCIO 4
# Cria um programa que leia as temperaturas da semana (útil) e devolva a média das mesmas. 



seg=float(input("Insira a temperatura de segunda feira: "))
ter=float(input("Insira a temperatura de terça feira: "))
qua=float(input("Insira a temperatura de quarta feira: "))
qui=float(input("Insira a temperatura de quinta feira: "))
sex=float(input("Insira a temperatura de sexta feira: "))
media=(seg+ter+qua+qui+sex)/5
print(f"A média das temperaturas da semana é {media:.2f}")

# MAIS À fRENTE.... :)

n = 1
semana = []
 
while n <= 7:
    temp = int(input(f"Qual a temperatura do dia {n} \n"))
    semana.append(temp)
    n += 1

media = sum(semana)/len(semana)
print(f"A temperatura média da semana foi: {media}")





#_________________________________________________________________________________________________________
# EXERCÍCIO 5
# Faça um programa que receba o valor do quilo de um produto e a quantidade de quilos 
# do produto consumida calculando o valor final a ser pago.

preco_kg=float(input("Insira o preço por kilo: "))
quantidade=float(input("Insira a quantidade (kg) consumida: "))
pagamento=preco_kg*quantidade
print(f"O valor a pagar é: {pagamento}")





#_________________________________________________________________________________________________________
# EXERCÍCIO 6
# O preço de um automóvel é calculado pela soma do preço de fábrica com 
# o preço dos impostos (45% do preço de fábrica) e a percentagem do 
# revendedor (28% do preço de fábrica). 
# Faça um algoritmo que leia o nome do automóvel e o preço de fábrica e
# escreva o nome do automóvel e o preço final.

car=str(input("\nWhat's the cars name? "))
fabric=int(input("What's the cost price for the car ? "))
tax=float(fabric*0.45)
comission=float(fabric*0.28)
final=float(fabric+tax+comission)
print(f"\nYour car named {car}, has a final price of {final:.2f}€.\n\nFrom that price, {tax:.2f}€ are taxes value.\n\nAnd the seller will get {comission:.2f}€.\n")

# PORT
Nome_automóvel=str(input("Indique o nome do automóvel: "))
Preço_fábrica=float(input("O valor do preço de fábrica é de "))
Imposto=Preço_fábrica*0.45
Revendedor=Preço_fábrica*0.28
 
print(f"O carro {Nome_automóvel} tem o custo final de {Preço_fábrica+Imposto+Revendedor}")

#_________________________________________________________________________________________________________
# EXERCÍCIO 7
# Pretende-se calcular a área do triângulo, lendo a sua base e a sua altura.

Base=int(input("A base do triangulo é de "))
Altura=int(input("A altura do triangulo é de "))
 
print(f"A area do triangulo é de {Base*Altura/2}")