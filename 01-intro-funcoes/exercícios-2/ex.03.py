#Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para 
# digitar uma frase e retorne o número de vogais e consoantes na frase.



def cont (fr):
    
    vo = 0
    co = 0 
    
    for i in list(fr):
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" :
            vo= vo+1
        elif i.isalpha():  
            co= co+1
    return vo, co
    


f = input("insira uma frase:\n")
fr = (f.upper())

v, c = cont(fr)

print(f"numero de vogais é {v}")
print(f"numero de consoantes é {c}")
