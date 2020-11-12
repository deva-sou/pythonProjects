import sys

def menu():
    print("\n---- Bienvenue dans le jeu MORIARTY ----")
    print("\n[1] - Afficher les règles")
    print("[2] - Commencer une partie")
    print("[3] - Quitter le programme")
    rep = 1
    while rep != 0:
        rep = int(input("\nQuel est votre choix ? : "))
        if rep == 1:
            listedesregles()
        elif rep == 2:
            return
        elif rep == 3:
            sys.exit()

def listedesregles():
    print("\n---- Voici les règles du jeu ----")

def initialisation (totalListe):
    for i in range (10):
        liste = ["0",".",".",".",".",".",".",".",".","0"]
        if i == 0 or i == 9:
            liste = ["0","0","0","0","0","0","0","0","0","0"]
            totalListe.append(liste)
        else:
            totalListe.append(liste)
    totalListe[4][4] = 'R'
    totalListe[4][5] = 'V'
    totalListe[5][4] = 'V'
    totalListe[5][5] = 'R'
    print("\n---- C'est parti ! ----")

def affichage (totalListe):
    i = 1
    print("\n")
    print ("  1 2 3 4 5 6 7 8")
    for element in totalListe[1:9]:
        print (i,'|'.join(element[1:9]))
        i = i+1

def choosePlayer():
    print("\n---- Début de la partie ----")
    print("\nQuel joueur etes-vous ? [R]: activateur de proteine, [V]: inhibiteur de proteine")
    color = input("\n>> ")
    if color == "V":
        color2 = "R"
    elif color == "R":
        color2 = "V"
    else:
        print("Erreur de choix")
    return color,color2

def depotPion (totalListe,playercolor):
    print("\nJoueur",playercolor,"deposez votre pion: ([0] en ligne et en colonne pour abandonner)")
    print('\nQuelle ligne ? : ')
    ligne1 = int(input())
    print('\nQuelle colonne ? : ')
    colonne1 = int(input())
    position1 = [ligne1,colonne1]
    if ligne1 == 0 and colonne1 == 0:
        abandon = 1
        winCondition(totalListe,abandon)
    verif=regles(position1,totalListe,listeChangement,advcolor)
    if verif == True:
        totalListe[ligne1][colonne1] = playercolor
        return verif
    else:
        print("\nPosition non-valide\n")
        return

def changeState(listeChangement,playercolor,totalListe):
    for k in listeChangement:
        totalListe[k[0]][k[1]] = playercolor
    del listeChangement[:]

