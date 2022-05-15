class Televisao:
    def __init__(self, minimo, maximo):
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

tv = Televisao(1, 99)
tv.muda_canal_para_baixo()
print(tv.canal)
tv.muda_canal_para_cima()
print(tv.canal)