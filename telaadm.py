from tkinter import*
class telaadm:
    def __init__(self):

        self.tela=Toplevel(background="#781F25")
        self.tela["padx"]=200
        self.tela["pady"]=200

        self.titulo=Label(self.tela,text="Espaço administrativo",background="#781F25",foreground="white")
        self.titulo["font"]=("Times new Roman", "30","bold")
        self.titulo.pack()