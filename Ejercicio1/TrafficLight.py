Probabilily = [5, 2, 4, 9, 7]


def Trafficlight(probability):
    for probably in probability:
        if probably < 4:
            print("\t\tVerde * Probability = " + str(probably))
        elif 5 > probably >= 4:
            print("\t\tAmarillo * Probability = " + str(probably))
        else:
            print("\t\tRojo * Probability = " + str(probably))


Trafficlight(Probabilily)