# h = float (input("Digite sua altura:"))
# peso = float (input("Digite seu peso:"))

# peso_ideal = (72.7*h) - 58 

# if peso < peso_ideal:
#     print ("abaixo do peso ideal!")
    
# elif peso == peso_ideal:
#     print ("Dentro do peso ideal!")
    
# else:
#     print ("acima do peso ideal")
    

# altura = float(input("Digite a sua altura em metros: "))
# genero = input("Digite o seu gênero (M para masculino, F para feminino): ")

# if genero == "M":
#     peso_ideal = (72.7 * altura) - 58
#     print("O seu peso ideal (para homens) é:", peso_ideal, "kg")
# elif genero == "F":
#     peso_ideal = (62.1 * altura) - 44.7
#     print("O seu peso ideal (para mulheres) é:", peso_ideal, "kg")
# else:
#     print("Gênero inválido. Digite M para masculino ou F para feminino.")


# lista = []
# for M in range (3):
    
#     nota = float(input("digite sua nota:"))
#     lista.append(nota)
    
# soma = sum (lista)
# print("o resultado é:", soma)

    
# if soma >= 28:
#     print ( "aprovado")
    
# media =soma/4
# print("a media é:", media)

# n1 = float (input("primeiro segmento:"))
# n2 = float(input("segundo segmento:"))
# n3 =float (input("terceiro segmento:"))

# if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
#     print ("Os segmentos podem formar um triangulo")
    
#     if n1 == n2 == n3:
#         print("equilatero")
        
#     elif n1 != n2 != n3 != n1:
#         print ("escaleno")
        
#     else:
#         print ("isoceles")

# else:
#     print("os segmentos acima não podem formar triangulos")

# n1 = int(input("primeiro segmento:"))
# n2 = int(input("segundo segmento:"))
# n3 = int (input("terceiro segmento:"))

# print("soma", ((2*n1)) * (n2/2))
# print("produto", (3*n1 + n3))
# print("cubo", n3**3) 

# numeros = [1,2,3,4,5,6,7,8,9]

# divisiveis = []
# for numero in numeros:
#     if numero % 3 == 0 or numero % 5 == 0:
#         divisiveis.append(numero)
# print (divisiveis)

# lista1 = [2,4,5,6,8,7]

# lista2 = [4,5,8,9,1,7]

# comuns = []

# for elemento in lista1:
#     if elemento in lista2:
#         comuns.append(elemento)
# print(comuns)

# lista = [1,4,3,6,7,8,9]

# soma = 0

# for numero in lista:
#     if numero% 2 != 0:
#         soma += numero
# print (soma)

                                            
# tupla = (10,4,7,9,17)
# valor_maximo = max(tupla)
# print ( valor_maximo)


# dicionario = {"nome": "joão", "idade":30, "cidade": "são paulo"}

# print(dicionario["nome"])
# print(dicionario["idade"])
# print(dicionario["cidade"])


# dicionario = {"nome": "joão", "idade": 30,"ciadde":"são paulo"}
# for chave, valor in dicionario.items():
#     print(chave, valor)