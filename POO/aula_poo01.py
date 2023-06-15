class Pessoa:
    def __init__(self,nome,idade,cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        
    def apresentar(self):
        print("Ola meu nome é:",self.nome)
        
    def envelhecer(self,anos):
        self.idade += anos
        print(self.idade)
        
    def mostrarcpf (self):
        print ("Este é meu cpf",self.cpf)
        
pessoa1 = Pessoa ("Bruno",25,60480841373)


pessoa1.apresentar ()
pessoa1.envelhecer (2)



        