#importando tudo do modulo
import matematica

#importando elementos especifios do modulo
from matematica import PI, somar, subitrair
#from matematica import * ==>  importa tudo tamém!
#from matematica import somar as somar_mat, PI as PI_MAT



PI = 99999

num = int(input("n1: \n"))
num2 = int(input("n2: \n"))

print(matematica.somar(num, num2))

from estatistica.descritiva import media, maximo, minimo
from estatistica.inferencial import VALOR

