class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, número, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print("CC N°%s Saldo: %10.2f" %(self.número, self.saldo))
        for cliente in self.clientes:
            print('Nome: %s\nTelefone: %s\n'%(cliente.nome, cliente.telefone))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            print('Saldo insuficiente!')
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0],o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)

class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo = 0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            return Conta.saque(self, valor)

    def extrato(self):
        Conta.extrato(self)
        print('\nLimite: %.2f \n'%(self.limite))
        print('Disponível: %.2f \n'%(self.limite + self.saldo))

leandro = Cliente('Leandro','9999-8888')
anne = Cliente('Anne','7777-4444')

conta = ContaEspecial([leandro], 123, 4500, 7000)
conta.extrato()