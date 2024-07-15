#Librerías
import random

def JuegoCiclo(Monto,ApuestaDada):

    #Variables 
    ciclo=int(0)
    apuestaAcumulada=int()
    apuesta=int()
    Resultado=[]

    #Constantes
    #apuestaMinima=int(5)
    perdidaAcumulada=int(0)
    gananciaAcumulada=int(100)
    Nciclos=int(100)

    #Proceso 

    apuestaAcumulada=int(Monto)
    apuesta=int(ApuestaDada)

    #Algoritmo de Proceso de Apuestas 
    while(ciclo<=Nciclos):
        ndado=random.randint(1,6)
        if(ndado%2==0):
            apuestaAcumulada=apuestaAcumulada+(2*apuesta)
            #print("Usted Gano")
        if(ndado%2==1):
            apuestaAcumulada=apuestaAcumulada-apuesta
            #print("usted perdio")
        if(apuestaAcumulada>gananciaAcumulada):
            #print("Usted alcanzo el limite de Ganancias")
            Resultado.append(int(1))
            break
        if(apuestaAcumulada<perdidaAcumulada):
            #print("Usted alcanzo el limite de Perdida") 
            Resultado.append(int(-1))
            break
        #print(apuestaAcumulada)
        ciclo=ciclo+1

    if(ciclo>=Nciclos):

        if(apuestaAcumulada<=int(Monto)):
            Resultado.append(int(-1))
        else:
            Resultado.append(int(1))

    Resultado.append(int(apuestaAcumulada)) 

    return Resultado

    #print("usted tiene",apuestaAcumulada)