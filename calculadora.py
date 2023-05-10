#Calculadora(simples)

n1 = 0  
n2 = 0
resultado = 0
operator = 0

n1 = int(input("Digite o primeiro numero: "))
print("Operadores disponiveis: ''+', '-', '*', '/' .")
operator = input("Digite o operador: ")
n2 = int(input("Digite o segundo numero: "))

if operator == '+':
    resultado = n1 + n2
elif operator == '-':
    resultado = n1 - n2
elif operator == '*':
    resultado = n1 * n2
elif operator == '/':
    resultado = n1 / n2
else:
    resultado = 'Operação invalida'

print(f'{n1} {operator} {n2} = {resultado}')