class Masina:
    def __init__(self,marca):
        self.marca=marca
        self.viteza=0
        self.pornita = False
    def porneste(self):
        self.pornita= True
        print("Masina e pornita")
    def opreste(self):
        self.pornita = False
        self.viteza = 0
        print("Masina e oprita")
    def accelereaza(self, valoare):
        if self.pornita:
            self.viteza += valoare
        else:
            print("Masina este oprita")




m1 = Masina("Audi")
m1.accelereaza(20)
m1.porneste()
m1.accelereaza(20)
print(m1.viteza)

m1.opreste()
print(m1.viteza)