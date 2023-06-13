# import numpy as np

# m = np.empty((2,2),dtype=float)
# cont=0


# for linhas in range(2):
#     for colunas in range(2):
#         numero= float(input('digite um numero:'))
#         m[linhas][colunas] = numero
#         cont=0
#         if m [linhas][colunas]==0:
#             cont=cont + 1
            
#         listapares=[]
        
#         if m[linhas][colunas] % 2 ==0:
#             listapares.append(m[linhas][colunas])
            
            

        
# print(m)
# print(cont)

# matriz= [[1,2,3,],[4,5,6,],[7,8,9]]
 
# soma=0

# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         soma+=matriz[i][j] 
        
#         print(f'A soma de todos os elementos da matriz é (soma),')   



def idade(maior, menor):
    idade = int(input("digite sua idade"))
    
    if idade < 18:
        print ("menor")
    elif idade > 60:
     print ("idoso")
     
    else:
        print ("maior")
        



























