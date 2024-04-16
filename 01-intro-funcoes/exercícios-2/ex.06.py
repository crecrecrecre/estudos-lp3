
def conversor(pont):
    if pont >= 0 and pont <60:
        nota = "F"
    elif pont >= 60 and pont <70:
        nota = "D"
    elif pont >=70 and pont <80:
        nota = "C"
    elif pont >=80 and pont <90:
        nota = "B"
    elif pont >=90 and pont <=100:
        nota = "A"
    return nota
        
pont = int(input("digite a pontuação de 0 a 100\n"))
nota = conversor(pont)

print(f"a nota convertida é {nota}")