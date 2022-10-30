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
        self.cuenta = CuentaBancaria(tasa_interes=0.02, balance=0)	# añadió esta línea
    # Métodos de instancia
    def hacer_deposito(self,amount):
        self.cuenta.deposito += amount
        return self  # Permite repetir operaciones en la misma linea ej: rta.hacer_deposito(100).hacer_deposito(20).hacer_deposito(50)
    
    # hacer_retiro(self, amount): haz que este método reduzca el balance del usuario en la cantidad especificada 
    def hacer_retiro(self,amount):
        if self.cuenta.balance-amount>0:
            self.cuenta.balance-=amount
        else:
            return 'Sin saldo suficiente'
    #mostrar_balance_usuario(self): haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
    def mostrar_balance_usuario(self):
        print('Usuario: '+self.name+' ,Balance:' +str(self.cuenta.balance))

    # BONUS: transfer_dinero(self, other_user, amount): haz que este método reduzca el balance del usuario por el monto y agrega esa cantidad al balance de otro_usuario 
    def transferencia_dinero(self,other_user,amount):
        if type(other_user) is not Usuario:
            print('Usuario no existe')
        else:
            if self.cuenta.balance-amount>0:
                self.cuenta.retiro(amount)
                other_user.cuenta.deposito(amount)
            else:
                print('Sin Saldo suficiente')


RTA = Usuario('RTA','RTA@gma')
GVE = Usuario('GVE','GVE@gma')

RTA.cuenta.deposito(100).deposito(200).retiro(100).generar_interes().mostrar_info_cuenta()



