""""
zona sana: ph 6.5-8.5 y ICA menor o igual a 50
Zona moderadamente sana: ph entre 6.5-8.5 ICA 51-100
Zona contaminada nivel 1: ph 6.0-9.0  ICA 101-150
Zona contaminada nivel 2: ph no importa, pero ICA 201- mas300
ph mayor 6 o menors in importar el ICA

promedio de ph de las pruebas del agua
promedio del ICA de las pruebas del aire
"""
phsano = 0
phpromedio = 0
icapromedio = 0
zonas = 0
zonasa = 0
zonams = 0
zonacn1 = 0
zonacn2 = 0

zonasrev = int(input("¿Cuántas zonas vas a revisar?  "))
while zonas < zonasrev:
  PH = float(input("¿Cual es el PH del agua? Recuerda que el PH es entre 0 y 14:  "))
  if PH <= 14 and PH >= 0:
    phpromedio += PH
  if PH > 14:
    print("respuesta invalida")
  elif PH >= 6.5 and PH <= 8.5:
    phsano += 1
  ICA = float(input("¿Cuál es el ICA de la zona?  "))
  if ICA >= 0 and ICA <= 300:
    icapromedio += ICA
  if ICA >= 0 and ICA <= 50:
    print("La calidad del aire es sana")
  elif ICA <= 100 and ICA >=51:
    print("La calidad del aire es moderada")
  elif ICA <= 150 and ICA >= 101:
    print("La calidad del aire es dañina a la salud de los grupos sensibles")
  elif ICA >= 151 and ICA <= 200:
     print("La calidad del aire es dañina a la salud")
  elif ICA <= 300 and ICA >= 201:
     print("La calidad del aire es muy dañina a la salud")
  if PH >= 6.5 and PH <= 8.5 and ICA <= 50:
    zonasa += 1
    print("La zona es sana")
  if PH >= 6.5 and PH <= 8.5 and ICA >= 100 and ICA <= 51:
    zonams += 1
    print("La zona es moderadamente sana")
  if PH >= 6.0 and PH <= 6.5 or PH >= 8.5 and PH >= 9 and ICA >= 100 and ICA <= 51:
    zonams += 1
    print("La zona es moderadamente sana")
  if PH >= 6.0 and PH <= 6.5 or PH <= 9 and PH >= 8.5 and ICA >= 101 and ICA <= 150:
    zonacn1 += 1
    print("La zona es zona contaminada tipo 1")
  if ICA >= 201 and ICA <= 300:
    zonacn2 += 1
    print("La zona es zona contamindad tipo 2")
  if PH <= 6 or PH >= 9:
    zonacn2 += 1
    print("La zona es zona contamindad tipo 2")

  zonas += 1

porcentajeca2 = zonacn2*100/zonasrev
porcentajeca1 = zonacn1*100/zonasrev
if porcentajeca2 >= 50:
    print("Hay contigencia ambiental nivel 2")
elif porcentajeca2 <50:
  pass
if porcentajeca1 > 50:
  print("Hay contingencia ambiental nivel 1")
elif porcentajeca1 <= 50:
  pass 
else:
  print("No hay contingencia ambiental")
promedio = phpromedio/zonasrev
promedioICA = icapromedio/zonasrev
print("El número de zonas sanas es:", zonasa)
print("El número de zonas moderadamente sanas es:", zonasa)
print("El número de zonas contaminadas nivel 1 es:", zonacn1)
print("El número de zonas contaminadas nivel 2 es:", zonacn2)

print(f"promedio de PH de las pruebas del agua {phpromedio}")
print(f"promedio de ICA de las pruebas del aire {promedioICA}")