def regles(position1,totalListe,listeChangement,advcolor):
    listePos = []
    for i in range(position1[0]-1,position1[0]+2,1):
        for j in range(position1[1]-1,position1[1]+2,1):
            if totalListe[i][j] == advcolor:
                a = i
                b = j
                if a == position1[0]-1 and b == position1[1]-1:
                    while totalListe[a][b] == advcolor:
                        listePos.append([a,b])
                        a = a-1
                        b = b-1
                    if totalListe[a][b] == "0" or totalListe[a][b] == ".":
                        del listePos[:]
                        a = i
                        b = j
                    else:
                        listeChangement.extend(listePos)
                        del listePos[:]
                        a = i
                        b = j
                if a == position1[0]-1 and b == position1[1]:
                    while totalListe[a][b] == advcolor:
                        listePos.append([a,b])
                        a = a-1
                    if totalListe[a][b] == "0" or totalListe[a][b] == ".":
                        del listePos[:]
                        a = i
                        b = j
                    else:
                        listeChangement.extend(listePos)
                        del listePos[:]
                        a = i
                        b = j
                if a == position1[0]-1 and b == position1[1]+1:
                    while totalListe[a][b] == advcolor:
                        listePos.append([a,b])
                        a = a-1
                        b = b+1
                    if totalListe[a][b] == "0" or totalListe[a][b] == ".":
                        del listePos[:]
                        a = i
                        b = j
                    else:
                        listeChangement.extend(listePos)
                        del listePos[:]
                        a = i
                        b = j
                if a == position1[0] and b == position1[1]-1:
                    while totalListe[a][b] == advcolor:
                        listePos.append([a,b])
                        b = b-1
                    if totalListe[a][b] == "0" or totalListe[a][b] == ".":
                        del listePos[:]
                        a = i
                        b = j
                    else:
                        listeChangement.extend(listePos)
                        del listePos[:]
                        a = i
                        b = j
                if a == position1[0] and b == position1[1]+1:
                    while totalListe[a][b] == advcolor:
                        listePos.append([a,b])
                        b = b+1
                    if totalListe[a][b] == "0" or totalListe[a][b] == ".":
                        del listePos[:]
                        a = i
                        b = j
                    else:
                        listeChangement.extend(listePos)
                        del listePos[:]
                        a = i
                        b = j
                if a == position1[0]+1 and b == position1[1]-1:
                    while totalListe[a][b] == advcolor:
                        listePos.append([a,b])
                        a = a+1
                        b = b-1
                    if totalListe[a][b] == "0" or totalListe[a][b] == ".":
                        del listePos[:]
                        a = i
                        b = j
                    else:
                        listeChangement.extend(listePos)
                        del listePos[:]
                        a = i
                        b = j
                if a == position1[0]+1 and b == position1[1]:
                    while totalListe[a][b] == advcolor:
                        listePos.append([a,b])
                        a = a+1
                    if totalListe[a][b] == "0" or totalListe[a][b] == ".":
                        del listePos[:]
                        a = i
                        b = j
                    else:
                        listeChangement.extend(listePos)
                        del listePos[:]
                        a = i
                        b = j
                if a == position1[0]+1 and b == position1[1]+1:
                    while totalListe[a][b] == advcolor:
                        listePos.append([a,b])
                        a = a+1
                        b = b+1
                    if totalListe[a][b] == "0" or totalListe[a][b] == ".":
                        del listePos[:]
                        a = i
                        b = j
                    else:
                        listeChangement.extend(listePos)
                        del listePos[:]
                        a = i
                        b = j

    if ((len(listeChangement) != 0) and (totalListe[position1[0]][position1[1]] == ".")):
        return True
    else:
        return False

def winCondition(totalListe,abandon):
    countRed = 0
    countGreen = 0
    compteur = 0
    for i in range(1,9):
        for j in range(1,9):
            if totalListe[i][j] == "V":
                countGreen += 1
            if totalListe[i][j] == "R":
                countRed += 1
            position2 = [i,j]
            countPos = regles(position2, totalListe, listeChangement, advcolor)
            if countPos == True:
                compteur += 1
            del listeChangement[:]
    if compteur == 0 or countRed == 0 or countGreen == 0 or (countRed+countGreen) == 64 or abandon == 1:
        score(totalListe, countRed, countGreen,abandon)
    else:
        return

def score(totalListe,countRed,countGreen,abandon):
    print("\n---- Résultats de la partie ----")
    print(f"\nCompteur de vert : {countGreen}, compteur de rouges : {countRed}")
    if abandon == 1:
      print("Abandon : le joueur ", advcolor, " remporte la partie")
      sys.exit()
    elif int(countRed) > int(countGreen):
        print("\nLe joueur R a gagné")
        sys.exit()
    elif int(countRed) < int(countGreen):
        print("\nLe joueur V a gagné")
        sys.exit()
    else:
        print("\nEgalité entre le joueur V et R !")
        sys.exit()

### MAIN CODE:

menu()
playercolor,advcolor = choosePlayer()
state = 1
abandon = 0
totalListe = []
listeChangement = []
initialisation(totalListe)

while state == 1:
        affichage(totalListe)
        val = depotPion(totalListe,playercolor)
        if val == True:
            changeState(listeChangement,playercolor,totalListe)
            playercolor,advcolor = advcolor,playercolor
            winCondition(totalListe,abandon)
