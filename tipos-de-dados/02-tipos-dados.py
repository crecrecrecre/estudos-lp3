#tipos de dados

#1 numerico
# int, float, complex

#int
idade = 10
temperatura = -30

#float
altura = 178.20

#2 bool
verdade = True
mentira = False

#3 strings
#conjunto (sequencia) de caracteres

nome = 'Maria da Silva'
nome = "Maria da Silva"

#multilinha
frase = """oi mundooooooo
tudo beeeeeeeeeeem
tchaaaaaaaaaaaau
"""

#interpolação
nome = "joao campos" 
idade = 20
#f-strings
frase = f"Ola {nome}. Voce tem {idade} anos!"
print(frase)

#i o char hein
#string de apenas 1 caracter
letra = 'a'
letra = "a"

#acesso a um caraxctere da string

nome= "Silvo"

print (nome[0])
print (nome[-1])
print (nome[-3])

#strings sao objetos
#objetos tem metodos e atribustos

#nome = nome.upper()
#altera o nome pra maiusculo

print(nome.capitalize()) #Silvo

print(nome.upper()) #SILVO

#4 listas
# indexadas
# pode ser alterada

habilidades = []
#vazia
habilidades = ['python', 'html', 'java']

# acesso um item da lista

habilidades[1]

#adicionar um item no final da lista

habilidades.append('c#')#agr a lista eh python, html, java e c#

#inserir em uma posicao especifica
#python html CSS  java e c#

habilidades.insert(2, 'css')
#print (habilidades)

#habilidades.clear()#limpa

#print(habilidades)


#valer a lista

for habilidade in habilidades:
    print (habilidade)

    #pra cada habilidade da lista habilidades, mexibir a habiliade


#5 tuple ou tupla

#uma tupla é uma lista de valores
#não pode ser alterada!!!!!!!

opcoes = ('sim', 'nao', 'sla talvez')
#colchetes são para listas, q podem ser alteradas, já os parentesis são para tuplas, que não podem ser modificadas
print (opcoes[0])

for opcao in opcoes :
    print(opcao)


#set ou conjunto

#conjunto de valores
#não permite elementos duplicados
#não é indexavel

habilidades = {'python', 'java', 'c#', 'java'}
print(habilidades)

#habilidades [i] não vai funcionar

#6 dict (dicionarios)
# palavras ==> definição
# chave ==> valor
#key ==> value
#conjunto chave valor
nome = "Pedro Alves"
idade = 17
habilidades = ['Java', 'c#', 'css']
empregado = True

candidato = {
    'nome': 'Pedro Alves',
    'idade' : 17,
    'habilidades' : ['Java', 'c#', 'css'],
    'empregado' : True

} 

print(candidato ['nome'])

print(candidato.keys())
print(candidato.values())

#None
nome = None






















