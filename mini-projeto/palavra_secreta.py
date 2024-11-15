import random
import os
import time

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

        tempo_inicio = time.time()

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

            if self.contagem == 15:
                for letra in self.palavra_secreta:
                    if letra not in self.letras_acertadas:
                        self.letras_acertadas += letra
                        break

            if self.contagem == 25:
                for letra in self.palavra_secreta:
                    if letra not in self.letras_acertadas:
                        self.letras_acertadas += letra
                        break

            if self.contagem == 40:
                for letra in self.palavra_secreta:
                    if letra not in self.letras_acertadas:
                        self.letras_acertadas += letra
                        break

            self.palavra_formada = ''
            for self.letra_secreta in self.palavra_secreta:
                if self.letra_secreta in self.letras_acertadas:
                    self.palavra_formada += self.letra_secreta
                else:
                    self.palavra_formada += '*'
                
    
            os.system('clear')
            if self.contagem == 15:
                print('Já se foram 15 tentativas, vou te ajudar!!') 
            if self.contagem == 25:
                print('Burro??? Já se foram 25 tentativas, vou te dar mais uma letra.') 
            if self.contagem == 40:
                print('40 tentativas, sério? Nunca mais joga isso, vou te dar a ultima letra.')

            print(f'Palavra formada: {self.palavra_formada}')
        

            if self.palavra_formada == self.palavra_secreta:
                os.system('clear')
                
                tempo_final = time.time()
                tempo_gasto = tempo_final - tempo_inicio

                print('Parabéns, você ganhou!')
                print(f'A palavra era "{self.palavra_secreta}"')
                print(f'{self.contagem} tentativas')
                print(f'Tempo gasto: {tempo_gasto:.2f} segundos')
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
            self.palavras_secretas += 'throw', 'through', 'abroad', 'knowledge', 'environmental'
        else:
            print('digite um nível válido')
        self.palavra_secreta = random.choice(self.palavras_secretas)
    
    def traducao(self):
        traducoes = {
            'hello': 'Olá',
            'thank you': 'Obrigado',
            'nice': 'Legal',
            'good': 'Bom',
            'bad': 'Ruim',
            'easy': 'Fácil',
            'table': 'Mesa',
            'wood': 'Madeira',
            'maybe': 'Talvez',
            'because': 'Porque',
            'beautiful': 'Bonito',
            'notebook': 'Caderno',
            'backpack': 'Mochila',
            'weird': 'Estranho',
            'outside': 'Fora',
            'church': 'Igreja',
            'health': 'Saúde',
            'noise': 'Barulho',
            'throw': 'Arremessar',
            'through': 'Através',
            'abroad': 'Exterior',
            'knowledge': 'Conhecimento',
            'environmental': 'Ambiental',
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
        
def selecionar_tema():
    print(
            'Olá, bem-vindo ao jogo PALAVRA SECRETA, o objetivo desse jogo é você conseguir acertar qual a palavra que está\nescondida na menor quantidade de tentativas possiveis'
            )
    print("Escolha o tema do jogo:")
    print("1 - Faculdade")
    print("2 - Inglês")
    print("3 - Países")

    while True:
        try:
            tema = int(input("Escolha o tema: "))
            if tema in [1, 2, 3]:
                os.system('clear')
                return tema
            else:
                print("Tema inválido. Escolha entre 1 e 4.")
        except ValueError:
            print("Por favor, insira um número válido.")

def selecionar_nivel():
    print("Escolha o nível de dificuldade")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    print("4 - Muito Difícil")

    while True:
        try:
            nivel = int(input("Escolha o tema: "))
            if nivel in [1, 2, 3, 4]:
                os.system('clear')
                return nivel
            else:
                print("Nível inválido. Escolha entre 1 e 4.")
        except ValueError:
            print("Por favor, insira um número válido.")

tema_jogo = selecionar_tema()
nivel_jogo = selecionar_nivel()

if tema_jogo == 1:
    jogo = Faculdade(nivel_jogo)
    jogo.jogar()
elif tema_jogo == 2:
    jogo = Ingles(nivel_jogo)
    jogo.jogar()
elif tema_jogo == 3:
    jogo = Paises(nivel_jogo)
    jogo.jogar()
else:
    print("Não era pra chegar aqui")
    exit()


