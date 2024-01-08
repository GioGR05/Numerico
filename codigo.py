
import math as m                                # necesitamos tener un factor de descuento "^" y por lo tanto importamos 
					        # una biblioteca llamada math import math mm y esta biblioteca
					        # tendrá el método de la potencia
import matplotlib.pyplot as plt


class Bond:                                     # Definamos una clase en Python llamada Bond y en esta clase podemos 
						# definir un constructor; además de la palabra reservada self,  tomará
 						# dos atributos, primero la madurez y, en segundo lugar el cupón

    def __init__(self,maturity,coupon):
        self.maturity = maturity                # En el constructor asignaremos estas variables a los atributos de clase 
        self.coupon = coupon #anual in%         # Nota: El cupón se pagará anualmente (por simplicidad) y se expresará 
					        # en puntos porcentuales

    def pv(self,r):                             # El primer método que vamos a definir será  el valor presente, 
					        # necesitamos reutilizar la palabra reservada self y para calcular el precio 
                                                # también necesitaremos la tasa de interés a preferencia

        sum = 100*m.pow(1+r, -self.maturity)    # Aquí usaremos la potencia m para la potencia mencionada antes:
					        # la base será 1 más la tasa de interés r y la potencia será la madurez, 
						# y debido a que estamos dividiendo, necesitamos tomar una potencia 
					        # negativa; así que tenemos la suma inicializada

        for i in range(1,self.maturity+1):      # Ahora tenemos que sumar todos los cupones, así que para eso vamos a 	
					        # usar un ciclo for para cada año, por lo que para i dentro del rango, 
						# y como el rango de funciones de Python del año 1 de forma predeterminada
						# comienza desde 0, debemos especificar que desde 1, además el proceso 
						# se repetirá hasta la madurez donde también debemos agregar 1 para que la
						# última iteración sea con i igual a la madurez 

            sum += self.coupon*m.pow(1+r, -i)   # Y para cada una de esas iteraciones aumentaremos la suma incrementando
						# por el cupón

        return round(sum,2)            		# Finalmente vamos a retornar el valor de la suma, además vamos a dejar el
						# redondeo a solo dos decimales


bond = Bond(10,4)                     		# Definimos una instancia para usar esta clase 
				      		# Tomamos 10 años de maduración y un cupón del 4%, 
				      		# Lo que queremos ver es que queremos imprimir cuál sería el valor presente 
						# para este bono

print(bond.pv(0.04))                  		# ¿Por qué es este caso interesante? Porque si la tasa de interés en el mercado 
				      		# es del 4% y la tasa del cupón es del 4%, eso significa que está 
				      		# a la par al valor razonable, digamos que el cupón compensa exactamente la tasa de 
				      		# interés en el mercado y el precio debería ser igual a 100 en este caso


# Verifiquemos si lo hicimos bien, así imprimimos el precio:
>> 100.00








import math as m                                # necesitamos tener un factor de descuento "^" y por lo tanto importamos 
					        # una biblioteca llamada math import math mm y esta biblioteca
					        # tendrá el método de la potencia
import matplotlib.pyplot as plt


class Bond:                                     # Definamos una clase en Python llamada Bond y en esta clase podemos 
						# definir un constructor; además de la palabra reservada self,  tomará
 						# dos atributos, primero la madurez y, en segundo lugar el cupón

    def __init__(self,maturity,coupon):
        self.maturity = maturity                # En el constructor asignaremos estas variables a los atributos de clase 
        self.coupon = coupon #anual in%         # Nota: El cupón se pagará anualmente (por simplicidad) y se expresará 
					        # en puntos porcentuales

    def pv(self,r):                             # El primer método que vamos a definir será  el valor presente, 
					        # necesitamos reutilizar la palabra reservada self y para calcular el precio 
                                                # también necesitaremos la tasa de interés a preferencia

        sum = 100*m.pow(1+r, -self.maturity)    # Aquí usaremos la potencia m para la potencia mencionada antes:
					        # la base será 1 más la tasa de interés r y la potencia será la madurez, 
						# y debido a que estamos dividiendo, necesitamos tomar una potencia 
					        # negativa; así que tenemos la suma inicializada

        for i in range(1,self.maturity+1):      # Ahora tenemos que sumar todos los cupones, así que para eso vamos a 	
					        # usar un ciclo for para cada año, por lo que para i dentro del rango, 
						# y como el rango de funciones de Python del año 1 de forma predeterminada
						# comienza desde 0, debemos especificar que desde 1, además el proceso 
						# se repetirá hasta la madurez donde también debemos agregar 1 para que la
						# última iteración sea con i igual a la madurez 

            sum += self.coupon*m.pow(1+r, -i)   # Y para cada una de esas iteraciones aumentaremos la suma incrementando
						# por el cupón

        return round(sum,2)            		# Finalmente vamos a retornar el valor de la suma, además vamos a dejar el
						# redondeo a solo dos decimales


