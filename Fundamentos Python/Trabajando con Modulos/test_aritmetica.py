#Cuando un modulo esta en la misma carpeta
import Modulo_Aritmetica as Aritmetica


#Cuando un modulo esta en otra carpeta

#Opcion 1 "from <Folder> import <File>"
from Modulos import Modulo_Aritmetica2 as Aritmetica2

#Opcion 2 "import <Folder>.<File>"
import Modulos.Modulo_Aritmetica3 as Aritmetica3

resultado = Aritmetica.suma(6, 2)
print(resultado)

resultado = Aritmetica2.restar(6, 2)
print(resultado)

resultado = Aritmetica3.multiplicar(6, 2)
print(resultado)