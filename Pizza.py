import time
class pizza:
    def __init__(self,tamanho,vinicial,pizzafinal):
        self.tamanho=tamanho
        self.vinicial=vinicial
        self.pizzafinal=pizzafinal
    def fazer_pizza(self):
        self.tamanho=input("Qual o tamanho da pizza?(M ou G)").upper()

        if self.tamanho=="M":
            self.vinicial+=20.00
        elif self.tamanho=="G":
            self.vinicial+=25.00

        ingredientes=[
        ["Molho",1],
        ["Muçarela",1.3],
        ["Palmito",1],
        ["Milho",1],
        ["Bacon",3],
        ["Presunto",2],
        ["Orégano",1],
        ["Carne de sol",4],
        ["Cheddar",1]
        ]

        pizza=[]
        for c  in range (9):
          adicionar=(input("Deseja adicionar {} a sua pizza?(s/n)".format(ingredientes[c][0]))).lower()
          if adicionar=="s":
              self.vinicial+=ingredientes[c][1]
              pizza.append(ingredientes[c][0])
              time.sleep(1)
          elif adicionar=="n":
            print("Okay. Próximo ingrediente...")
            time.sleep(1)
          else:
            print("Erro.Ingrediente não adicionado!")
        print("O valor da sua pizza saiu de: R$ {}".format(self.vinicial))
        print("Com os ingredientes:")
        for c in range(len(pizza)):
            print(pizza[c])
        return pizza==self.pizzafinal

pizzza=pizza("",0,"")
pizzza.fazer_pizza()