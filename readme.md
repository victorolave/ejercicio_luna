# Reto semana 04
En vista de que la asignación de las etapas de evacuación fue todo un éxito gracias a la aplicación que implementamos, nos han contratado nuevamente para ayudar en la organización de la primera ciudad en el planeta Ragnar.

En la primera ciudad del planeta Ragnar solamente existe una calle, en la cual, las casas están marcadas con direcciones que van desde el 0 hasta el 2000. Los nuevos habitantes solo se pueden transportar por esa calle que va en ambas direcciones.

Se debe implementar un programa que asigne un empleo a cada nuevo habitante de la nueva ciudad en el nuevo planeta, teniendo en cuenta su distancia y el día y hora de la cita.

## Asignación del empleo

Esta función tiene como objetivo asignar un empleo a los habitantes, para lo cual, se ingresa una lista con la dirección de cada habitante en cada posición. Las direcciones son los números entre 0 y 2000 con la letra I si es a la izquieda de la la calle y D en caso de que 
sea en el lado derecho de la calle.

### Ejemplo:
Lista_direcciones = [“10-D”, “65-I”, “30-I”, “900-D”]

El gobierno del planeta ha construido diez centros de asignación de empleo (CDA) a lo largo de la única calle de la ciudad, las direcciones de cada CDA son un número entre 0 y 2000 ya que cada CDA ocupa ambos lados de la calle.

Se debe implementar una función que permita:

- Recibir como parámetros de entrada la lista de direcciones de los habitantes y la 
lista de los 10 CDA
- Retornar una lista para cada CDA con todas las direcciones de las personas que 
debe atender. El criterio de asignación es asignar un habitante al CDA más cercano 
a su residencia

## Citas para asignación

En cada CDA se demoran 10 minutos en el proceso de asignación por cada habitante, y necesitan una aplicación que asigne el empleo a cada habitante asignado al CDA teniendo en cuenta las siguientes restricciones:

- Los días del planeta Ragnar solo duran 5 horas, es decir, 300 minutos
- La asignación inicia el día 1 a las 0:00 y se realiza cada 20 minutos
- Cuando se llega a la cita número 15 del día se pasa al día siguiente

Se debe implementar una función que permita:

- Recibir como parámetro la lista de direcciones de los habitantes asignados al CDA
- Retornar una lista con el día y hora de la cita correspondiente a cada dirección de la 
lista ingresada

### Ejemplo:

Si recibe:

Lista_direcciones=["10-D","65-I","30-I","900-D","65-I","15-D","89-I","35-I","9-D","650-I","905-D","5-I","10-D","655-I","300-I","900-D","605-I"]

Debe retornar

Lista_citas=["1-0:0","1-0:20","1-0:40","1-1:0","1-1:20","1-1:40","1-2:0","1-2:20","1-2:40","1-3:0","1-3:20","1-3:40","1-4:0","1-4:20","1-4:40","2-0:00”, “2-0:20”]

Y funciona de la siguiente manera

Lista_citas = [“1-0:00”, “1-0:20”, “1-0:40”, “1-1:00”…]

Donde el 1 representa el día y el 0:00 representa la hora
