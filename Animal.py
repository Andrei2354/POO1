class animal:

    """
    1. ¿Que palabra reservada se utiliza en lugar de animal(nombre de la clase) al atributo patas?
    2.¿Qué palabra reservada hay que utilizar para crear un nuevo objeto?

    """
    #patas = 0 #atributo

    def caminar(self):  #metodo
        self.patas = 0 #atributo
        print("caminando", self.patas ,"patas")


def main():
    vaca = animal()
    vaca.patas = 4
    vaca.caminar()

    pato = animal()
    pato.patas = 2
    pato.caminar()

    

if __name__ == "__main__":
    main()