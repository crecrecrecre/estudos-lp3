#importando tudo do modulo
import matematica

#importando elementos especifios do modulo
from matematica import PI, somar, subitrair
#from matematica import * ==>  importa tudo tamém!
#from matematica import somar as somar_mat, PI as PI_MAT



PI = 99999

print(matematica.PI)
print(matematica.somar(10, 10))

from estatistica.descritiva import media, maximo, minimo
from estatistica.inferencial import VALOR

