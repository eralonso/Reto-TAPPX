"""
Test 1

def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print(funcion.__name__)
        if (funcion.__name__ == "suma"):
            print("Bien")
        #print("Se va a llamar")
        c = funcion(a, b)
        #print(c)
        #print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    #print("Entra en funcion suma")
    return a + b

print(f"return == {suma(5,8)}")

"""

"""
Test 2

def log(fichero_log):
    def decorador_log(func):
        def decorador_funcion(*args, **kwargs):
            print(*args)
            with open(fichero_log, 'a') as opened_file:
                output = func(*args, **kwargs)
                opened_file.write(f"{output}\n")
        return decorador_funcion
    return decorador_log

@log('ficherosalida.log')
def suma(a, b):
    return a + b

@log('ficherosalida.log')
def resta(a, b):
    return a - b

@log('ficherosalida.log')
def multiplicadivide(a, b, c):
    return a*b/c

suma(10, 30)
resta(7, 23)
multiplicadivide(5, 10, 2)

"""

"""
Test 3

import os
log_messages = [ f"({os.getenv('USER'):})Running: Start Machine      [ exec-time = {2} {'ms'} ]",
            f"({os.getenv('USER'):})Running: Boil Water         [ exec-time = {2} {'ms'} ]",
            f"({os.getenv('USER'):})Running: Make Coffe         [ exec-time = {2} {'ms'} ]"]

for message in log_messages:
    print(message)

"""