bond = Bond(10,4)                     		# Definimos una instancia para usar esta clase 
				      		# Tomamos 10 años de maduración y un cupón del 4%, 
				      		# Lo que queremos ver es que queremos imprimir cuál sería el valor presente 
						# para este bono

#print(bond.pv(0.04))                  		# Comentamos esta línea


# Ahora, usando este VP de la función del bono veremos cuál es la relación entre las tasas de interés y el VP del bono, 
# así que primero definamos un arreglo de tasas de interés, llamado 'ir', así que generemos tasas de interés desde 
# cero hasta 10 y vamos a usar el bucle "for", aquí también para i en el rango, además, consideremos que si comenzamos 
# desde cero, el argumento irá de cero a nueve, así que en realidad vamos a escribirlo :

# Definiendo el rango y recorriendolo, así generaremos el VP   
# Esto va a generar números de 0 a 9, por lo que debemos multiplicarlo  por 0.01 para obtener un porcentaje correcto

ir = range(10)
pvs = [bond.pv(i*0.01) for i in ir]



plt.plot(ir, pvs)				# Ahora vamos a graficar y trazaremos la tasa de interés contra los VP 
plt.grid(True)					# Agregamos la cuadrícula
plt.show()


# Grafica las tasas de interés vs los VPs









import math as m                                # necesitamos tener un factor de descuento "^" y por lo tanto importamos 
					        # una biblioteca llamada math import math mm y esta biblioteca
					        # tendrá el método de la potencia
import matplotlib.pyplot as plt


class Bond:                                     # Definamos una clase en Python llamada Bond y en esta clase podemos 
						# definir un constructor; además de la palabra reservada self,  tomará
 						# dos atributos, primero la madurez y, en segundo lugar el cupón

    def __init__(self,maturity,coupon):
        self.maturity = maturity                # En el constructor asignaremos estas variables a los atributos de clase 
        self.coupon = coupon #anual in%         # Nota: El cupón se pagará anualmente (por simplicidad) y se expresará 
					        # en puntos porcentuales



    def pv(self,r):                             # El primer método que vamos a definir será  el valor presente, 
					        # necesitamos reutilizar la palabra reservada self y para calcular el precio 
                                                # también necesitaremos la tasa de interés a preferencia


        sum = 100*m.pow(1+r, -self.maturity)    # Aquí usaremos la potencia m para la potencia mencionada antes:
					        # la base será 1 más la tasa de interés r y la potencia será la madurez, 
						# y debido a que estamos dividiendo, necesitamos tomar una potencia 
					        # negativa; así que tenemos la suma inicializada

        for i in range(1,self.maturity+1):      # Ahora tenemos que sumar todos los cupones, así que para eso vamos a 	
					        # usar un ciclo for para cada año, por lo que para i dentro del rango, 
						# y como el rango de funciones de Python del año 1 de forma predeterminada
						# comienza desde 0, debemos especificar que desde 1, además el proceso 
						# se repetirá hasta la madurez donde también debemos agregar 1 para que la
						# última iteración sea con i igual a la madurez 


            sum += self.coupon*m.pow(1+r, -i)   # Y para cada una de esas iteraciones aumentaremos la suma incrementando
						# por el cupón

        return round(sum,2)            		# Finalmente vamos a retornar el valor de la suma, además vamos a dejar el
						# redondeo a solo dos decimales



    #Copiemos el método PD de la función Pv que tenemos aquí, llamémoslo derivado de PV, así que lo que tenemos que hacer aquí 
