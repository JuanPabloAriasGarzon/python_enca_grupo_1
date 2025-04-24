'''
realizar las importaciones de las funciones segun las 4 variantes vistas 
hacer print a la ejecucion de las funciones importadas
'''

from operaciones import suma, random_number, modulo
print(suma(4,5))

import operaciones as op
print(op.resta(4,5))

from operaciones import *
print(multiplicacion(4,5))

print(division(4,5))

from operaciones import division_piso as dp
print(dp(4,5))

print(random_number())

print(modulo(4,5))