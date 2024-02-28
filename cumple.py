class Persona:

    def __init__(self, nombre, edad,):
        self.nombre = nombre #atributo
        self.edad = edad #atributo  


    def imprimir(self):         
        print("El nombre del cumpleañero es ", self.nombre ,"y tiene", self.edad)


    def cumpleanos(self):
        self.edad += 1
        print("Cumple ", self.edad)

def main():
    daniel = Persona("Daniel", 10)
    daniel.imprimir()
    daniel.cumpleanos()

main()
