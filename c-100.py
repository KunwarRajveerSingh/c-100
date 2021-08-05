class Car:
    def __init__(self,model, color, company, speedlimit):
        self.color = color
        self.model = model
        self.company = company
        self.speedlimit = speedlimit
    
    def start(self,model):
        print(model,'started')
        print(self.model,'started')
    def stop(self,model):
        print(model,'is stop')
    def accelerate(self,speedlimit):
        print('accelerating to',speedlimit)
    def changeGear(self,gear):
        print('gear changed to',gear)

audi = Car('a6','red','audi','280')
print(audi.model)
print(audi.color)
print(audi.company)
print(audi.speedlimit)

audi.start('Q2')
audi.stop(audi.model)
audi.accelerate(240)
audi.changeGear(4)



        
