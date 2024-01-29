"""
* Título: modelo de simulación de cola de supermercado
* Objetivo: calcular, simuladamente, la cantidad de cajeros para no perder más de 3 clientes por jornada
* Enviar solución por email a alexsandra.cassiano@uap.edu.ar y nicolas.giqueaux@uap.edu.ar
* Grupos de no más de 3 miembros
*
* Consideraciones:
*   -> Una cola por caja
*   -> Cantidad de cajas variables. Usar listas de cajas. Comenzar con una sola caja, luego ir aumentando.
*   -> Cada ejecución del algoritmo representa una jornada de trabajo en donde la cantidad de cajas no varía.
*   -> Para cambiar la cantidad de cajas se deberá detener el programa y parametrizar la cantidad de cajas que se desea.
*   -> Jornada dura 8 horas.
*   -> La frecuencia promedio de ingreso de una persona a la caja durante la jornada es una cada 10 minutos.
*   -> El tiempo que tarda cada caja en atender está entre 3 a 10 minutos. Determinar al azar.
*   -> Las personas tiene distintos grados de paciencia de espera en la cola, 
       si se agota abandona la compra: esperan entren 5 a 15 minutos. 
       Determinar al azar cuando entra a la cola.
*   -> Si un cliente ya está en la caja siendo atendido espera a terminar y no abandona.
*   -> Política de cajas "Primero en entrar, primero en salir"
*   -> Cuando una pesona sale de la caja se saca de la lista y se desplazan todos los elementos restantes. 
       Osea, en el índice 0 del array de la cola de la caja representa a la persona que se está atendiendo,
       cuando esta sale, se saca del array y la persona que estaba en el índice 1 para al 0, la que estaba 
       en el indice 2 pasa al 1 y así sucesivamente
*   -> Iterar cada segundo de las 8 horas de la jornada, es decir que se deberá hacer un bucle que tenga 8(horas) * 60(minutos/h) ciclos.

*   Reporte al final del día:    
*   -> Cantidad de cajas
*   -> Cantidad de personas que abondonan la compra
*   -> Cantidad de personas atendidas
*   -> Promedio de tiempo en caja
*
* https://es.wikipedia.org/wiki/Teor%C3%ADa_de_colas
"""
import math
import random

minuto = 0 #variable contador para llevar la cuenta de los minutos transcurridos del día laboral
fin_de_la_jornada = 8 * 60 #variable que marca el fin de las 8 horas de trabajo
cantidad_personas_abandonaron = 0
cantidad_personas_atendidas = 0
promedio_tiempo_cajas = 0
cantidad_de_cajas = 3  # Cantidad de cajas agregadas

cajas = [[] for i in range(cantidad_de_cajas)]



def generador_persona():
    """
    Usar esta función por minuto para crear la persona que se suman a la cola de una caja
    Uso: p = generador_persona()
    Retorna: una persona o None si no hay nadie para entrar a la cola en ese minuto
    """
    p = None
    probabilidad_de_entrada = random.randint(1, 10)#probabilidad 1 en 10 de entrar a una sola cola
    if(probabilidad_de_entrada == 1):
        p = {
            "grado_de_paciencia" : random.randint(5, 15),#cantidad de minutos que tolera en la cola
            "tiempo_esperando_en_cola" : 0,#contador de iteraciones, si llega a grado_de_paciencia se va.
            "tiempo_esperando_en_caja" : 0,#contador de iteraciones cuando ya está en caja, cuando llegue a tiempo_que_tarda_la_caja, se va
            "tiempo_que_tarda_la_caja" : random.randint(3, 10)#tiempo que le va a tardar la caja en antender a este cliente: de 3 a 10 minutos
        }
    return p

#************************************************************************
#MOTOR PRINCIPAL
#Bucle que representa lo que sucede en cada minuto de la jornada laboral
#Cada iteración representa lo que sucede en un minuto de la jornada
while(minuto <= fin_de_la_jornada): 
    minuto = minuto + 1
    
    #LOGICA DE LA ENTRADA A COLA
    #¿en este minuto ingresa un persona a la caja?:
    
        
    
    # Encontrar la caja con la menor cantidad de personas
    p = generador_persona()
    if(p):
        print("Entra una persona a la cola: " + str(p))    
        caja_menor_cantidad = 0
        for i in range(cantidad_de_cajas):
            if len(cajas[i]) < len(cajas[caja_menor_cantidad]):
                caja_menor_cantidad = i
        # Agregar la nueva persona a la caja con la menor cantidad de personas
        cajas[caja_menor_cantidad].append(p)

    #LOGICA DE LA PACIENCIA
    #incrementar a todos los contadores de la personas en cola 1 minuto, evaluar si supera el límite de paciencia, sacar de la cola de ser necesario
    if len(cajas[0]) > 1:
        i = 1
        while(i < len(cajas[0])):
            cajas[0][i]["tiempo_esperando_en_cola"] += 1
            if cajas[0][i]["tiempo_esperando_en_cola"] > cajas[0][i]["grado_de_paciencia"]:
                del cajas[0][i]
                cantidad_personas_abandonaron += 1
            else:
                i = i + 1
            
    #LOGICA DE LA SALIDA DE CAJA
    #incrementar el contador de la persona que está en caja en 1 minuto. evaluar si ya llega al fin de tiempo determinado para atendderlo
    if len(cajas[0]) > 0:
        cajas[0][0]["tiempo_esperando_en_caja"] +=1
        if cajas[0][0]["tiempo_esperando_en_caja"] == cajas [0][0]["tiempo_que_tarda_la_caja"]:
            promedio_tiempo_cajas += cajas [0][0]["tiempo_que_tarda_la_caja"]
            del cajas[0][0]
            cantidad_personas_atendidas += 1



print("Cantidad cajas: " + str(cantidad_de_cajas))
print("Abandonaron: " + str(cantidad_personas_abandonaron))
print("Atendidos: " + str(cantidad_personas_atendidas))
print("Promedio de tiempo de atención: " + str(round(promedio_tiempo_cajas/cantidad_personas_atendidas,2)) + " min")
