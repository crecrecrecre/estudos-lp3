#Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número 
# entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao 
# usuário se o palpite está alto ou baixo, até que ele acerte o número.

import random

n = random.randint(1, 100)


def maior(n, palpite):
    if palpite > n:
        return "é mais baixo!!"
    else:
        return ""
        
def menor(n, palpite):
    if palpite < n:
        return "é mais alto!!"
    else:
        return ""
        
        
acertou = False
while not acertou:
    palpite = int(input("palpite de 0 a 100: "))
    
    if palpite < 0 or palpite > 100:
        print("Fora da escala")
        continue
    
    print(maior(n, palpite))
    print(menor(n, palpite))
    
    if palpite == n:
        acertou = True
        
print("achouuu")
        

    
    
