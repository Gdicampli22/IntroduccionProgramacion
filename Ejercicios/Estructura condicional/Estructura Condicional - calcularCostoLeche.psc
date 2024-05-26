Algoritmo calcularCostoLeche
		Definir cantidad Como Entero
		Definir es_jubilado Como Logico
		Definir costo_unitario, costo_total, descuento Como Real
		
		costo_unitario = 1000
		
		Escribir "Ingrese la cantidad de unidades compradas:"
		Leer cantidad
		Escribir "¿Es jubilado? (1 para Sí, 0 para No):"
		Leer es_jubilado
		
		costo_total = cantidad * costo_unitario
		
		Si cantidad > 24 Entonces
			descuento = 0.15
		Sino
			Si cantidad > 12 Entonces
				descuento = 0.10
			Finsi
		Finsi
		
		Si es_jubilado Entonces
			descuento = descuento + 0.10
		FinSi
		
		costo_final = costo_total * (1 - descuento)
		Escribir "El costo final es:", costo_final
		


FinAlgoritmo
