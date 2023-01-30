from tkinter import*
from comprar import*
from tkinter import ttk
from pickle import*
from classpizzadoce import*
from classpizza import*

class telaadm(comprar):
    def __init__(self):

        self.tela=Toplevel(background="#781F25")
        self.tela["padx"]=200
        self.tela["pady"]=200

        self.titulo=Label(self.tela,text="Espaço administrativo",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","bold")
        self.titulo.pack()

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

        self.tipos=["Pizza comum","Pizza doce"]

        self.textcaixa=Label(self.tela,text="Tipo da pizza:",background="#781F25",foreground="white")
        self.textcaixa["font"]=("Times new Roman", "15","bold")

        self.caixa=ttk.Combobox(self.tela,values=self.tipos,background="#FF6347",foreground="White")
        self.caixa.pack()

        self.addpizza=Button(self.tela,text="ADICIONAR PIZZA",background="#B50011",foreground="white")
        self.addpizza["font"]=("Times new Roman","10","bold")
        self.addpizza.config(width=40)
        self.addpizza["command"]= self.adicionarpizza
        self.addpizza.pack()

        self.botao_fechar=Button(self.tela,text="FECHAR",background="#90A74C",foreground="white")
        self.botao_fechar["font"]=("Times new Roman","10","bold")
        self.botao_fechar.config(width=40)
        self.botao_fechar["command"]= self.tela.destroy
        self.botao_fechar.pack()

        #self.mensagem1=Label(self.tela,text="",background="#781F25",foreground="white")
        #self.mensagem1["font"]=("Times new Roman", "15","bold")
        #self.mensagem1.pack()
    
    def adicionarpizza(self):
        if self.caixa.get()==self.tipos[0]:

           sabor=self.entradanovapizzas.get()
           preco=self.entradaprecopizza.get()

           p=pizza(sabor,preco)
           self.tabela.insert(text=sabor,values=preco)

           arq=open("cardapio.txt","wb")
           arq.dumps(p,arq)
           arq.close()

        elif self.caixa.get()==self.tipos[1]:

           choconome=Label(self.tela,text="Digite o tipo de chocolate",background="#781F25",foreground="white")
           choconome["font"]=("Times new Roman", "10","bold")
           choconome.pack()

           entradachocolate=Entry(self.tela,background="#FF6347")
           entradachocolate.config(width=48)
           entradachocolate.pack()

           chocolate=entradachocolate.get()
           sabor=self.entradanovapizzas.get()
           preco=self.entradaprecopizza.get()

           p=pizzadoce(sabor,preco,chocolate)

           arq=open("cardapiopizzasdoce.txt","wb")
           arq.dumps(p,arq)
           arq.close()