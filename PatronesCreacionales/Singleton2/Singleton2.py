# Pasillas Luis Miguel Angel            08/Sep/17
# MAE Rene Solis Reyes                  Patrones de Diseño

# Patron Singleton


# Obetivo general: 
# Es una clase que solo se puede crear una instancia (objeto), normalmente se puede 
# acceder desde cualquier lugar del programa. Suele utilizarse para almacenar informacion
# global como datos globales.

# En el ejemplo de abajo le damos un valor asignado a la instancia de 5, 
# luego instanciamos al mismo objeto con un nuevo valor 7. Ahora revisamos
# los valores de los dos objetos creados y ambos tienen el ultimo mismo numero
# dado que es 7. Solo puede existir una instancia y en este caso la ultima que se creo.

class MySingleton:    
    _inner=None
    class inner:
        def __init__(self):
            self.num=None
    def __init__(self):
        if MySingleton._inner is None:
            MySingleton._inner=MySingleton.inner()
    def __getattr__(self, name):
        return getattr(self._inner, name)
    def __setattr__(self, name, value):
        return setattr(self._inner, name, value)
            


first=MySingleton()
first.num=5
print (first.num)

second=MySingleton()
second.num=7
print (second.num)
print (first.num)


# salida:
# 5
# 7
# 7