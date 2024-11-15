class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def imprimir(self):
        print(f'Minha coordenada x é: {self.x}')
        print(f'Minha coordenada y é: {self.y}')
pt = Point(2, 3)
pt.imprimir()

# class Color:
#     def __init__(self, cor):
#         self.cor = cor
#     def set_cor(self):
#         cores = ['black','red','blue']
#         if self.cor in cores:
#             print(self.cor)
#         else:
#             print(cores[0])

# qual_cor = Color('preto')
# qual_cor.set_cor()
        

