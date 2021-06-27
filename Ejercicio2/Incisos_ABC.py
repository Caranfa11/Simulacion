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



print("\n\nInciso A \n")
print("Numeros PseudoAleatorios Obtenidos " +str(MixtoCongruente(2,1,3,10,10)))
print("\n\nInciso B \n")
print("Numeros PseudoAleatorios Obtenidos " + str(MixtoCongruente(1,5,1,8,8)))
print("\n\nInciso C \n")
print("Numeros PseudoAleatorios Obtenidos " + str(MixtoCongruente(100,61,27,100,5)))