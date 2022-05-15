class Televisao:
    def __init__(self, canal_inicial):
        self.ligada = False
        self.canal = canal_inicial
        self.tamanho = 21
        self.marca = "sony"
    def muda_canal_para_baixo(self):
        self.canal -= 1
    def muda_canal_para_cima(self):
        self.canal += 1