
#funciones de orden superior
#son funciones combinadas para duvolver un valor
def suma1 (value):
    return value + 1

def sumar2(numero1, numero2):
    return suma1(numero1+numero2)

print(sumar2(5,2))


####################################################################
#clousures
def numeros ():
    def add(value):
        return value + 10
    return add

variable = numeros()
print(variable(5))