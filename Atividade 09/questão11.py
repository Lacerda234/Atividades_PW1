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
    
    def sacar(self, valor):
        return self.saldo >= valor

    def saque(self, valor):
        if self.sacar(valor):
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
    
    def sacar(self, valor):
        return self.saldo + self.limite >= valor
    
    def extrato(self):
        Conta.extrato(self)
        print('Limite: %.2f\n'%(self.limite))
        print('Disponível: %.2f\n'%(self.limite + self.saldo))

leandro = Cliente('Leandro','9999-8888')

conta = ContaEspecial([leandro], 3210, 7000, 10000)
conta.extrato()
conta.saque(8500)
conta.saque(9000)
conta.saque(2000)
conta.extrato()