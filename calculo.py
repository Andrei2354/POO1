class Calculo:
    def __init__(self, numero1:int, numero2:int):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def aritmeticaSuma(self):
        print(f"El valor de la suma es:", self.numero1 + self.numero2)


    def aritmericaResta(self):
        print(f"El valor de la resta es:",  self.numero1 - self.numero2)


    def aritmericaMult(self):
        print (f"El valor de la multiplicación es:", self.numero1 * self.numero2)


    def aritmericaDiv(self):
        print(f"El valor de la división es: ", self.numero1 / self.numero2)
    


if __name__ == "__main__":
    calculo = Calculo(2 , 2)
    calculo.aritmeticaSuma()
    calculo.aritmericaResta()
    calculo.aritmericaMult()
    calculo.aritmericaDiv()