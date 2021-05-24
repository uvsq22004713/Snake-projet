#################################################
# groupe BI 2
# Olivier COTTIN
# Clément LUKACS
# Lara ESPINASSE   
# Gabriel HAMOUCH
# Hugo NAZAC
# https://github.com/uvsq22004713/Snake-projet.git
##################################################

######################
# Import des librairie

import tkinter as tk
import tkinter.scrolledtext as st
from random import randint
from tkinter.messagebox import *

############
# Variables globales

WIDTH = 500
HEIGHT = 500
CARRE = 11
x, y = WIDTH / CARRE, HEIGHT / CARRE


stock = 0
direct = None
vitesse = 300

carte = []
cpt_pomme =0

head_snake = (0, 0)
serpent = []

objets = []

racine = tk.Tk()
racine.title("project snake")

fenetreon = False

score = 0
pseudo = tk.StringVar()
filename = r"C:Score1.txt" #Variable global accès et nom fichier

########################################
# Fonctions


def quitter(x):
    """permet de quitter la fenêtre actuelle"""
    global fenetreon
    x.destroy()
    if fenetreon == True:
        opt_select_frame.destroy()
        fenetreon = False


def cartes(num):
    """permet de modifier la carte """
    global stock, carte, CARRE, WIDTH, HEIGHT, x,y
    stock = num
    if num == 0 :
        temp = open("niveau 1.txt", "r")
        CARRE = 15
        x, y = WIDTH / CARRE, HEIGHT / CARRE
    elif num == 1 :
        temp = open("niveau 2.txt", "r")
        CARRE = 12
        x, y = WIDTH / CARRE, HEIGHT / CARRE
    elif num == 2 :
        temp = open("niveau 3.txt", "r")
        CARRE = 15
        x, y = WIDTH / CARRE, HEIGHT / CARRE

    liste = []
    data = []
    for lines in temp:
        liste = lines.split()
        liste = list(map(int,liste))
        
        data.append(liste)
    carte = data
    temp.close()



def reset():
    """Recrée tout l'environnement du jeu quand une partie se termine"""
    global score, pseudo, carte, objets, serpent, head_snake, direct, cpt_pomme


    head_snake = (0, 0)
    serpent = []
    objets = []
    direct = None
    cpt_pomme = 0


    score = 0
    pseudo.set('')



def gameover():
    """termine la partie et renvois au menus principal"""
    tk.messagebox.showinfo(title='Game Over',
                            message="Game Over \n vous allez retourner vers l'écran principal"
                            )
    reset()
    canvas.grid_remove()
    pseudoaff.grid_remove()
    scoreaff.grid_remove()

    bvn.grid()
    pseudo_label.grid()
    pseudo_entry.grid()
    btnjouer.grid()
    maps.grid()


def affichage():
    """créer la génération du terrain, du mur, du snake et 
       de la pomme avec des chiffres pour l'utiliser avec une matrice

    chaque element est representé par un chiffre
    pomme = 2
    tete du serpent = 3
    mur = 1
    herbe = 0 """
    
    global objets
    if carte == []:
        cartes(0)
    if len(objets) != 0:
        for elem in objets:
            canvas.delete(elem)
        objets = []

    #affiche les elements sur la carte
    for j in range(len(carte)):
        for i in range(len(carte[0])):
            if carte[j][i] == 1: 
                mur = canvas.create_rectangle((x * i, y * j),
                                              ((x * i) + x, (y * j) + y),
                                              fill="wheat2",
                                              outline="black"
                                              )
                objets.append(mur)
            elif carte[j][i] == 0: #affichage herbe
                herbe = canvas.create_rectangle((x * i, y * j), 
                                                ((x * i) + x, (y * j) + y), 
                                                fill="pale green",
                                                outline="pale green"
                                                )
                objets.append(herbe)
            elif carte[j][i] == 2: #affichage des pommes
                #Efface l'ancienne pomme en recouvrant de vert la dernière position
                pomme1 = canvas.create_rectangle((x * i, y * j),
                                                ((x * i) + x, (y * j) + y),
                                                fill="pale green",
                                                outline="pale green"
                                                )
                #affiche la nouvelle pomme
                pomme2 = canvas.create_oval(((x * i) + 10, (y * j) + 10),
                                            (((x * i) + x) - 10, ((y * j) + y) - 10),
                                            fill="firebrick2"
                                            )
                objets.append(pomme1)
                objets.append(pomme2)
            elif carte[j][i] == 3: #affichage de la tete du serpent
                tete = canvas.create_rectangle((x * i, y * j),
                                                ((x * i) + x, (y * j) + y),
                                                fill="springgreen4",
                                                outline="springgreen4"
                                                )
                objets.append(tete)


