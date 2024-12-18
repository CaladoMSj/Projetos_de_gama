import math

def soma():
    number_1 = int(input("\n\nPrimeiro número: "))
    number_2 = int(input("Número a ser somado: "))
    resultado = number_1 + number_2
    print(f"    Resultado: {number_1} + {number_2} = {resultado}")


def subtracao():
    number_1 = int(input("\n\nPrimeiro número: "))
    number_2 = int(input("Número a ser subtraído: "))
    resultado = number_1 - number_2
    print(f"    Resultado: {number_1} - {number_2} = {resultado}")


def multiplicacao():
    number_1 = int(input("\n\nPrimeiro número: "))
    number_2 = int(input("Número a ser multiplicado: "))
    resultado = number_1 * number_2
    print(f"    Resultado: {number_1} × {number_2} = {resultado}")
    
    
def divisao():
    number_1 = int(input("\n\nPrimeiro número: "))
    number_2 = int(input("Segundo número: "))
    if number_2 != 0:
        resultado = number_1 / number_2
        print(f"    Resultado: {number_1} ÷ {number_2} = {resultado}")
    else:
        print("        ERRO: Não é possível dividir por Zero.")
        

def porcentagem():
    number = float(input("\n\nDigite o número: "))
    porcentagem = float(input("Digite a porcentagem (%): "))
    resultado = (number * porcentagem) / 100
    print(f"    Resultado: {porcentagem}% de {number} = {resultado}")


