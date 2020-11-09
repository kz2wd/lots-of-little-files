def calculer_suite(p):
    u = 1
    for i in range(p):
        somme = calculer_suite(i)
        for j in range(i):
            somme += calculer_suite(j) * calculer_suite(i - j)
        u = somme
    return u


def afficher_suite(p):
    for i in range(p):
        print("n :", i, " u =", calculer_suite(i))


afficher_suite(5)
