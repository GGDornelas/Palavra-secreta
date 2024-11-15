import random
import os

class Faculdade:
    def __init__(self, nivel):
        self.nivel = nivel
        self.palavras_secretas = []
        self.palavra_secreta = ''
        self.letras_acertadas = ''
        self.letra_digitada = ''
        self.contagem = 0
        if self.nivel == 1:
            self.palavras_secretas += 'aula', 'aluno', 'professor', 'prova'
        elif self.nivel == 2:
            self.palavras_secretas += 'engenharia', 'fisica', 'calculo', 'matricula'
        elif self.nivel == 3:
            self.palavras_secretas += 'laboratorio', 'auditorio', 'discente'
        elif self.nivel == 4:
            self.palavras_secretas += 'scardua', 'obelisco', 'restaurante universitario'
        else:
            print('Não era pra chegar aqui, digite um nível válido')
        self.palavra_secreta = random.choice(self.palavras_secretas)
        

    def objetivo(self):
        print(
            'Olá, bem-vindo ao jogo PALAVRA SECRETA, o objetivo desse jogo é você conseguir acertar qual a palavra que está\nescondida na menor quantidade de tentativas possiveis'
            )

    def jogar(self):
        print(f'Nível escolhido = {self.nivel}')

        while True:
            self.letra_digitada = input('Digite uma letra: ').lower()
            

            if len(self.letra_digitada) > 1:
                print('Digite apenas uma letra')
                continue
            
            self.contagem += 1

            if ' ' in self.palavra_secreta:
                self.letras_acertadas += ' '

            if self.letra_digitada in self.palavra_secreta:
                self.letras_acertadas += self.letra_digitada

            if self.contagem == 10:
                self.letras_acertadas += self.palavra_secreta[0]  # CORRIGIR O FATO DE SE JA TIVER A PRIMEIRA LETRA E DUAS IGUAIS 

            self.palavra_formada = ''
            for self.letra_secreta in self.palavra_secreta:
                if self.letra_secreta in self.letras_acertadas:
                    self.palavra_formada += self.letra_secreta
                else:
                    self.palavra_formada += '*'
                
    
            os.system('clear')
            if self.contagem == 10:
                print('Já foram 10 tentativas, toma a primeira letra') 
            print(f'Palavra formada: {self.palavra_formada}')
        

            if self.palavra_formada == self.palavra_secreta:
                os.system('clear')
                print('Parabéns, você ganhou!')
                print(f'A palavra era "{self.palavra_secreta}"')
                print(f'{self.contagem} tentativas')
                break
        


class Ingles(Faculdade):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.palavras_secretas = []
        if self.nivel == 1:
            self.palavras_secretas += 'hello', 'thank you', 'nice', 'good', 'bad', 'easy'
        elif self.nivel == 2:
            self.palavras_secretas += 'table', 'wood', 'maybe', 'because', 'beautiful', 'notebook', 'backpack'
        elif self.nivel == 3:
            self.palavras_secretas += 'weird', 'outside', 'church', 'health', 'noise'
        elif self.nivel == 4:
            self.palavras_secretas += 'throw', 'through', 'abroad', 
        else:
            print('digite um nível válido')
        self.palavra_secreta = random.choice(self.palavras_secretas)
    
    def traducao(self):
        traducoes = {
            'hello': 'Olá',
            'thank you': 'Obrigado',
            'table': 'Mesa',
            'wood': 'Madeira',
            'maybe': 'Talvez',
            'because': 'Porque',
            'beautiful': 'Bonito',
            'notebook': 'Caderno',
            'backpack': 'Mochila',
            'weird': 'Estranho',
            'outside': 'Lá fora',
            'church': 'Igreja',
            'health': 'Saúde',
            'throw': 'Lançar',
            'through': 'Através',
            'abroad': 'Exterior',
        }
        return traducoes.get(self.palavra_secreta, 'Não tem tradução')
    
    def objetivo(self):
        super().objetivo()
        print('Tema = INGLÊS')

    def jogar(self):
        super().jogar()  
        print(f'Tradução: {self.traducao()}')
    

class Paises(Faculdade):
    def __init__(self, nivel):
        super().__init__(nivel)
        self.palavras_secretas = []
        if self.nivel == 1:
            self.palavras_secretas += 'brasil', 'peru', 'china', 'argentina', 'estados unidos', 'franca', 'alemanha', 'canada'
        elif self.nivel == 2:
            self.palavras_secretas += 'china', 'japao', 'holanda', 'australia', 'grecia', 'turquia', 'egito', 'inglaterra'
        elif self.nivel == 3:
            self.palavras_secretas += 'singapura', 'irlanda do norte', 'argelia', 'tailandia', 'albania', 'marrocos', 'angola', 'nova zelandia', 'afeganistao'
        elif self.nivel == 4:
            self.palavras_secretas += 'chipre', 'alaska', 'etiopia', 'burkina faso', 'azerbaijao'
        else:
            print('digite um nível válido')
        self.palavra_secreta = random.choice(self.palavras_secretas)
    
    
    def objetivo(self):
        super().objetivo()
        print('Tema = PAISES')

    def jogar(self):
        super().jogar()  
        


def selecionar_nivel():
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    print("4 - Muito Difícil")

    while True:
        try:
            nivel = int(input("Digite o número do nível desejado: "))
            if nivel in [1, 2, 3, 4]:
                os.system('clear')
                return nivel
            else:
                print("Nível inválido. Escolha entre 1 e 4.")
        except ValueError:
            print("Por favor, insira um número válido.")

nivel = selecionar_nivel()







faculdade = Faculdade(nivel)
# faculdade.objetivo()
# faculdade.jogar()    

ingles = Ingles(nivel)
# ingles.objetivo()
# ingles.jogar()

paises = Paises(nivel)
paises.objetivo()
paises.jogar()

