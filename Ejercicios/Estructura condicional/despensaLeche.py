""" Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad.
 Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un descuento 
 del 10%. Si compra más de 24 unidades, el descuento es del 15%. Además posee la promoción 
 a los jubilados. La promoción de jubilados es sumarle un 10% de descuento
  (si posee otros descuentos, se suma los descuentos).
 Desarrolle una solución algorítmica para saber cuento debe pagar el cliente. """

costo_unitario = 1000

# Entrada de datos
cantidad = int(input("Ingrese la cantidad de unidades compradas: "))
es_jubilado = bool(int(input("¿Es jubilado? (1 para Sí, 0 para No): ")))

# Calcular costo total sin descuentos
costo_total = cantidad * costo_unitario

# Calcular descuentos
if cantidad > 24:
    descuento = 0.15
elif cantidad > 12:
    descuento = 0.10
else:
    descuento = 0

if es_jubilado:
    descuento += 0.10

# Calcular el costo final
costo_final = costo_total * (1 - descuento)
print(f"El costo final es: {costo_final}")