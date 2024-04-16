#Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite 
# uma palavra ou frase e verifique se é um palíndromo (ou seja, 
# pode ser lida de frente para trás e de trás para frente da mesma forma).


def verificapalindromo (frase): 
    if frase == frase[::-1]:
        palindromo = True
    else:
        palindromo = False
    return palindromo
         

frase = input("insira uma frase:\n")
frase = (frase.lower())
frase = frase.replace(' ', '')

palindromo = verificapalindromo(frase)

if palindromo == True:
    print("é um palíndromo")
else:
    print("não é um palíndromo")