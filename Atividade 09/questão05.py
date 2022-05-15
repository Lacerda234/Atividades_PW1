class Televisao:
    def __init__(self, minimo=2, maximo=14):
        self.ligada = False
        self.canal = minimo
        self.cmin = minimo
        self.cmax = maximo
        self.tamanho = 21
        self.marca = "sony"
    def muda_canal_para_baixo(self):
        if(self.canal-1 >= self.cmin):
            self.canal -= 1
        else:
            self.canal = self.cmax
    def muda_canal_para_cima(self):
        if(self.canal+1 <= self.cmax):
            self.canal += 1
        else:
            self.canal = self.cmin

tv1 = Televisao(1, 32)
tv1.muda_canal_para_baixo()
print(tv1.canal)
tv1.muda_canal_para_cima()
print(tv1.canal)

print('')

tv2 = Televisao(3, 25)
tv2.muda_canal_para_baixo()
print(tv2.canal)
tv2.muda_canal_para_cima()
print(tv2.canal)