#es multiplicar por menos la madurez y aquí también tenemos que disminuir la potencia en uno y lo mismo aquí menos i 
#multiplicado por este término menos está bien, entonces esta es la derivada de nuestra función de valor presente, 
#observe que esta derivada será la misma para la función de valor presente así como para el valor presente - precio
# porque el precio no depende de la tasa de interés, por lo que es un constante, por lo que si tomamos una derivada y
#esta vez desaparecerá

    def pv_derivative(self,r):						# Copiemos el método de VP de la función que ya 
									# teníamos para tener la derivada del VP
        sum = -self.maturity*100*m.pow(1+r, -self.maturity-1)		# Multiplicamos por menos la madurez y disminuimos la
									# potencia en uno
        for i in range(1,self.maturity+1):
            sum += -i*self.coupon*m.pow(1+r, -i-1)			# Aquí igual, menos i y menos uno
        return round(sum,2)


# Notemos que esta derivada será la misma para la función de valor presente así como para el valor presente - precio
# porque el precio no depende de la tasa de interés, por lo que es un constante



bond = Bond(10,4)                     

#print(bond.pv(0.04))                  #Comentamos la línea

# Vamos a escribir una función llamada tangente
# Definamos un precio que se llama que digamos que va a ser 91 y 

price = 91


# Ahora, usando este VP de la función del bono veremos cuál es la relación entre las tasas de interés y el VP del bono, 
# así que primero definamos un arreglo de tasas de interés, llamado 'ir', así que generemos tasas de interés desde 
# cero hasta 10 y vamos a usar el bucle "for", aquí también para i en el rango, además, consideremos que si comenzamos 
# desde cero, el argumento irá de cero a nueve, así que en realidad vamos a escribirlo :

# Definiendo el rango y recorriendolo, así generaremos el VP   
# Esto va a generar números de 0 a 9, por lo que debemos multiplicarlo  por 0.01 para obtener un porcentaje correcto

ir = range(10)

pvs = [bond.pv(i*0.01) -price for i in ir]


tangent = [ bond.pv(0) - price + i*0.01*bond.pv_derivative(0) for i in ir]



plt.plot(ir, pvs)			# Ahora vamos a graficar y trazaremos la tasa de interés contra los VP 
plt.plot(ir, tangent)				 # También trazaremos la tasa de interés contra la tangente
plt.grid(True)					 # Para cuadricular
plt.show()







import math as m                                # necesitamos tener un factor de descuento "^" y por lo tanto importamos 
					        # una biblioteca llamada math import math mm y esta biblioteca
					        # tendrá el método de la potencia
import matplotlib.pyplot as plt


class Bond:                                     # Definamos una clase en Python llamada Bond y en esta clase podemos 
						# definir un constructor; además de la palabra reservada self,  tomará
 						# dos atributos, primero la madurez y, en segundo lugar el cupón

    def __init__(self,maturity,coupon):
        self.maturity = maturity                # En el constructor asignaremos estas variables a los atributos de clase 
        self.coupon = coupon #anual in%         # Nota: El cupón se pagará anualmente (por simplicidad) y se expresará 
					        # en puntos porcentuales

    def pv(self,r):                             # El primer método que vamos a definir será  el valor presente, 
					        # necesitamos reutilizar la palabra reservada self y para calcular el precio 
                                                # también necesitaremos la tasa de interés a preferencia

        sum = 100*m.pow(1+r, -self.maturity)    # Aquí usaremos la potencia m para la potencia mencionada antes:
					        # la base será 1 más la tasa de interés r y la potencia será la madurez, 
						# y debido a que estamos dividiendo, necesitamos tomar una potencia 
					        # negativa; así que tenemos la suma inicializada

        for i in range(1,self.maturity+1):      # Ahora tenemos que sumar todos los cupones, así que para eso vamos a 	
					        # usar un ciclo for para cada año, por lo que para i dentro del rango, 
						# y como el rango de funciones de Python del año 1 de forma predeterminada
						# comienza desde 0, debemos especificar que desde 1, además el proceso 
						# se repetirá hasta la madurez donde también debemos agregar 1 para que la
						# última iteración sea con i igual a la madurez 

            sum += self.coupon*m.pow(1+r, -i)   # Y para cada una de esas iteraciones aumentaremos la suma incrementando
						# por el cupón

        return round(sum,2)            		# Finalmente vamos a retornar el valor de la suma, además vamos a dejar el
						# redondeo a solo dos decimales




    def pv_derivative(self,r):						# Copiemos el método de VP de la función que ya 
									# teníamos para tener la derivada del VP
        sum = -self.maturity*100*m.pow(1+r, -self.maturity-1)		# Multiplicamos por menos la madurez y disminuimos la
									# potencia en uno
        for i in range(1,self.maturity+1):
            sum += -i*self.coupon*m.pow(1+r, -i-1)			# Aquí igual, menos i y menos uno
        return round(sum,2) 
    
    
    
    
    def ytm(self, price):					# Definimos un nuevo método que tomará el argumento 
								# a la palabra self y a los precios porque lo estamos 
								# calculando hasta el vencimiento según el precio de 
								# mercado
        x = 0							# Inicializamos en la suposición 0

        while(abs(round(self.pv(x)-price,2)) > 0):		# Queremos tener varias iteraciones hasta que nos acerquemos
								# lo suficiente al rendimiento real al vencimiento así que
								# podemos usar un ciclo while, mientras que la diferencia 
								# absoluta entre el precio y lo que obtenemos de nuestra próxima
								# suposición sea mayor que 0
								# Vamos a redondear para que tengamos dos decimales
								
            x = x-(self.pv(x)-price)/self.pv_derivative(x)
        return x


