import copy


def resolve():

    grille = [[0 for _ in range(8)] for _ in range(8)]  # On créer une grille de 8 par 8

    """
    Choisissons un code :
    0 pour une case libre
    1 pour une case occupée
    2 pour une case contenant une reine
    """

    """
    Considérons qu'il suffit de placer une reine par ligne jusqu'a trouver une 
    configuration respectant les  règles. On a 8^8 possibilités au max, ce qui 
    semble raisonnable
    """

    calcul_ligne(grille, 0)


def calcul_ligne(grille, i):
    reste_grille = copy.deepcopy(grille[i:])
    for xi in indices_des_0(grille[i]):
        grille[i:] = copy.deepcopy(reste_grille)
        grille[i][xi] = 2
        elimine_case(grille, xi, i)

        if i < 7:
            calcul_ligne(grille, i + 1)
        elif i == 7:
            nice_print(grille)
            print()


def indices_des_0(ligne):
    pos_of_0s = []
    for i, nb in enumerate(ligne):
        if nb == 0:
            pos_of_0s.append(i)
    return pos_of_0s


def elimine_case(grille, x, y):
    # ligne
    for i in range(8):
        if grille[y][i] == 0:
            grille[y][i] = 1

    # colonne
    for i in range(8):
        if grille[i][x] == 0:
            grille[i][x] = 1

    # diagnonale haut gauche - bas droit
    for i in range(8):
        pos_x = i + x - y
        pos_y = i
        if 0 <= pos_y <= 7 and 0 <= pos_x <= 7:
            if grille[pos_y][pos_x] == 0:
                grille[pos_y][pos_x] = 1

    # diagonale haut droit - bas gauche
    for i in range(8):
        pos_x = x + y - i
        pos_y = i
        if 0 <= pos_y <= 7 and 0 <= pos_x <= 7:
            if grille[pos_y][pos_x] == 0:
                grille[pos_y][pos_x] = 1


def nice_print(list_to_print):
    for i in list_to_print:
        print(i)


resolve()
