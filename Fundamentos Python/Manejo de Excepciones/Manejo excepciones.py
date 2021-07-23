from Clases_Excepciones import NumerosIdenticosException

try:
    10/0
except: #equivalente a Catch()
    print("Ocurrio un error")
    
try:
    10/0
except Exception as e:
    print("Ocurrio un error:" , e)

print("- - - ")

resultado = None
try:
    a = int(input("Primer Numero: "))
    b = int(input("Segundo Numero: "))
    resultado = a / b
    
    if a == b:
        raise NumerosIdenticosException("Ocurrio un error, numeros identicos")
    
    print("Resultado: ", resultado)
except ZeroDivisionError as e:
    print("Ocurrio un error", type(e))
except TypeError as e:
    print("Ocurrio un error", type(e))
except ValueError as e:
    print("Ocurrio un error", type(e))
except Exception as e:
    print("Ocurrio un error", type(e))
else:
    print("No hubo ningun error")
finally: # Siempre se va a ejecutar
    print("Fin del menejo de excepciones")