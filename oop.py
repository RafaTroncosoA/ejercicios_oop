class Usuario:
    #Atributo de clase
    nombre_banco='Primer Dojo Nacional'
    
    # Atributos de instancia
    def __init__(self,name,email):
        self.name= name
        self.email= email
        self.balance_cuenta=0
        self.movimientos = []
    # Métodos de instancia
    def hacer_deposito(self,amount):
        self.balance_cuenta += amount
        self.movimientos.append(amount)
        return self  # Permite repetir operaciones en la misma linea ej: rta.hacer_deposito(100).hacer_deposito(20).hacer_deposito(50)
    # hacer_retiro(self, amount): haz que este método reduzca el balance del usuario en la cantidad especificada 
    def hacer_retiro(self,amount):
        if self.balance_cuenta-amount>0:
            self.balance_cuenta-=amount
            self.movimientos.append(-amount)
        else:
            return 'Sin saldo suficiente'
    #mostrar_balance_usuario(self): haz que este método imprima el nombre del usuario y el balance de cuenta en la terminal 
    def mostrar_balance_usuario(self):
        print('Usuario: '+self.name+' ,Balance:' +str(self.balance_cuenta))

    # BONUS: transfer_dinero(self, other_user, amount): haz que este método reduzca el balance del usuario por el monto y agrega esa cantidad al balance de otro_usuario 
    def transferencia_dinero(self,other_user,amount):
        if type(other_user) is not Usuario:
            print('Usuario no existe')
        else:
            if self.balance_cuenta-amount>0:
                self.hacer_retiro(amount)
                other_user.hacer_deposito(amount)
            else:
                print('Sin Saldo suficiente')


rta = Usuario('RTA','rta@gmail.com')
gve = Usuario('GVE','gve@gmail.com')
lts = {}

rta.hacer_deposito(100)
rta.balance_cuenta
rta.hacer_deposito(20).hacer_deposito(10)
rta.mostrar_balance_usuario()

rta.transferencia_dinero(gve,100)
rta.transferencia_dinero(lts,20)

rta.balance_cuenta
rta.transferencia_dinero(gve,50)

rta.balance_cuenta
rta.movimientos
rta.hacer_retiro(20)
rta.balance_cuenta
rta.hacer_retiro(200)
rta.movimientos


