from classpizza import*

class pizzadoce(pizza):
    def __init__(self,sabor,preco,chocolate=bool):
        pizza.__init__(self, sabor,preco)
        self.chocolate=chocolate  