class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []
    def adiciona_cidade(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)
    def populacao(self):
        return sum([c.populacao for c in self.cidades])
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        self.estado = None
    def __str__(self):
        return ('Cidade: %s\nPopulação: %i\nEstado: %s'%(self.nome, self.populacao, self.estado))

pb = Estado('Paraíba', 'PB')
pb.adiciona_cidade(Cidade('Cajazeiras', 61.816))
pb.adiciona_cidade(Cidade('Monteiro', 33.638))
pb.adiciona_cidade(Cidade('Campina Grande', 413.830))

rn = Estado('Rio Grande do Norte', 'RN')
rn.adiciona_cidade(Cidade('Pau dos Ferros', 30.802))
rn.adiciona_cidade(Cidade('Areia Branca', 28.156))
rn.adiciona_cidade(Cidade('Apodi', 35.904))

ce = Estado('Ceará', 'CE')
ce.adiciona_cidade(Cidade('Crato', 133.913))
ce.adiciona_cidade(Cidade('Quixeramobim', 82.455))
ce.adiciona_cidade(Cidade('Icó', 68.303))

for estado in [pb, rn, ce]:
    print('Estado: %s Sigla: %s'%(estado.nome, estado.sigla))
    for cidades in estado.cidades:
        print('Cidade: %s População: %s'%(cidades.nome, cidades.populacao))
    print('População do Estado: %s\n'%estado.populacao())