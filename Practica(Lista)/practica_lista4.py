# 4. Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista. 

from ClaseLista import List
from typing import Any, Optional

lista_abc = List()

lista_abc.append("a")
lista_abc.append("b")
lista_abc.append("f")
lista_abc.append("c")
lista_abc.append("g")

lista_abc.insert_value("d",3)
lista_abc.insert_value("r",len(lista_abc))

lista_abc.show()