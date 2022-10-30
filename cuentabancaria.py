# CUENTA

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


# USUARIO
class Usuario:
    #Atributo de clase
    nombre_banco='Primer Dojo Nacional'
    lista_cuentas={}
    
    # Atributos de instancia
    def __init__(self,name,email):
        self.name= name
        self.email= email
        self.cuenta = CuentaBancaria(tasa_interes=0.02, balance=0)
        self.total_cuentas= {'cuenta_0':self.cuenta}
    
    # Métodos de instancia
    def crear_nueva_cuenta(self,nombre_cuenta):
        self.total_cuentas[nombre_cuenta]=CuentaBancaria(tasa_interes=0.02, balance=0)

    def hacer_deposito(self,amount,nombre_cuenta='cuenta_0'):
        self.total_cuentas[nombre_cuenta].deposito(amount)
        return self
    
    # hacer_retiro(self, amount): haz que este método reduzca el balance del usuario en la cantidad especificada 
    def hacer_retiro(self,amount,nombre_cuenta='cuenta_0'):
        if self.total_cuentas[nombre_cuenta].balance-amount>=0:
            self.total_cuentas[nombre_cuenta].retiro(amount)
        else:
            return 'Sin saldo suficiente'
    #mostrar_balance_usuario(self): haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
    def mostrar_balance_usuario(self,nombre_cuenta):
        print('Usuario: '+self.name+' ,Balance:' +str(self.total_cuentas[nombre_cuenta].balance))

    # BONUS: transfer_dinero(self, other_user, amount): haz que este método reduzca el balance del usuario por el monto y agrega esa cantidad al balance de otro_usuario 
    def transferencia_dinero(self,other_user,amount,nombre_cuenta='cuenta_0'):
        if type(other_user) is not Usuario:
            print('Usuario no existe')
        else:
            if self.total_cuentas[nombre_cuenta].balance-amount>0:
                self.total_cuentas[nombre_cuenta].retiro(amount)
                other_user.cuenta.deposito(amount)
            else:
                print('Sin Saldo suficiente')



RTA = Usuario('RTA','RTA@gma')
GVE = Usuario('GVE','GVE@gma')

RTA.crear_nueva_cuenta('cuenta2')

RTA.hacer_deposito(100,'cuenta_0').hacer_deposito(100,'cuenta2').total_cuentas['cuenta2'].generar_interes()
RTA.total_cuentas['cuenta2'].balance

RTA.transferencia_dinero(GVE,100,'cuenta2')
RTA.total_cuentas['cuenta2'].balance

RTA.total_cuentas['cuenta2'].balance


RTA.hacer_deposito(100,'cuenta_0')

RTA.total_cuentas['cuenta2'].deposito(100).mostrar_info_cuenta()




RTA.cuenta.deposito(100).deposito(200).retiro(100).generar_interes().mostrar_info_cuenta()



