# 0! Questão
# def funcao (a,b): soma = a + b; sub = a - b ;mul = a * b ;div = a/b ;funcao (2,3) ;print (soma) ;print(sub) ;print(mul) ;print(div)

a = float(input("Primeiro número:"))
b = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")
if operação == "+":
    resultado = a + b
elif operação == "-":
    resultado = a - b
elif operação == "*":
    resultado = a * b
elif operação == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)