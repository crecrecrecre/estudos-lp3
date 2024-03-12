#if
idade = 20

#if condicao
#cod
#cod
#cod


if idade>=18:
    print("maior de idade")
    


#IF ELSE


if idade>=18:
    print("maior de idade")
else :
    print("menor")
    
    

#if/elif/else

#crianca = 0 -12
#adolescente = 13 a 17
#adulto = 18 a 59
#idoso = 60+

if idade <= 12:
    print("crianca")
elif idade<= 17:
    print("adolescente")
elif idade <= 59:
    print("adulto")
else:
    print("idoso")



#if aninhado
email = "lalala@gmail.com"
senha = "123"

if email == "lalala@gmail.com":
    if senha == "123":
        print ("acesso permitido")
    else:
        print("invalido")
else:
    print("invalido")






if email == "lalala@gmail.com" and senha == "123":
    print ("acesso permitido")
else:
    print ("invalido")

#entrada numero
#1-domingo
#2-segunda
#3-terça
#4-quarta
#5-quinta
#6-sexta
#7-sabado

dia = 4


if dia == 1:
    print("domingo")
elif dia == 2:
    print("segunda")
#pipipi


#exxx

dias = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sabado"
}

if dia in dias:
    print (dias[dia])


