from math import e,factorial
#Codigo Formulas y Funciones a Usar

#P
def TraficoDelSistema(Lambda,U):
    return Lambda/U
#Pn
def ProbabilidadDeNPaquetesEnSistema(P,n):
    return (P**n)*(1-P)
#Wq
def TiempoDeEsperaEnColaCliente(P,U,Lambda):
    return P / (U - Lambda)
#Ws
def TiempoPromedioEnSistemaCliente(Wq, U):
    return Wq + (1/U)
#Lq
def TiempoDeEsperaEnColaPaquete(Lambda,Wq):
    return Lambda*Wq
#Ls
def TiempoPromedioEnSistemaPaquete(Lambda, Ws):
    return Lambda*Ws
#Tiempo
def ProbabilidadDeTiempoDeEspera(P,t,U):
    return e**(-U*(1-P)*t)
#TiempoEntrada
def ProbabilidadDeEntradasPorTiempo(Tiempo,Lambda,n):
    return e ** ((Lambda * Tiempo) * ((Lambda * Tiempo) ** n)) / factorial(n)

def MixtoCongruente(XInicial,a,c,m,size):
    numeros = []
    print("Valores Inciales del Metodo:\ta = {0:.2f} ; c = {1:.2f} ; m = {2:.2f} ; X0 = {3:.2f}".format(a,c,XInicial,m))
    for i in range(size):
        print("\t\tIteracion # {0:.0f}\n\tValor de X0 = {1:.2f}".format(i,XInicial))
        modulo = a*XInicial + c
        print("{0:.2f}(a) * {1:.2f}(Xn) + {2:.2f}(c) = {3:.2f}".format(a,XInicial,c,modulo))
        xn = modulo % m
        print("{0:.2f}(Ans) modulo de {1:.2f}(m) = {2:.2f}".format(modulo,m,xn))
        XInicial = xn
        numeros.append(xn)
    return numeros

def ProbabilidadDeEntrada(Posibilidades):
    print("Probailidades de LLegada de Clientes:\n10% --> No Hay Cliente Nuevo\n30% --> Hay 1 Cliente Nuevo\n40% --> Hay 2 Clientes Nuevos\n20% --> Hay 3 Clientes Nuevos\n")
    for probabilidad in Posibilidades:
        if probabilidad <= 0:
            print("No Han Ingresado Nuevos Clientes - Numero Aleatorio Obtenido = ",probabilidad)
        elif 1 <= probabilidad <= 3:
            print("Nuevo Cliente Ingresado          - Numero Aleatorio Obtenido = ",probabilidad)
        elif 4 <= probabilidad <= 7:
            print("Nuevos 2 Clientes Ingresados     - Numero Aleatorio Obtenido = ",probabilidad)
        else:
            print("Nuevos 3 Clientes Ingresados     - Numero Aleatorio Obtenido = ",probabilidad)

#Codigo de Procesos
print("\n\n\nInicio de La Simulacion")
Entrada = MixtoCongruente(2,1,3,10,10)
print("Numeros PseudoAleatorios Obtenidos ",Entrada,"\n\n")
ProbabilidadDeEntrada(Entrada)
Lambda = 45/60
U = 1