def pomme_detector(pos_x, pos_y):
    """détecte et renvoie la présence d'une pomme dans la carte"""
    global carte
    return carte[pos_y][pos_x] == 2


def generation_pomme():
    """permet de generer des pommes"""
    global score
    lim= len(carte) - 1
    one = randint(1, lim)
    two = randint(1, lim)
    while carte[one][two] != 0:
        one = randint(1, lim)
        two = randint(1, lim)
    carte[one][two] = 2
    affichage()


def move_snake(head_x, head_y):
    """Sert a déplacer le serpent"""
    global head_snake, serpent, carte

    head_snake = (head_x, head_y)
    serpent.insert(0, head_snake)
    carte[head_y][head_x] = 3


def snake():
    """Fonction qui réunit le déplacement et l'affichage du serpent"""
    move_snake(6, 7)
    affichage()


###################################################
#Fonctions relatives aux changements de directions

def haut(*args):
    global direct
    direct = "haut"


def bas(*args):
    global direct
    direct = "bas"


def gauche(*args):
    global direct
    direct = "gauche"


def droite(*args):
    global direct
    direct = "droite"


def mouvement():
    """permet de déplacer le snake"""
    global direct, carte, head_snake, serpent, score, scoreaff, cpt_pomme
    
    if direct is None:
        racine.after(vitesse, mouvement)
        return

    snake_x, snake_y = head_snake

    if direct == "haut":
        snake_y -= 1
    elif direct == "bas":
        snake_y += 1
    elif direct == "gauche":
        snake_x -= 1
    elif direct == "droite":
        snake_x += 1

    #si on est sur objet "mur" ou "serpent" on perd
    if carte[snake_y][snake_x] == 1 or carte[snake_y][snake_x] == 3:
        save_score()
        gameover()
        return

    #si on est sur la pomme
    if pomme_detector(snake_x, snake_y):
        move_snake(snake_x, snake_y)
        generation_pomme() # on génére une nouvelle pomme
        score += 1 # on incremente le score
        scoreaff.config(text= 'Score = ' + str(score)) #on affiche le nouveau score
    else: 
        move_snake(snake_x, snake_y)
        (last_x, last_y) = serpent.pop()
        carte[last_y][last_x] = 0
    
    #generation d'une pomme si premier passage
    if cpt_pomme == 0:
        generation_pomme()
        cpt_pomme = 1
        


    affichage()
    racine.after(vitesse, mouvement)

################################################################
# Affichages et fenêtres


def map_decoche(x,y):
    """permet de décocher les différentes tailles de cartes et enregistrer la sélection"""
    if x == 0:
        petite.deselect()
    if x == 1 or y == 1:
        moyenne.deselect()
    if y == 2:
        grande.deselect()
    somme = x + y
    if somme == 3:
        cartes(0)
    elif somme == 2:
        cartes(1)
    elif somme == 1:
        cartes(2)


def vit_decoche(x,y):
    """permet de décocher les différentes vitesses de jeu et d'enregistrer la sélection"""
    global vitesse
    if x == 0:
        lent.deselect()
    if x == 1 or y == 1:
        moyen.deselect()
    if y == 2:
        rapide.deselect()
    somme = x + y
    if somme == 3:
        vitesse = 300
    elif somme == 2:
        vitesse = 200
    elif somme == 1:
        vitesse = 100


