# MCOC2020-P0
# Mi computador
* Marca/modelo: iMac13,1 (21.5-inch, Late 2012)
* Sistema operativo: macOS Catalina v10.15.6
* Tipo: escritorio
* Año adquisicion: 2012
* Procesador:
	* Marca/modelo: Quad-Core Intel Core i5
	* Velocidad: 2,7 GHz
	* Numero de nucleos: 4
	* Numero de hilos: 2
	* Arquitectura: 
	* Set de instrucciones: 
* Tamaño de las caches del procesador:
	* Caché de nivel 2 (por nucleo): 256 KB
	* Caché de nivel 3: 6 MB
* Memoria: 
	* Total: 8GB
	* Tipo de memoria: DDR3
	* Velocidad: 1600 MHz
	* Numero de (SO)DIMM: 2
* Tarjeta grafica:
	* Marca/modelo: NVIDIA GeForce GT 640M
	* Memoria dedicada: 512 MB
	* Resolucion: 1920 x 1080
* Disco SATA:
	* Marca: Apple (Macintosh HD)
	* Tamaño: 1 TB
	* Sistema de archivos: APFS
* Direccion MAC: 8c:2d:aa:30:a9:9d
* Direccion IP (ROUTER): 192.168.0.10
* Direccion IP (ISP): 190.160.0.11
* Proveedor: VTR Banda Ancha S.A.

# Desempeño MATMUL:
![grafico](https://user-images.githubusercontent.com/69252038/89684852-39532d80-d8c9-11ea-844e-fc06c412a231.png)
* ¿Como difiere del gráfico del profesor?:
	* Nuestros gráficos difieren en el tiempo transcurrido para las matrices mas pequeñas. En el gráfico del profesor se ve que los realiza en menor cantidad de tiempo y sin tanta diferencia entre las corridas, en cambio, en mi gráfico se aprecia que hay corridas que lo hicieron rapidamente, mientras otras que estuvieron cerca del 0.1 s. 
	* También vemos que en la zona media (matrices de N igual 60 hasta 1000 aproximadamente) del gráfico del profesor, existe mayor diferencia entre las corridas, mientras que en mi gráfico se ve que los resultados no varían significativamente. 
	* Por ultimo para la zona final (matrices de N igual 2000 hasta 10000) tienen un comportamiento parecido ambos gráficos, a excepción de la ultima matriz, ya que mi pc lo realiza en mayor cantidad de tiempo (cercano a 30 segundos). 
* ¿A que se pueden deber estas diferencias?:
	* Puede deberse a que mientras se corría el codigo, se estaban realizando otras actividades al mismo tiempo, lo cual afecta al rendimiento del computador. Esto habla sobre el procesador que contiene cada pc. 
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurido no lo es ¿por qué puede ser?:
	* Los gráficos de uso de memoria son lineales e iguales porque esto no depende del rendimiento de las computadoras, si no de la magnitud de las matrices con las que se van a operar. 
* ¿Que versión de Python está usando?:
	* Python 3.8.1
* ¿Que versión de Numpy esta usando?:
	* Numpy 1.18.5
* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar:
	* 
## Función mimatmul:
![grafico](https://user-images.githubusercontent.com/69252038/89841383-c18f3800-db40-11ea-9a10-a1a907141162.png)
* ¿Como difiere del gráfico del ayudante?:
	* Al igual que en la entrega anterior, nuestros graficos varian principalmente en el tiempo transcurrido de las iteraciones realizadas. Se observa que mi gráfico demora mas tiempo en cada iteracion de cada N implementado en el codigo (queda clarisimo con el tiempo transcurrido con N = 500)
* ¿A que se pueden deber estas diferencias?:
	* Puede deberse a que mientras se corría el codigo, se estaban realizando otras actividades al mismo tiempo, lo cual afecta al rendimiento del computador. Esto habla sobre el procesador que contiene cada pc. Pero en particular para esta entrega, afecta directamente el codigo creado para realizar las multiplicaciones, ya que al hacer una ruta mas larga o un calculo mas tedioso, realiza las operaciones en mayor tiempo.
* Se hizo hasta el N = 500 ya que para mayores numeros, mi pc no lograba realizarlo en menos de 5 min. Esto quiere decir que hacer el grafico para 10 iteraciones con altos valores de N, implicaba estar esperando 1 hora y media o mas para obtener los resultados.

# Desempeño INV:
![grafico](https://user-images.githubusercontent.com/69252038/90091409-49697380-dcf4-11ea-8afc-70aa16d4d611.png)

* Grafico de caso SINGLE 
* Se observan los 3 casos propuestos

![grafico_half](https://user-images.githubusercontent.com/69252038/90091415-50908180-dcf4-11ea-9e98-313f8d1526a6.png)

* Grafico de caso HALF 
* Se observa solo los casos con Scipy, ya que con Numpy tiraba error (se cree que esto ocurre por la capacidad que tiene la libreria)

![grafico_double](https://user-images.githubusercontent.com/69252038/90091425-54bc9f00-dcf4-11ea-92b3-cb506f800ccc.png)

* Grafico de caso DOUBLE 
* Se observan los 3 casos propuestos

![grafico_longdouble](https://user-images.githubusercontent.com/69252038/90091428-571ef900-dcf4-11ea-9b08-af893add5322.png)

* Grafico de caso LONGDOUBLE 
* Se observa solo los casos con Scipy, ya que con Numpy tiraba error (se cree que esto ocurre por la capacidad que tiene la libreria)

* Numpy (color rojo), ScipyTrue (color azul) y ScipyFalse (color verde).
* Se puede observar que hay diferencias en los tiempos transcurridos entre graficos. Esto de puede deber a que los tipo de dato utilizado, afecta directamente a la memoria ocupada para realizar las operaciones, por lo tanto, a menor memoria utilizada, menor tiempo transcurrido en los procesos.  Con "np.half" y "np.longdouble" la libreria Numpy no los aceptaba y tiraba error. A pesar de eso, se entregó los resultados de la libreria Scipy.
* Es dificil ver en que momento hay cambios en caché del procesador, excepto en el gráfico del tipo DOUBLE en el que ocurrió un fenomeno en que variaba de manera extraña el tiempo transcurrido en las distintos N de matrices. Esto ocurrio en la linea de ScipyTrue (color azul). 
