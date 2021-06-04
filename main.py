""" 
Reto Semana 3 - Guerra digital
Carlos Castañeda
Mayo 26-2021
"""
import funciones as f

lista_cdas = f.obtener_lista_cda()
lista_direcciones = f.obtener_lista_direcciones( lista_cdas )

asignaciones_cda = f.asignar_empleos(lista_direcciones, lista_cdas)

#TODO: Por cada CDA 
for asignacion_cda in asignaciones_cda:
  horarios_cda = f.asignacion_citas(asignacion_cda)
  print(horarios_cda)
  print('-------------------------------------')