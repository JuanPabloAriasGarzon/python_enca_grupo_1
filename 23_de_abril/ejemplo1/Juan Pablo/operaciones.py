'''
crear las funciones de suma, resta, multiplicacion, division (validar 0 demoninador)
division piso
crear una funcion que genere un numero aleatorio(import random)
crear una funcion operacion modulo (%)
'''

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return 'Error'
    else:
        return a/b


def division_piso(a,b):
    if b == 0:
        return 'Error'
    else:
        return a//b
    
def random_number():
    import random
    return random.randint(1,999)

def modulo(a,b):
    return a % b
