#Operadores Aritiméticos
# +, -, /, *, %, **

nota1 = 10.0
nota2 = 6.0
nota3 = 5.5

media = (nota1 + nota2 + nota3)/3

numero = 10

elevadoaoquadrado = numero * numero 
elevadoaoquadrado = numero ** 2

#Operadores Lógicos
#and, or, not

print(2+3)
print(True and True)

#permitir a entrada no sistema
#usuario não bloqueado e
#usuário é um funcionário e
#hora atual entre 8 e 18h
#
#caso for adm pode acessar de qualquer forma

usuariobloqueado = False
usuariofuncionario = True
hora = 17
usuarioadmin = False

HorarioComercial = hora >= 8 and hora <= 18 #false

FuncionarioAtivo = usuariofuncionario and not usuariobloqueado

if (FuncionarioAtivo and HorarioComercial) or (usuarioadmin):
    print ("Acesso liberado")
else:
    print ("Acesso não liberado") 



  #  def dentro_horario_comercial (hora):
#        return hora >8and hora <= 18


#Operadores de comparação
# ==, !=, >, <, >=, <=

nota1 = 10.0
nota2 = 5.5

if nota1>nota2:
    print ("foi melhor na 1 tar")
else:
    print ("foi melhor na 2 ou teve a mesma nota nas 2")


#operador is not
#operador de identidade
#comparar se os objetos são os mesmmos
#mesmo espaço na memória

a = [1,2,3]
b = [1,2,3]
print (a==b) #mesmos valores, True

print (a is b)

#in e not in
#usado para verificar se um elemento existe em uma sequencia
#str, list, tupla

opcoes = ('sim', 'nao', 'talvez')
opcao = input("Digite Uma Opcao")


opcao = opcao.lower().strip()#tira maiusculos e espacos


if opcao in opcoes:
    print("Opção disponivellll")
else:
    print("Invalido diva")


