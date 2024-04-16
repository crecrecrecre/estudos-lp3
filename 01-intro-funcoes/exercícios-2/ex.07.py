#Ex07 - Jogo da Forca: Implemente uma versão simples do jogo da forca. 
# O programa começa com uma palavra oculta (o usuário não vê) e o usuário
# tenta adivinhar a palavra, letra por letra. O usuário tem um número limitado 
# de tentativas para adivinhar toda a palavra.

import random

def escolherpalavra ():
    palavras = ["arvore", "boneca", "claro", "farofa", "goiaba", "igreja", "jujuba"]
    return random.choice(palavras)

palavra=escolherpalavra() 
letras_usuario = []
chances = 5
ganhou = False

print("\n\nFORCA\n\n")

while True:
    
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    
    
    print(f"adivinhe a palavra (você tem {chances} chances)")
    letrat = input("insira uma tentativa: ")
    letras_usuario.append(letrat.lower())
    if letrat.lower() not in palavra.lower():
        chances = chances - 1
        
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False
        
    if chances == 0 or ganhou == True:
        break
        
    
if ganhou:
    print(f"parabens, voce ganhou!! a palavra era {palavra}")
else:
    print(f"voce perdeu!! a palavra era {palavra}")