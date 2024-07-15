import juegodeprobabilidad 

VecesJugado=int(0)
VecesGanado=int(0)
VecesPerdido=int(0)
GananciaTotal=int(0)

apuestaMinima=int(5)
perdidaAcumulada=int(0)
gananciaAcumulada=int(100)

print("Ingrese La Cantidad de veces que quiere jugar")
NumeroDeJuegos=int(input())

#Algoritmo de Detección de apuesta del monto inicial que este dentro de los parametros

while(True):
    print("ingrese el monto inicial de cada juego, debe ser mayor o igual a 5 y menor a 100")
    MontoTotal=int(input())
    if(MontoTotal<apuestaMinima):
        print("Ingrese un monto permitido")
    if(MontoTotal>=apuestaMinima):
        if(MontoTotal>gananciaAcumulada):
            print("Ingrese un monto permitido")
        else:
            break

#Algoritmo de Detección de Apuesta inicial y que cumpla con las reglas

while(True):
    print("ingrese la cantidad que quiera apostar")
    ApuestaTotal=int(input())
    if(ApuestaTotal>MontoTotal):
        print("usted no puede aportar mas de lo que lleva acumulado")
    else:
        if(ApuestaTotal<apuestaMinima):
            print("ingrese un monto permitido")
        else:
            break

while(VecesJugado<=NumeroDeJuegos):

    ResultadoDelJuego=juegodeprobabilidad.JuegoCiclo(MontoTotal,ApuestaTotal)
    
    if(int(ResultadoDelJuego[0])==1):
        VecesGanado=VecesGanado+1
    if(int(ResultadoDelJuego[0])==-1):
        VecesPerdido=VecesPerdido+1
    
    GananciaTotal=GananciaTotal+ResultadoDelJuego[1]
    VecesJugado=VecesJugado+1

print("Usted Gano")
print(VecesGanado," Partidas")
print("Usted perdio")
print(VecesPerdido," Partidas")
print("Su Ganancia Fue")
print(GananciaTotal," Dolares")

