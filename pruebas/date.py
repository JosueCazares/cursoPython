#importar hora y fehca

import datetime 

ahora=datetime.datetime.now()
print(ahora)
print(type(ahora))
print()
#diferente tipo de formato
print(ahora.strftime("%d/%m/%Y_%H:%M:%S"))