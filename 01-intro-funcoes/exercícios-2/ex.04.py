#Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. 
# O programa deve pedir ao usuário para votar várias vezes e, no final,
# mostrar o número de votos de cada candidato e quem foi o vencedor.

def votacao(voto):
    cont1=0
    cont2=0
    cont3=0
    for voto in votos:
        if voto == 1:
            cont1= cont1+1
        elif voto == 2:
            cont2= cont2+1
        elif voto == 3:
            cont3= cont3+1
        
    return cont1, cont2, cont3

votos = []
for i in range(12):
    voto = (int(input("clique 1 para votar no candidato 1, 2 para votar no candidato 2 ou 3 para votar no candidato 3!\n")))
    votos.append(voto)  
        

  
    
c1, c2, c3 = votacao(voto)
    
print(f"foram {c1} votos para o candidato 1")
print(f"foram {c2} votos para o candidato 2")
print(f"foram {c3} votos para o candidato 3")


