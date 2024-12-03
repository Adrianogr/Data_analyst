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


# RESOLUÇÃO:
# Exibe o menu de opções
print("Menu:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")

# Lê a escolha do usuário
opcao = int(input("Escolha uma operação (1 a 5): "))

# Usando match-case para executar a opção escolhida
match opcao:
    case 1:
        # Soma
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 + numero2
        print(f"O resultado da soma é: {resultado}")
    
    case 2:
        # Subtração
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 - numero2
        print(f"O resultado da subtração é: {resultado}")
    
    case 3:
        # Multiplicação
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        resultado = numero1 * numero2
        print(f"O resultado da multiplicação é: {resultado}")
    
    case 4:
        # Divisão
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro: Não é possível dividir por zero.")
    
    case 5:
        # Sair
        print("Saindo do programa.")
    
    case _:
        print("Opção inválida. Escolha um número entre 1 e 5.")


