class CuentaBancaria:
    todas_las_cuentas=[]

    def __init__(self, tasa_interes, balance): 
        self.tasa_interes=tasa_interes
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito(self, amount):
        self.balance+=amount
        return self

    def retiro(self, amount):
        if self.balance-amount>=0:
            self.balance-=amount
            return self
        else:
            print('Fondos Insuficientes')
            
    def mostrar_info_cuenta(self):
        print('Balance cuenta : '+str(self.balance))

    def generar_interes(self):
        if self.balance>0:
            self.balance = self.balance*(1+self.tasa_interes)
            return self
    
    @classmethod
    def lista_cuentas(cls):
        for j in cls.todas_las_cuentas:
            print(j)



cuenta_1 = CuentaBancaria(0.1,100)
cuenta_2 = CuentaBancaria(0.3,20)


cuenta_1.deposito(100).deposito(100).deposito(100).generar_interes().mostrar_info_cuenta()
cuenta_2.deposito(100).deposito(100).retiro(150).retiro(10).generar_interes().mostrar_info_cuenta()

CuentaBancaria.todas_las_cuentas
