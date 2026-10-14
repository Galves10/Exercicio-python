def soma(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b
if __name__ == '__main__':
    a1 = int(input("Digite um valor:"))
    b1 = int(input("Digite outro valor:"))
    c = str(input("Digite + para somar ou - para subtrair, * para multiplicar, / para dividir:"))
    if c == '+':
        print("Soma:", soma(a1,b1))
    elif c == '-':
        print("Subtração:", sub(a1,b1))
    elif c == '*':
        print("Multiplicação:", mult(a1,b1))
    elif c == '/':
        print("Divisão:", div(a1,b1))
    else:
        print("Calculo não existente")