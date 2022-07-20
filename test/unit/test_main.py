from main import somar_dois_numeros, dividir, multiplicar, subtrair, exponenciar, calcular_area_quadrado, calcular_area_retangulo, calcular_area_triangulo


def teste_somar_dois_numeros():  # na def de teste, sempre deixar as 4 primeiras letras como "test" para que o framework entenda o que fazer
    # 3 etapas do teste
    # 1a etapa: Configuração / Prepara
    # Valores / Dados
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saída / Output
    resultado_esperado = 17

    # 2a etapa: Eexecuta
    resultado_atual = somar_dois_numeros(num1, num2)

    # 3a etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


def teste_divisao():
    num1 = 8
    num2 = 4

    resultado_esperado = 2

    resultado_atual = dividir(num1, num2)

    assert resultado_atual == resultado_esperado


def teste_multiplicar():

    num1 = 25
    num2 = 4

    resultado_esperado = 100

    resultado_atual = multiplicar(num1, num2)
    assert resultado_atual == resultado_esperado


def teste_subtrair():
    num1 = 25
    num2 = 30
    resultado_esperado = -5
    resultado_atual = subtrair(num1, num2)
    assert resultado_atual == resultado_esperado


def teste_exponenciar():
    num1 = 10
    num2 = 3
    resultado_esperado = 1000
    resultado_atual = exponenciar(num1, num2)
    assert resultado_esperado == resultado_atual


def testar_area_quadrado():
    num1 = 5
    num2 = 2
    resultado_esperado = 25
    resultado_atual = calcular_area_quadrado(num1, num2)
    assert resultado_esperado == resultado_atual


def testar_area_retangulo():
    num1 = 3
    num2 = 3
    resultado_esperado = 9
    resultado_atual = calcular_area_retangulo(num1, num2)
    assert resultado_esperado == resultado_atual


def testar_area_triangulo():
    num1 = 3
    num2 = 3
    resultado_esperado = 4.5
    resultado_atual = calcular_area_triangulo(num1, num2)
    assert resultado_esperado == resultado_atual