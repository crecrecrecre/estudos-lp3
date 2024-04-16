#Ex02 - Tabuada de Um Número: Solicite ao usuário um número 
# e exiba a tabuada desse número de 1 a 10.

n = int(input ("insira o numero para calcular a tabuada\n"))
print(f"TABUADA DO {n}:\n")

def calculotabuada (n):
   for i in range(1,11):
        m = i * n
        print (f"{n} x {i} = {m}")
        
        
        
calculotabuada (n)