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
from random import randint
from tkinter.messagebox import *

######################
# CONSTANTES


WIDTH = 500
HEIGHT = 500
carre = 11
x, y = WIDTH / carre, HEIGHT / carre

#######################
# Variables globals

direct = None
vitesse = 300

carte = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
         ]


head_snake = (0, 0)
serpent = []

objets = []

racine = tk.Tk()
racine.title("project snake")

######################
#Variables de l'écran principal
score= 0
pseudo= tk.StringVar()


####FONCTIONS DU JEU

######################
# Fonction
def quitter():
    """permet de quitter la fenêtre actuelle"""
    racine.destroy()

def cartes():

    carte_une = []
    for i in range(125):
        temp = []
        for j in range(125):
            if i == 0 or i == 124 or j == 0 or j == 124:
                temp.append(1)
            else:
                temp.append(0)
        carte_une.append(temp)

def reset():
    global score, pseudo, carte, objets, serpent, head_snake, direct
    
    carte = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
             ]

    head_snake = (0, 0)
    serpent = []
    objets = []
    direct = None


    score = 0
    pseudo.set('')

    affichage()
    generation_pomme()
    snake()
    mouvement()


def gameover():
    """termine la partie"""
    tk.messagebox.showinfo(title='Game Over', message="Game Over \n vous allez retourner vers l'écran principal")
    reset()
    canvas.grid_remove()
    label.grid_remove()
    scoreaff.grid_remove()

    bvn.grid()
    pseudo_label.grid()
    pseudo_entry.grid()
    btnjouer.grid()
    

def affichage():
    """créer la génération du terrain, du mur du snake et 
       de la pomme avec des chiffres pour l'utiliser avec une matrice"""
    global objets
    if len(objets) != 0:
        for elem in objets:
            canvas.delete(elem)
        objets = []
    for i in range(len(carte)):
        for j in range(len(carte[0])):
            if carte[j][i] == 1:
                mur = canvas.create_rectangle(x * i, y * j, (x * i) + x, (y * j) + y, fill="wheat2", outline="black")
                objets.append(mur)
            elif carte[j][i] == 0:
                herbe = canvas.create_rectangle(x * i, y * j, (x * i) + x, (y * j) + y, fill="pale green",
                                                outline="pale green")
                objets.append(herbe)
            elif carte[j][i] == 2:
                pomme1 = canvas.create_rectangle(x * i, y * j, (x * i) + x, (y * j) + y, fill="pale green",
                                                 outline="pale green")
                pomme2 = canvas.create_oval((x * i) + 10, (y * j) + 10, ((x * i) + x) - 10, ((y * j) + y) - 10,
                                            fill="firebrick2")
                objets.append(pomme1)
                objets.append(pomme2)
            elif carte[j][i] == 3:
                tete = canvas.create_rectangle(x * i, y * j, (x * i) + x, (y * j) + y, fill="springgreen4",
                                               outline="springgreen4")
                objets.append(tete)


def pomme_detector(pos_x, pos_y):
    global carte
    return carte[pos_y][pos_x] == 2


def generation_pomme():
    global score
    one = randint(1, 9)
    two = randint(1, 9)
    while carte[one][two] != 0:
        one = randint(1, 9)
        two = randint(1, 9)

    carte[one][two] = 2
    affichage()


def move_snake(head_x, head_y):
    global head_snake, serpent, carte

    head_snake = (head_x, head_y)
    serpent.insert(0, head_snake)
    carte[head_y][head_x] = 3


def snake():
    move_snake(6, 7)
    affichage()


def mouvement():
    global direct, carte, head_snake, serpent, score, scoreaff
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

    if carte[snake_y][snake_x] == 1 or carte[snake_y][snake_x] == 3:
        gameover()
        return

    if pomme_detector(snake_x, snake_y):
        move_snake(snake_x, snake_y)
        generation_pomme()
        score += 1
        scoreaff.config(text= 'Score = ' + str(score))
    else:
        move_snake(snake_x, snake_y)
        (last_x, last_y) = serpent.pop()
        carte[last_y][last_x] = 0

    affichage()
    racine.after(vitesse, mouvement)

###Fonctions relatives aux changements de directions#############
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

######################
# Programme principal


#####################
# Placement des widgets
def fenjeu():
        bvn.grid_remove()
        pseudo_entry.grid_remove()
        pseudo_label.grid_remove()
        btnjouer.grid_remove()
        
        canvas.grid()
        label.grid()
        scoreaff.grid()



######################
# Création des widgets
bvn= tk.Label(racine, text= "SNAKE", font = ("Times", "30", "italic"), fg= "green")
bvn.grid(row=1, column=1, columnspan=3)
pseudo_entry = tk.Entry(racine, textvariable= pseudo)
pseudo_entry.grid(row=2,column=2)
pseudo_label= tk.Label(racine, text="Pseudo :")
pseudo_label.grid(row=2, column=1)
btnjouer= tk.Button(racine, text='Go!',width= 15, command= fenjeu)
btnjouer.grid(row=3, column=2)
close = tk.Button(racine, text= "Close", command= quitter)
close.grid(row=3, column=3)




canvas = tk.Canvas(racine, width=str(WIDTH), heigh=str(HEIGHT), bg="black")
canvas.grid(column=1, row= 2, columnspan=2)
canvas.grid_remove()
label= tk.Label(racine, textvariable= pseudo)
label.grid(column=1, row= 1)
label.grid_remove()
scoreaff = tk.Label(racine, text= "Score = " + str(score))
scoreaff.grid(column=2, row= 1)
scoreaff.grid_remove()

######################
# Appel  de fonctions

affichage()
generation_pomme()
snake()
mouvement()

########################
# Liaison des événements

racine.bind("<Up>", haut)
racine.bind("<Down>", bas)
racine.bind("<Left>", gauche)
racine.bind("<Right>", droite)
racine.resizable(False, False)

racine.mainloop()
