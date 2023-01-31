from tkinter import*
from tkinter import ttk
from pickle import*
from classpizzadoce import*
from classpizza import*

class telaadm:
    def __init__(self):

        self.tela=Toplevel(background="#781F25")
        self.tela["padx"]=100
        self.tela["pady"]=100

        self.titulo=Label(self.tela,text="Espaço administrativo",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","bold")
        self.titulo.pack()

        self.tabela = ttk.Treeview(self.tela, column=("c1", "c2"), show='headings', height=8)
        self.tabela.column("# 1", anchor=CENTER)
        self.tabela.heading("# 1", text="Pizza")
        self.tabela.column("# 2", anchor=CENTER)
        self.tabela.heading("# 2", text="Preço")
        self.tabela.pack()

        self.novapizza=Label(self.tela,text="Digite o nome da pizza que será adicionada:",background="#781F25",foreground="white")
        self.novapizza["font"]=("Times new Roman", "15","bold")
        self.novapizza.pack()

        self.entradanovapizzas=Entry(self.tela,background="#FF6347")
        self.entradanovapizzas.get().lower()
        self.entradanovapizzas.config(width=48)
        self.entradanovapizzas.pack()

        self.preconovapizza=Label(self.tela,text="Digite o preço da pizza:",background="#781F25",foreground="white")
        self.preconovapizza["font"]=("Times new Roman", "15","bold")
        self.preconovapizza.pack()

        self.entradaprecopizza=Entry(self.tela,background="#FF6347")
        self.entradaprecopizza.get().lower()
        self.entradaprecopizza.config(width=48)
        self.entradaprecopizza.pack()

        self.tipos=["Pizza comum","Pizza Doce"]

        self.textcaixa=Label(self.tela,text="Tipo da pizza:",background="#781F25",foreground="white")
        self.textcaixa["font"]=("Times new Roman", "15","bold")

        self.caixa=ttk.Combobox(self.tela,values=self.tipos,width=45)
        self.caixa.pack()

        self.deletepizza=Button(self.tela,text="CARREGAR CARDÁPIO",background="#B50011",foreground="white")
        self.deletepizza["font"]=("Times new Roman","10","bold")
        self.deletepizza.config(width=40)
        self.deletepizza["command"]= self.carregarcardapio
        self.deletepizza.pack()

        self.addpizza=Button(self.tela,text="ADICIONAR PIZZA",background="#B50011",foreground="white")
        self.addpizza["font"]=("Times new Roman","10","bold")
        self.addpizza.config(width=40)
        self.addpizza["command"]= self.adicionarpizza
        self.addpizza.pack()

        self.deletepizza=Button(self.tela,text="EXCLUIR PIZZA",background="#B50011",foreground="white")
        self.deletepizza["font"]=("Times new Roman","10","bold")
        self.deletepizza.config(width=40)
        self.deletepizza["command"]= self.apagarpizza
        self.deletepizza.pack()

        self.botao_fechar=Button(self.tela,text="FECHAR",background="#90A74C",foreground="white")
        self.botao_fechar["font"]=("Times new Roman","10","bold")
        self.botao_fechar.config(width=40)
        self.botao_fechar["command"]= self.tela.destroy
        self.botao_fechar.pack()

        self.mensagem1=Label(self.tela,text="",background="#781F25",foreground="white")
        self.mensagem1["font"]=("Times new Roman", "15","bold")
        self.mensagem1.pack()

    def apagarpizza(self):

      selecao = self.tabela.selection()[0]
      self.tabela.delete(selecao)
      arq= open("cardapio.txt", "wb")
      cardapio=[self.tabela.item(x)['values'] for x in self.tabela.get_children()]
      dump(cardapio,arq)
      arq.close()
  
    def carregarcardapio(self):

        pizzas = []
        arq = open("cardapio.txt", "rb")
        pizzas = load(arq)
        arq.close()
        for item in pizzas:
          self.tabela.insert('','end',values=item)
        
    def adicionarpizza(self):

        if self.caixa.get()==self.tipos[0]:

           sabor=self.entradanovapizzas.get()
           preco=self.entradaprecopizza.get()

           p=pizza(sabor,preco)
           self.tabela.insert('', 'end', values=(sabor,"R$ {0}".format(preco)))

           arq=open("cardapio.txt","ab")
           dump(p,arq)
           arq.close()

           self.mensagem1["text"]=("Você cadastrou uma pizza comum!")

           cardapio=[self.tabela.item(x)['values'] for x in self.tabela.get_children()]
           arq= open("cardapio.txt", "wb")
           dump(cardapio,arq)
           arq.close()
        
        elif self.caixa.get()==self.tipos[1]:

           sabor=self.entradanovapizzas.get()
           preco=self.entradaprecopizza.get()

           p=pizzadoce(sabor,preco,chocolate=True)
           self.tabela.insert('', 'end', values=(sabor,preco))

           arq=open("cardapio.txt","ab")
           dump(p,arq)
           arq.close()
           
           self.mensagem1["text"]=("Você cadastrou uma pizza Doce")

           cardapio=[self.tabela.item(x)['values'] for x in self.tabela.get_children()]
           arq= open("cardapio.txt", "wb")
           dump(cardapio,arq)
           arq.close()
        
          ##Erro ao adicionar pizza do tipo doce