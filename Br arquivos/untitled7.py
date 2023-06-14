senha = input("Digite sua senha:")

tentativas = 0

while senha != "123" and tentativas < 3:
    
    tentativas += 1
    print ("senha incorreta, tente novamente!")
    senha = input("Digite sua senha:")
    
if senha == "123":
    print ("senha correta")
    
else:
    print("numero de tentativas excedeu")

        
