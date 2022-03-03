class Router: 
    def __init__(self, model, swversion, ipadd) :
        self.model = model
        self.swversion = swversion
        self.ipadd = ipadd
    
    def getdesc(self) :
        desc = f'Router model : {self.model}\n' \
            f'Sofware Version : {self.swversion}\n'\
                f'Router Management Address : {self.ipadd}\n'
        
        return desc
    
class Switch(Router): #Inheritance
    def getdesc(self) :
        desc = f'Router model : {self.model}\n' \
            f'Sofware Version : {self.swversion}\n'\
                f'Router Management Address : {self.ipadd}\n'
        
        return desc
    
rtr1 = Router('iosV', '15.6.7', '10.10.10.1')
rtr2 = Router('isr4221', '16.9.5', '10.10.10.5')
sw1 = Switch('Cat9300', '16.9.5', '10.10.10.8')

print('Rtr1\n', rtr1.getdesc(), '\n', sep='')
print('Rtr2\n', rtr2.getdesc(), '\n', sep='')
print('Switch1\n', sw1.getdesc(), '\n', sep='')