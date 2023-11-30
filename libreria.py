"""
renta de plataforma libros infantiles: marzo, abril y julio es GRATIS
renta plataforma novelas: febrero, marzo, abril y mayo es GRATIS
no aplica cupon adicional en: enero, noviembre y diciembre.

- Ciencia ficción: 453. Compra de por vida: 2porciento del precio. Cupón de descuento: no aplica
-infantil: 317. Compra de por vida: 4 porciento. Cupón de descuento: no aplica.
-Novela: 726 8 porciento. cupón de descuento: 150.

1: 80 de mensualidad
2: 50 de mensoalidad
3: 110 de mensualidad



"""
print("1. Ciencia Ficción")
print("2. Infantil")
print("3. Novela")
tipo1 = "ciencia ficcion"
tipo2 = "Infantil"
tipo3 = "Novela"
tipo = int(input("Pon el tipo de libro: 1,2, o 3  "))
vida = str(input("Se desea comprar el libro de por vida? si o no:  ")).lower()
cupon = str(input("Se cuenta con cupón adicional? si o no:  ")).lower()
mes = str(input("¿Qué mes es?  ")).lower()

if tipo == 1 and vida == "si":
  aumento1 = 453*0.02
  precio1 = 453 + aumento1
  print("El libro que escogio fue:", tipo1)
  print("El precio original del libro es: $453")
  print("El costo de por vida es: $453 mas el 2% del precio")
  print("El costo de la mensualidad es: $0")
  print("Los cupones no aplican en esta categoria")
  print(f"Su total a pagar es {precio1}")
elif tipo == 1 and vida == "no":
  precio1 = 80
  print(f"Usted escogió: {tipo1}")
  print("El precio original del libro es: $453")
  print("El costo de por vida es: $0")
  print("El costo de la mensualidad es: $80")
  print("Los cupones no aplican en esta categoria")
  print(f"Su total a pagar es {precio1}")

if tipo == 2 and vida == "si":
  aumento2 = 317*0.04
  precio2 = 317 + aumento2
  print("El libro que escogio fue:", tipo2)
  print("El precio original del libro es: $317 ")
  print("El costo de por vida es: $317 mas el 4% del precio")
  print ("El costo de mensualidad es: $0")
  print("Los cupones no aplican en esta categoria")
  print(f"su total a pagar es {precio2}")
elif tipo == 2 and vida == "no":
  precio2 = 50
  print("El libro que escogio fue:", tipo2)
  print("El precio original del libro es: $317 ")
  print("El costo de por vida es: $0")
  print ("El costo de mensualidad es: $50")
  print("Los cupones no aplican en esta categoria")
  print(f"su total a pagar es {precio2}")
elif tipo == 2 and vida == "no" and mes == "marzo" or mes == "abril" or mes == "julio":
  precio2 = 0
  print("El libro que escogio fue:", tipo2)
  print("El precio original del libro es: $317 ")
  print("El costo de por vida es: 0")
  print ("El costo de mensualidad es: 50")
  print("Los cupones no aplican en esta categoria")
  print(f"su total a pagar es {precio2}")

  
if tipo == 3 and vida == "si" and cupon == "si":
  aumento3 = 726*0.08
  precio3 = 726 + aumento3 - 150
  print("El libro que escogio fue:", tipo3)
  print("El precio original del libro es: $726 ")
  print("El costo de por vida es: 726 + 8%")
  print ("El costo de mensualidad es: 0")
  print("Con un cupon de: 150")
  print(f"su total a pagar es {precio3}")
elif tipo == 3 and vida == "si" and cupon == "no":
  aumento3 = 726*0.08
  precio3 = 726 + aumento3
  print("El libro que escogio fue:", tipo3)
  print("El precio original del libro es: $726 ")
  print("El costo de por vida es: 726 + 8%")
  print ("El costo de mensualidad es: 0")
  print("Los cupones no aplican")
  print(f"su total a pagar es {precio3}")
elif tipo == 3 and vida == "no" and cupon == "no" and mes == "febrero" or mes == "marzo" or mes == "abril" or mes =="mayo":
  precio3 = 0
  print("El libro que escogio fue:", tipo3)
  print("El precio original del libro es: $726 ")
  print("El costo de por vida es: 0")
  print ("El costo de mensualidad es: 110")
  print("Los cupones no aplican en esta categoria")
  print(f"su total a pagar es {precio3}")
elif tipo == 3 and vida == "no" and cupon == "no" and mes == "enero" or "noviembre" or mes == "diciembre": 
  precio3 = 110
  print("El libro que escogio fue:", tipo3)
  print("El precio original del libro es: $726 ")
  print("El costo de por vida es: 0")
  print ("El costo de mensualidad es: 110")
  print("Los cupones no aplican en esta categoria")
  print(f"su total a pagar es {precio3}")
