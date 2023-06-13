def idade(maiordeidade, menordeidade):
    idade = int(input("digite sua idade"))
    
    if idade <= 18:
        print ("menor de idade")
    elif idade >= 60:
     print ("idoso")
     
    else:
        print ("maior de idade")
        