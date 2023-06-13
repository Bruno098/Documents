# import numpy as np
# matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print ( matriz)



# import numpy as np

# linha = int(input("digite o numero de linhas:"))
# matrizvazia = np.empty ((linha,linha))

# matrizvazia [0] [0] = 1
# matrizvazia [0] [1] = 2
# matrizvazia [0] [2] = 3
# matrizvazia [1] [0] = 4
# matrizvazia [1] [1] = 5
# matrizvazia [1] [2] = 6
# matrizvazia [2] [0] = 7
# matrizvazia [2] [1] = 8
# matrizvazia [2] [2] = 9
# print(matrizvazia)


# linhas = int(input("digite o numero de linhas na matriz:"))
# colunas = int(input("digite o numero de colunas na mtariz:"))

# matriz = [[0 for j in range(colunas)] for i in range (linhas)]

# for i in range (linhas):
#     valor = int(input("digite o valor para o elemento [(i)] [(j)]"))
#     matriz[i] [j] = valor

# import numpy as np
# count = 0
# matriz_vazia = np.empty ((2,2))
# for i in range (2):
#     for e in range (2):
#         valor = int(input("Digite o numero:"))
        
#         matriz_vazia [i] [e] = valor
#         if matriz_vazia [i] [e] == 0:
    
#            count = count +1
     
# print(count)
    
    
# def idade (i):
#     if i < 18:
#         print ("de maior")
        
#     else:
#         print ("de menor")
        
# idade (18)

# import math
# def idade():
#     i = int(input("digite sua idade:"))
    
#     if i <= 18:
#         print ("menor de idade")
#     elif i >= 60:
#         print ("idoso")
     
#     else:
#         print ("maior de idade")
        
# idade()
        
# ----------------------------------

# def checarpar (n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False 
    
# checarpar (20)
#  ___________________________________

# def bhaskara (a,b,c):
#     delta = (b**2) - (4*a*c)
    
#     x1 = ((-1)*b) + (delta**0.5)/(2*a)
    
#     x2 = ((-1)*b) + (delta**0.5)/(2*a)
#     if delta == 0:
#         print()
#         print("equação do segundo grau:" ",a," ".x²".b,".x",c,"= 0")
#         print ("como delta = 0, temos um único valor de raiz (x1 = x2):",x1)
#     elif delta > 0:
#         print()
#         print("equação do segundo grau:" ",a," ".x²".b,".x",c,"= 0")
#         print ("como delta > 0, temos dois valores distintos de raizes:",x1,"e", x2)
#     else:
#         print()
#         print("equação do segundo grau:" ",a," ".x²".b,".x",c,"= 0")
#         print ("como delta > 0, temos dois valores distintos de raizes:",x1,"e", x2)
        
#         a = 2
#         b = 3
#         c = 10
       
# bhaskara (2,3,10)
               
#   _____________________________________________

# Função que diz se o aluno foi aprovado ou reprovado

# def aprovadoereprovado (n1,n2,n3):
#      media = (n1 + n2 + n3)/3
     
#      if media < 7:
#          print ("reprovado")
#      else:
#          print ("Aprovado!!!!!!!")
         
# aprovadoereprovado (3,3,7)

# ______________________________________________________________________
   
   
#    FUNÇÃO PRA SABER AS HORAS TRABALHADAS E O SALARIO TOTAL NO MÊS

# def salariototal ():
    
    
#     valor = float(input("Digite o valor que você ganha por hora:"))
    
#     horas = int (input("Digite suas horas trabalhadas no mês:"))
#     salariototal = valor * horas


#     print (" O salariototal é:", salariototal)

# ____________________________________________________

# def grausf ():
    
#     f = float(input("Digite a temperatura:"))
#     c = 5 * ((f-32) / 9)
    
#     print("A temperatura em celsius é:",c)
#     return c
# grausf()  
    
    
# def pesoideal ():
    
#     h = float(input("Digite a sua altura:"))
#     sexo = input ("Digite seu genero (M para masculino, F para feminino)")
    
#     if sexo == "M":
#         pesoM = (72.7*h) - 58
#         print ("O peso ideal é:", pesoM)
        
#     elif sexo == "F":
#         pesoF = (62.1*h) - 44.7
#         print ("O peso ideal é:", pesoF)

     

funcionarios={}
 
def cadastrar_funcionario():
    nome=input('digite o nome do funcionario:')
    idade=int(input('digite a idade do funcionario:'))
    cargo=input('digite o cargo do funcionario:')  
    salario=float(input('digite o salario do funcionario:'))
    
    funcionario = {
        'nome':nome,
        'idade':idade,
        'cargo':cargo,
        'salario':salario,
    } 
    funcionario[nome] =funcionario
    print('funcionario cadastrado com sucesso')  
        

def exibir_funcionario():
    nome=input('digite o nome do funcionario:') 
    
    if nome in funcionarios:
        funcionario=funcionarios[nome]
        print('dados do funcionario:')
        print('nome:',funcionario['nome'])
        print('idade:',funcionario['idade'])
        print('cargo:',funcionario['cargo'])
        print('salario:',funcionario['salario'])
    else:
        print('funcionarios não encontrados!')
 
def exibir_funcionarios():
    if funcionarios:
        print('lista de funcionarios:')
        for nome,funcionario in funcionarios.item():
            print('nome:',funcionario['nome'])
            print('idade:',funcionario['idade'])
            print('cargo:',funcionario['cargo'])
            print('salario:',funcionario['salario'])
            print('----------------------')
    else:
        print('não há funcionarios cadastrados!')        

def remover_funcionários():
    nome = input ("Digite digite o nome do funcionário:")
    
    if nome in funcionarios:
        del funcionarios [nome]
        print ("Funcionario removido com sucesso")
      
    else: 
        print ("Funcionario não encontrado")
        
while True:
    
    print ("/n Sistema de cadastro de funcionarios ===")
    print ("1 _ cadastrar funcionario")
    print ("2 _ exibir dados de um funcionario")
    print ("3 _  Exibir todos os funcionarios cadastrados")
    print ("4 _Remover funcionario")
    print ("0 _ Sair")
    
    opcao = input ("Digite a opcao desejada:")
        
    if opcao == "1":
        cadastrar_funcionario ( )
    elif opcao == "2":
        exibir_funcionario( )
    elif opcao == "3":
        exibir_funcionarios ( )
    elif opcao == "4":
        remover_funcionários ()
    elif opcao == "0":
        break
    else:
        print ("Opcçao invalida! Digite novamente.")
    

    
    


    
    








        
    
   