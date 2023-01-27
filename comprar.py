from tkinter import*
class comprar:
    def __init__(self):
        
        self.pizzas=[
        ["Pizza de carne-R$",33],
        ["Pizza de Queijo-R$",32],
        ["Pizza de Frango-R$",34],
        ["Pizza de Calabresa-R$",30],
        ["Pizza Americana-R$",32],
        ["Pizza de Chocolate-R$",30]
        ]

        self.tela=Toplevel(master=None,background="#781F25")
        self.tela["padx"]=200
        self.tela["pady"]=200

        self.titulo=Label(self.tela,text="CARDAPIO PIZZAS FEITAS",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","bold")
        self.titulo.pack()

        self.cardapio=Label(self.tela,text="\n1.Pizza de carne-R$35\n2.Pizza de Queijo-R$32\n3.Pizza de Frango-R$34\n4.Pizza de Calabresa-R$30\n5.Pizza Americana-R$32\n6.Pizza de Chocolate-R$30\n",background="#781F25",foreground="white",bd=3,relief="solid")
        self.cardapio["font"]=("Times new Roman","10","bold")
        self.cardapio.pack()

        self.botao_comprar=Button(self.tela,text="COMPRAR",background="#B50011",foreground="white")
        self.botao_comprar["font"]=("Times new Roman","10","bold")
        self.botao_comprar.config(width=100)
        self.botao_comprar["command"]
        self.botao_comprar.pack()

        self.botao_fechar=Button(self.tela,text="FECHAR",background="#90A74C",foreground="white")
        self.botao_fechar["font"]=("Times new Roman","10","bold")
        self.botao_fechar.config(width=100)
        self.botao_fechar["command"]= self.tela.destroy
        self.botao_fechar.pack()

    #def mostrar_cardapio(self):
        #for x in range(len(self.pizzas)):
            #self.mensagem["text"]=self.pizzas[x]

