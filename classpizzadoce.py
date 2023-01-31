from classpizza import*
class pizzadoce(pizza):

    def __init__(self,sabor,preco,chocolate=str):
       pizza.__init__(sabor,preco)
       self.chocolate=chocolate

       
    