def potencia():
    base = float(input("\n\nDigite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = base ** expoente
    print(f"    Resultado: {base} elevado a {expoente} = {resultado}")

def raiz():
    number = float(input("\n\nDigite o número: "))
    raiz = float(input("Digite o valor da raiz: "))
    resultado = number ** (1 / raiz)
    print(f"    Resultado: A raiz {raiz} de {number} = {resultado}")


def fatorial():
    number = int(input("\n\nDigite um número inteiro: "))
    if number >= 0:
        resultado = math.factorial(number)
        print(f"    Resultado: O fatorial de {number} é {resultado}")
    else:
        print("        ERRO: Fatorial não é definido para números negativos!")


def logaritmo():
    number = float(input("\n\nDigite o número: "))
    base = input("Digite a base (exemplo: 10 para log comum ou 'e' para log natural): ")
    if base == "e":
        resultado = math.log(number)
        print(f"    Resultado: O logaritmo natural de {number} é {resultado}")
    else:
        base = float(base)
        resultado = math.log(number, base)
        print(f"    Resultado: O logaritmo de {number} na base {base} é {resultado}")


# Fórmulas de Física
def velocidade_media():
    distancia = float(input("\n\nDigite a distância (m): "))
    tempo = float(input("Digite o tempo (s): "))
    if tempo > 0:
        resultado = distancia / tempo
        print(f"    Resultado: Velocidade média = {resultado} m/s")
    else:
        print("        ERRO: O tempo deve ser maior que zero!")

def energia_cinetica():
    massa = float(input("\n\nDigite a massa (kg): "))
    velocidade = float(input("Digite a velocidade (m/s): "))
    resultado = (massa * velocidade ** 2) / 2
    print(f"    Resultado: Energia cinética = {resultado} J")


def equacao_primeiro_grau():
    print("\nForma da equação: ax + b = 0")
    a = float(input("Digite o coeficiente 'a': "))
    b = float(input("Digite o coeficiente 'b': "))
    if a != 0:
        x = -b / a
        print(f"\nResultado: A solução é x = {x}")
    else:
        print("\nERRO: O coeficiente 'a' não pode ser zero!")

def equacao_segundo_grau():
    print("\nForma da equação: ax² + bx + c = 0")
    a = float(input("Digite o coeficiente 'a': "))
    b = float(input("Digite o coeficiente 'b': "))
    c = float(input("Digite o coeficiente 'c': "))
    
    if a == 0:
        print("\nERRO: Não é uma equação do segundo grau! Use a função de primeiro grau.")
        return
    
    delta = b ** 2 - 4 * a * c
    print(f"\nDelta calculado: {delta}")
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"\nResultado: As raízes são x1 = {x1} e x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"\nResultado: A raiz dupla é x = {x}")
    else:
        print("\nERRO: Não há raízes reais!")

def teorema_pitagoras():
    print("\nTeorema de Pitágoras: a² + b² = c²")
    escolha = input("Deseja encontrar 'A' (cateto 1), 'B' (cateto 2) ou 'C' (hipotenusa)? ").lower()
    
    if escolha == "a" or "A":
        b = float(input("\nDigite o valor de b (cateto 2): "))
        c = float(input("Digite o valor de c (hipotenusa): "))
        if c > b:
            a = math.sqrt(c ** 2 - b ** 2)
            print(f"\nResultado: O valor de a é {a}")
        else:
            print("\nERRO: A hipotenusa deve ser maior que o cateto!")
    elif escolha == "b" or "B":
        a = float(input("\nDigite o valor de a (cateto 1): "))
        c = float(input("Digite o valor de c (hipotenusa): "))
        if c > a:
            b = math.sqrt(c ** 2 - a ** 2)
            print(f"\nResultado: O valor de b é {b}")
        else:
            print("\nERRO: A hipotenusa deve ser maior que o cateto!")
    elif escolha == "c" or "C":
        a = float(input("\nDigite o valor de a (cateto 1): "))
        b = float(input("Digite o valor de b (cateto 2): "))
        c = math.sqrt(a ** 2 + b ** 2)
        print(f"\nResultado: O valor de c é {c}")
    else:
        print("\nERRO: Escolha inválida!")

def calculo_areas():
    print("\nEscolha a figura geométrica para calcular a área:")
    print("1. Quadrado")
    print("2. Retângulo")
    print("3. Triângulo")
    print("4. Círculo")
    escolha = input("Digite o número correspondente: ")
    
    if escolha == "1":
        lado = float(input("\nDigite o valor do lado do quadrado: "))
        area = lado ** 2
        print(f"\nResultado: A área do quadrado é {area}")
    elif escolha == "2":
        base = float(input("\nDigite a base do retângulo: "))
        altura = float(input("Digite a altura do retângulo: "))
        area = base * altura
        print(f"\nResultado: A área do retângulo é {area}")
    elif escolha == "3":
        base = float(input("\nDigite a base do triângulo: "))
        altura = float(input("Digite a altura do triângulo: "))
        area = (base * altura) / 2
        print(f"\nResultado: A área do triângulo é {area}")
    elif escolha == "4":
        raio = float(input("\nDigite o raio do círculo: "))
        area = math.pi * raio ** 2
        print(f"\nResultado: A área do círculo é {area}")
    else:
        print("\nERRO: Escolha inválida!")


# Funções Divertidas
def sorteio():
    import random
    minimo = int(input("\n\nDigite o valor mínimo: "))
    maximo = int(input("Digite o valor máximo: "))
    resultado = random.randint(minimo, maximo)
    print(f"    Resultado: O número sorteado foi {resultado}")

def pi_aleatorio():
    casas = int(input("\n\nQuantas casas decimais de PI você quer? "))
    print(f"    Resultado: PI com {casas} casas decimais = {round(math.pi, casas)}")


# Menu Principal
def limpar_tela():
    print("\n" * 100)

print(" Olá, essa calculadora é baseada em puro código. Sem gráficos visuais!")

def calculadora():
    
    print("\n\n    Veja as opções e digite o número listado abaixo:")
    print("\n        Cálculos básicos:")
    print("    1. Adição")
    print("    2. Subtração")
    print("    3. Multiplicação")
    print("    4. Divisão")
    print("    5. Porcentagem")
    print("    6. Potência")
    print("    7. Raiz")
    print("    8. Fatorial")
    print("    9. Logaritmo")
    print("\n        Cálculos com fórmulas:")
    print("    10. Velocidade Média")
    print("    11. Energia Cinética")
    print("    12. Equação de Primeiro Grau")
    print("    13. Equação de Segundo Grau")
    print("    14. Teorema de Pitágoras")
    print("    15. Calcular Áreas")
    print("\n        Entre outros:")
    print("    70. Sorteio de Números Aleatórios")
    print("    71. Gerador de PI com Casas Decimais")
    print("    99. Sair")
    
    
    while True:
        escolha = input("\n\n      Escolher a opção: ")
        
        
        # Cálculos básicos
        if escolha == "1":
            soma()
        elif escolha == "2":
            subtracao()
        elif escolha == "3":
            multiplicacao()
        elif escolha == "4":
            divisao()
        elif escolha == "5":
            porcentagem()
        elif escolha == "6":
            potencia()
        elif escolha == "7":
            raiz()
        elif escolha == "8":
            fatorial()
        elif escolha == "9":
            logaritmo()
        
        # Fórmulas
        elif escolha == "10":
            velocidade_media()
        elif escolha == "11":
            energia_cinetica()
        elif escolha == "12":
            equacao_primeiro_grau()
        elif escolha == "13":
            equacao_segundo_grau()
        elif escolha == "14":
            teorema_pitagoras()
        elif escolha == "15":
            calculo_areas()
        
        # Entre outros
        elif escolha == "70":
            sorteio()
        elif escolha == "71":
            pi_aleatorio()
        
        elif escolha == "99":
            print("\n        Calculadora encerrada. Até a próxima!")
            break
        else:
            print("Digite apenas uma das opções acima.")
            

calculadora()