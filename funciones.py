import random

CANTIDAD_CDA = 10
CANTIDAD_DIRECCIONES = 2000
LADOS = ['I', 'D']

def obtener_lista_cda():
  lista_cda = []
  cont=0
  while cont<CANTIDAD_CDA:
    ncda=(random.randint(0,CANTIDAD_DIRECCIONES))
    if ncda not in lista_cda:
     lista_cda.append( ncda )
     cont+=1 
   
  lista_cda.sort()

  return lista_cda

def obtener_lista_direcciones( lista_cdas ):
  lista_direcciones = []

  cont=0
  while cont<=CANTIDAD_DIRECCIONES:
   if cont not in lista_cdas:
      lado = random.choice(LADOS)
      lista_direcciones.append( str(cont) + '-' + str(lado) )
   cont=cont+1

  return lista_direcciones

def asignar_empleos(direcciones, cdas):
  
  asignaciones = obtener_listado_por_cda( len(cdas) )

  for direccion in direcciones:

    cont = 0
    numero_direccion = obtener_numero_direccion(direccion)
    menor = CANTIDAD_DIRECCIONES + 1
    indice_menor = 0
    
    while cont < len(cdas):
      distancia = abs(numero_direccion - cdas[cont])
      
      if distancia < menor:
        menor = distancia
        indice_menor = cont

      cont += 1
    
    asignaciones[indice_menor].append(direccion)

  return asignaciones


def obtener_listado_por_cda(tamano):
  return [[] for i in range( tamano )]

def obtener_numero_direccion(direccion_completa):
  numero_direccion = int(direccion_completa.split('-')[0])
  return numero_direccion

def asignacion_citas(direcciones_cda):
  citas = []

  dia = 1 #1
  hora = 0 #5
  minutos = 0 #0
 
  count = 0

  while count < len(direcciones_cda):
    citas.append(str(dia) + '-' + str(hora) + ':' + str(minutos))

    if hora >= 5 and minutos >= 40:
      dia += 1
      hora = 0
      minutos = 0

    else:

      if minutos >= 40: 
        hora += 1
        minutos = 0
      else:
        minutos += 20

    count += 1

  return citas