'''
Operador    Metodo
+           __add__(self, other)
-           __sub__(self, other)
*           __mul__(self, other)
/           __truediv__(self, other)
//          __floordiv__(self, other)
%           __mod__(self, other)
**          __pow__(self, other)
<           __lt__(self, other)
>           __gt__(self, other)
<=          __le__(self, other)
>=          __ge__(self, other)
==          __eq__(self, other)
!=          __ne__(self, other)
-=          __isub__(self, other)
+=          __iadd__(self, other)
*=          __imul__(self, other)
/=          __idiv__(self, other)
//=         __ifloordiv__(self, other)
%=          __imod__(self, other)
**=         __ipow__(self, other)

Operadores Unarios
-           __neg__(self, other)
+           __pos__(self, other)
~           __invert__(self, other)

'''   
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def __add__(self, otro):
        return self.__nombre + " " + otro.__nombre
    
    def __sub__(self, otro):
        return "Operacion no soportada"

p1 = Persona("Juan")
p2 = Persona("Maria")

print(p1 + p2)