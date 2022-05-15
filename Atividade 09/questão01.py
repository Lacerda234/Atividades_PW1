class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 21
        self.marca = "sony"
    def muda_canal_para_baixo(self):
        self.canal -= 1
    def muda_canal_para_cima(self):
        self.canal += 1

tv1 = Televisao()
tv1.tamanho = 50
tv1.marca = 'Samsung'

tv2 = Televisao()
tv2.tamanho = 65
tv2.marca = 'LG'

print('Primeira tv: marca %s e tamanho %i polegadas'%(tv1.marca, tv1.tamanho))
print('Segunda tv: marca %s e tamanho %i polegadas'%(tv2.marca, tv2.tamanho))