bond = Bond(10,4)                     #de acuerdo, así que tenemos este método, probémoslo ahora, así que definamos 
				      #una instancia de este enlace de clase es igual a y elegimos la madurez primero, 
				      #así que vamos a digamos que tenemos 10 años y un cupón, digamos 4%, 
				      #así que en primer lugar y lo que queremos ver es que queremos imprimir cuál 
                                      #sería el PD para este bono, así que llamemos a este método y digamos que para 
				      #una verificación de cordura veamos qué ser el pv de este bono si la tasa de 
				      #interés es exactamente la misma que la del cupón

#print(bond.pv(0.04))                  #¿Por qué es este caso interesante? Porque si la tasa de interés en el mercado 
				      #es del 4% y la página del cupón es del cuatro por ciento, eso significa que está 
				      #a la par al valor razonable, digamos que el cupón compensa exactamente la tasa de 
				      #interés en el mercado y el precio. debería ser igual a 100 en este caso,
				     # verifiquemos si lo hicimos bien, sí, imprimimos el precio


# Vamos a escribir una función llamada tangente
# Definamos un precio que se llama que digamos que va a ser 91 y 

price = 91


# Ahora, usando este VP de la función del bono veremos cuál es la relación entre las tasas de interés y el VP del bono, 
# así que primero definamos un arreglo de tasas de interés, llamado 'ir', así que generemos tasas de interés desde 
# cero hasta 10 y vamos a usar el bucle "for", aquí también para i en el rango, además, consideremos que si comenzamos 
# desde cero, el argumento irá de cero a nueve, así que en realidad vamos a escribirlo :

# Definiendo el rango y recorriendolo, así generaremos el VP   
# Esto va a generar números de 0 a 9, por lo que debemos multiplicarlo  por 0.01 para obtener un porcentaje correcto


ir = range(10)

ytm = bond.ytm(price)     			# Definimos a a la variable YTM 
print(ytm)					# Le aplicamos la funcion ytm al bono con el precio como parámetro
print (bond.pv(ytm))

pvs = [bond.pv(i*0.01) -price for i in ir]
tangent = [ bond.pv(0) - price + i*0.01*bond.pv_derivative(0) for i in ir]


plt.plot(ir, pvs)
plt.plot(ir, tangent)
plt.axvline(x=ytm*100)      			# Graficamos una función que traza una línea de eje vertical que defina
						# x = YTM, multiplicamos por 100 porque el resultado inicial nos da
						# un porcentaje
plt.grid(True)
plt.show()


# Grafica además la linea verical










import math as m                                # necesitamos tener un factor de descuento "^" y por lo tanto importamos 
					        # una biblioteca llamada math import math mm y esta biblioteca
					        # tendrá el método de la potencia
import matplotlib.pyplot as plt


