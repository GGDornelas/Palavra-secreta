class Pencil:
    def __init__(self, x='black'):   # init apaga o cache automaticamente
        self._cor = x

    def set_cor(self, cor):
        cores = ['black', 'red', 'blue']
        self._cor = cor if cor in cores else 'black'
                 
    def escrever(self, txt):
        print(f'minha cor é {self._cor} e o txt é {txt}')

    def get_cor(self):
        return self._cor
    
