from math import e, factorial


# Codigo Formulas y Funciones a Usar

# P
def TraficoDelSistema(Lambda, U):
    return Lambda / U


# Pn
def ProbabilidadDeNPaquetesEnSistema(P, n):
    return (P ** n) * (1 - P)


# Wq
def TiempoDeEsperaEnColaCliente(P, U, Lambda):
    return P / (U - Lambda)


# Ws
def TiempoPromedioEnSistemaCliente(Wq, U):
    return Wq + (1 / U)


# Lq
def TiempoDeEsperaEnColaPaquete(Lambda, Wq):
    return Lambda * Wq


# Ls
def TiempoPromedioEnSistemaPaquete(Lambda, Ws):
    return Lambda * Ws


# Tiempo
def ProbabilidadDeTiempoDeEspera(P, t, U):
    return e ** (-U * (1 - P) * t)


def MixtoCongruente(XInicial, a, c, m, size):
    numeros = []
    print("Valores Inciales del Metodo:\ta = {0:.2f} ; c = {1:.2f} ; m = {2:.2f} ; X0 = {3:.2f}".format(a, c, XInicial, m))
    for i in range(size):
        #print("\t\tIteracion # {0:.0f}\n\tValor de X0 = {1:.2f}".format(i, XInicial))
        modulo = a * XInicial + c
        #print("{0:.2f}(a) * {1:.2f}(Xn) + {2:.2f}(c) = {3:.2f}".format(a, XInicial, c, modulo))
        xn = modulo % m
        #print("{0:.2f}(Ans) modulo de {1:.2f}(m) = {2:.2f}".format(modulo, m, xn))
        XInicial = xn
        numeros.append(xn)
    return numeros


# TiempoEntrada
def ProbabilidadDeEntradasPorTiempo(Tiempo, Lambda, n):
    return e ** (-Lambda * Tiempo) * ((Lambda * Tiempo) ** n) / factorial(n)


def ProbabilidadDeEntrada(n, Lambda, Entrada):
    Clientes = 0
    ClientesAtendidos = 0
    Vieja = 0
    Probabilidades = []
    #Calculo Probabilidad de Ingreso de Clientes
    for i in range(n):
        Nueva = ProbabilidadDeEntradasPorTiempo(1, Lambda, i) + Vieja
        Vieja = Nueva
        Probabilidades.append(Nueva)


    print("\n")
    for Pseudoaleatorio in Entrada:
        if Pseudoaleatorio <= (Probabilidades[0]*100):
            print("\nNo Han Ingresado Nuevos Clientes       - Numero PseudoAleatorio Obtenido = ", Pseudoaleatorio, "     * Clientes Actuales: ", Clientes)

        elif Probabilidades[0]*100 < Pseudoaleatorio <= (Probabilidades[1]*100):
            Clientes += 1
            print("\nNuevo Cliente Ingresado     1          - Numero PseudoAleatorio Obtenido = ", Pseudoaleatorio, "     * Clientes Actuales: ", Clientes)

        elif (Probabilidades[1]*100) < Pseudoaleatorio < (Probabilidades[2] * 100):
            Clientes += 2
            print("\nNuevos Clientes Ingresados  2          - Numero PseudoAleatorio Obtenido = ", Pseudoaleatorio, "     * Clientes Actuales: ", Clientes)

        elif 99 <= Pseudoaleatorio <= 100:
            Clientes += 3
            print("\nNuevos Clientes Ingresados  3          - Numero PseudoAleatorio Obtenido = ", Pseudoaleatorio, "     * Clientes Actuales: ", Clientes)


        if Clientes >= 1:
            Clientes -= 1
            print("\nCliente Atendido                                                                     * Clientes Actuales: ", Clientes)
        else:
            print("\n                                                                                     * Clientes Actuales: ", Clientes)
            ClientesAtendidos += 1

    print("Clientes Atendidos en 2 Hora: ", ClientesAtendidos)
# Codigo de Procesos
print("\n\tInicio de La Simulacion\n")
Entrada = MixtoCongruente(100, 61, 27, 100, 120) # Se utilizo para generar numeros aleatorios controlados, tema explicado en las guias de Acropolis
print("\t\t\nNumeros PseudoAleatorios Obtenidos\n", Entrada)

Lambda = 45/60
U = 1
ProbabilidadDeEntrada(4, Lambda, Entrada)

p = TraficoDelSistema(Lambda, U)
pCero = ProbabilidadDeNPaquetesEnSistema(p, 0)
Wq = TiempoDeEsperaEnColaCliente(p, U, Lambda)
Ws = TiempoPromedioEnSistemaCliente(Wq, U)
Lq = TiempoDeEsperaEnColaPaquete(Lambda, Wq)
Ls = TiempoPromedioEnSistemaPaquete(Lambda, Ws)

print("\t\t\t\n\n++  Resultados Obtenidos de la Simulación  ++")
print("\nUnidad de Tiempo Utilizada: \n\t\tMinutos (60 Minutos)\n\tTiempo De Simulación: 2 Horas\n\n")
print(
    "Clientes que Ingresan por hora: {0:.2f}\nClientes Atendidos por Hora: {1:.2f}\n"
    "\n\t   * Informaación General *\n Intensidad de Trafico: {2:.2f} \nCondicion de no Saturacion: {3:.2f}\n"
    "\n\t* Información de Los Clientes *\nTiempo Promedio de Espera en Cola de los CLientes: {4:.2f}\nTiempo Promedio en Sistema de los CLientes: {5:.2f}\n"
    "\n\t* Información de Los Paquetes *\nTiempo Promedio de Espera en Cola de Paquetes: {6:.2f}\nTiempo Promedio en Sistema de los Paquetes: {7:.2f}\n"
    .format(Lambda, U, p, pCero, Wq, Ws, Lq, Ls)
)
print("\t\t\tLUIS CARANFA ; C.I:29.603.452")