def option_select():
    """permet de sélectionner la carte depuis un nouvel onglet"""
    global petite, moyenne, grande, lent, moyen, rapide, opt_select_frame, fenetreon
    opt_select_frame = tk.Tk()
    opt_select_frame.title("Options")
    fenetreon= True
    
    phrase1 = tk.Label(opt_select_frame, text= 'Choisissez le niveau que vous voulez jouer!')
    petite = tk.Checkbutton(opt_select_frame, text= 'Niveau 1', command= lambda: map_decoche(1,2))
    moyenne = tk.Checkbutton(opt_select_frame, text= 'Niveau 2', command= lambda: map_decoche(0,2))
    grande = tk.Checkbutton(opt_select_frame, text= 'Niveau 3', command= lambda: map_decoche(0,1))

    phrase2 =tk.Label(opt_select_frame, text='Choissisez la vitesse de la partie!')
    lent = tk.Checkbutton(opt_select_frame, text= 'Lent', command= lambda: vit_decoche(1,2))
    moyen = tk.Checkbutton(opt_select_frame, text= 'Moyen', command= lambda: vit_decoche(0,2))
    rapide = tk.Checkbutton(opt_select_frame, text= 'Rapide', command= lambda: vit_decoche(0,1))

    quitter_maps = tk.Button(opt_select_frame, text= 'Quitter', command= lambda: quitter(opt_select_frame))
    
    phrase1.grid(row= 0, column= 1, columnspan= 3)
    petite.grid(row= 2, column= 1)
    moyenne.grid(row= 2, column= 2)
    grande.grid(row= 2, column= 3)

    phrase2.grid(row= 4, column= 1, columnspan= 3)
    lent.grid(row= 5, column= 1)
    moyen.grid(row= 5, column= 2)
    rapide.grid(row= 5, column= 3)

    quitter_maps.grid(row= 6, column= 2, columnspan =2)
    opt_select_frame.mainloop()


def fenetreJeu():
    """permet de passer à l'affichage du jeu"""
    global fenetreon
    fenetreon = False
    if fenetreon == True:
        quitter(opt_select_frame)
    bvn.grid_remove()
    pseudo_entry.grid_remove()
    pseudo_label.grid_remove()
    btnjouer.grid_remove()
    maps.grid_remove()
       
    cartes(stock)
    affichage()
    snake()
    mouvement()

    canvas.grid()
    pseudoaff.grid()
    scoreaff.grid()


def save_score():
    """Sauvegarde des scores"""
    global score
    with open(filename, "a") as f_scoring:
        f_scoring.write(str(score) + " " + pseudo.get() + " \n")


def fenetre_score():
    """Affichage de la fenetre des scores"""
    f_score = tk.Tk()
    Score_label = tk.Label(f_score,text= "Voici les meilleurs scores",
                            font= ( "Time New Roman", 15),
                            background= 'green',
                            foreground= 'White'
                            )
    Score_label.grid(row= 1,column= 0)
    texte_area = st.ScrolledText(f_score, width= 30, height= 8, font= ("Time New Roman",15))
    texte_area.grid(row= 2, column= 0, pady= 0, padx= 0)

    
    with open(filename,"r") as f_old_scoring:
        oldscore = f_old_scoring.readlines()
        oldscore.sort(reverse=True)
        for scores in oldscore:
            texte_area.insert(tk.INSERT, str(" " +scores.upper()))
        texte_area.configure(state= 'disabled')
        
    f_score.mainloop()

######################
# Programme principal
######################
# Création des widgets 

"""Pour le menus"""
bvn= tk.Label(racine, text= "SNAKE", font= ("Times", "30", "italic"), fg= "green")
pseudo_entry = tk.Entry(racine, textvariable= pseudo)
pseudo_label = tk.Label(racine, text= "Pseudo :")
btnjouer = tk.Button(racine, text= 'Go!', width= 15, command= fenetreJeu)
close = tk.Button(racine, text= "Close", width= 10, command= lambda: quitter(racine))
maps = tk.Button(racine, text= "Options", width= 10, command= option_select)

"""Pour l'écran de jeu"""
canvas = tk.Canvas(racine, width= str(WIDTH), heigh= str(HEIGHT), bg= "black")
pseudoaff = tk.Label(racine, textvariable= pseudo)
scoreaff = tk.Label(racine, text= "Score = " + str(score))
ancien_score = tk.Button(racine, text= "Anciens score", command= fenetre_score)

###################
# Placement widgets

"""Pour le menus"""
bvn.grid(row= 1, column= 1, columnspan= 3)
pseudo_label.grid(row= 2, column= 1)
pseudo_entry.grid(row= 2,column= 2)
btnjouer.grid(row= 3, column= 2)
maps.grid(row= 2, column= 3)
close.grid(row= 3, column= 3)


"""Pour l'écran de jeu"""
canvas.grid(column= 1, row= 2, columnspan= 3)
canvas.grid_remove()
pseudoaff.grid(column= 1, row= 1)
pseudoaff.grid_remove()
scoreaff.grid(column= 3, row= 1)
scoreaff.grid_remove()
ancien_score.grid(row= 3, column= 1)

########################
# Liaison des événements

racine.bind("<Up>", haut)
racine.bind("<Down>", bas)
racine.bind("<Left>", gauche)
racine.bind("<Right>", droite)
racine.resizable(False, False)

racine.mainloop()
