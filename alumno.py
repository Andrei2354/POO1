class alumno:

    def __init__(self, nota, nombre):
        self.nota = nombre #atributo
        self.nombre = nota #atributo  


    def imprimir(self):         
        print("La nota de ", self.nombre ,"es", self.nota)


    def promoción(self):
        if(self.nota >= 5):
            print("promociona")
        else:
            print("No promociona")