class Bond:                                     # Definamos una clase en Python llamada Bond y en esta clase podemos 
						# definir un constructor; además de la palabra reservada self,  tomará
 						# dos atributos, primero la madurez y, en segundo lugar el cupón

    def __init__(self,maturity,coupon):
        self.maturity = maturity                # En el constructor asignaremos estas variables a los atributos de clase 
        self.coupon = coupon #anual in%         # Nota: El cupón se pagará anualmente (por simplicidad) y se expresará 
					        # en puntos porcentuales

    def pv(self,r):                             # El primer método que vamos a definir será  el valor presente, 
					        # necesitamos reutilizar la palabra reservada self y para calcular el precio 
                                                # también necesitaremos la tasa de interés a preferencia


        sum = 100*m.pow(1+r, -self.maturity)    # Aquí usaremos la potencia m para la potencia mencionada antes:
					        # la base será 1 más la tasa de interés r y la potencia será la madurez, 
						# y debido a que estamos dividiendo, necesitamos tomar una potencia 
					        # negativa; así que tenemos la suma inicializada

        for i in range(1,self.maturity+1):      # Ahora tenemos que sumar todos los cupones, así que para eso vamos a 	
					        # usar un ciclo for para cada año, por lo que para i dentro del rango, 
						# y como el rango de funciones de Python del año 1 de forma predeterminada
						# comienza desde 0, debemos especificar que desde 1, además el proceso 
						# se repetirá hasta la madurez donde también debemos agregar 1 para que la
						# última iteración sea con i igual a la madurez 


            sum += self.coupon*m.pow(1+r, -i)   # Y para cada una de esas iteraciones aumentaremos la suma incrementando
						# por el cupón

        return round(sum,2)            		# Finalmente vamos a retornar el valor de la suma, además vamos a dejar el
						# redondeo a solo dos decimales



    def pv_derivative(self,r):						# Copiemos el método de VP de la función que ya 
									# teníamos para tener la derivada del VP
        sum = -self.maturity*100*m.pow(1+r, -self.maturity-1)		# Multiplicamos por menos la madurez y disminuimos la
									# potencia en uno
        for i in range(1,self.maturity+1):
            sum += -i*self.coupon*m.pow(1+r, -i-1)
        return round(sum,2)
    
    
    
    
    def ytm(self, price):					# Definimos un nuevo método que tomará el argumento 
								# a la palabra self y a los precios porque lo estamos 
								# calculando hasta el vencimiento según el precio de 
								# mercado
        x = 0						        ###### Inicializamos en la suposición 0
        while(abs(round(self.pv(x)-price,2)) > 0):
            x = x-(self.pv(x)-price)/self.pv_derivative(x)
            print(x)
        return x


bond = Bond(10,4)                     #de acuerdo, así que tenemos este método, probémoslo ahora, así que definamos 
				      #una instancia de este enlace de clase es igual a y elegimos la madurez primero, 
				      #así que vamos a digamos que tenemos 10 años y un cupón, digamos 4%, 
				      #así que en primer lugar y lo que queremos ver es que queremos imprimir cuál 
                                      #sería el PD para este bono, así que llamemos a este método y digamos que para 
				      #una verificación de cordura veamos qué ser el pv de este bono si la tasa de 
				      #interés es exactamente la misma que la del cupón

#print(bond.pv(0.04))                  #¿Por qué es este caso interesante? Porque si la tasa de interés en el mercado 
				      #es del 4% y la página del cupón es del cuatro por ciento, eso significa que está 
				      #a la par al valor razonable, digamos que el cupón compensa exactamente la tasa de 
				      #interés en el mercado y el precio. debería ser igual a 100 en este caso,
				     # verifiquemos si lo hicimos bien, sí, imprimimos el precio

# Vamos a escribir una función llamada tangente
# Definamos un precio que se llama que digamos que va a ser 91 y 

price = 91



ir = range(10)

ytm = bond.ytm(price)
print(ytm)
print (bond.pv(ytm))

pvs = [bond.pv(i*0.01) -price for i in ir]
tangent = [ bond.pv(0) - price + i*0.01*bond.pv_derivative(0) for i in ir]
tangent4 = [ bond.pv(0.04) - price + (i-4)*0.01*bond.pv_derivative(0.04) for i in ir]


#plt.plot(ir, pvs)
#plt.plot(ir, tangent)
#plt.plot(ir, tangent4)
#plt.axvline(x=ytm*100)
#plt.grid(True)
#plt.show()
