# Cozinheiro
def somar_dois_numeros(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possível dividir por 0'


def multiplicar(num1, num2):
    return num1 * num2


def exponenciar(num1, num2):
    return num1 ** num2


def calcular_area_quadrado(num1, num2):
    return num1 ** num2 #area = lado²

def calcular_area_triangulo(num1, num2):
    return (num1 * num2) / 2 #area = (base * altura) /2


def calcular_area_retangulo(num1, num2):
    return num1 * num2 #area = base * altura


if __name__ == '__main__':
    # Garçom
    resultado = somar_dois_numeros(5, 7)
    print(f'A soma é {resultado}')  # < Prato

    resultado = subtrair(6, 5)
    print(f'A subtração é {resultado}')

    resultado = dividir(5, 0)
    print(f'A divisão é {resultado}')

    resultado = multiplicar(10, 10)
    print(f'A multiplicação é {resultado}')

    resultado = exponenciar(10, 3)
    print(f'A exponenciação é {resultado}')

    resultado = calcular_area_quadrado(5,2)
    print(f'A área do quadrado é {resultado}')

    resultado = calcular_area_triangulo(3, 3)
    print(f'A área do triângulo é {resultado}')

    resultado = calcular_area_retangulo(3, 3)
    print(f'A área do retângulo é {resultado}')



