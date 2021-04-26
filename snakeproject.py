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

### pendant le menu principal<
pseudo= 'pseudo'
score= 0


######################
# Fonction

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


def gameover():
    """termine la partie"""
    tk.messagebox.showinfo(title='Game Over', message='Game Over')


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

racine = tk.Tk()
racine.title("project snake")

######################
# Création des widgets

canvas = tk.Canvas(racine, width=str(WIDTH), heigh=str(HEIGHT), bg="black")
label= tk.Label(racine, text= pseudo)
scoreaff = tk.Label(racine, text= "Score = " + str(score))

#######################
# Placement des widgets

canvas.grid(column=1, row= 2, columnspan=2)
label.grid(column=1, row= 1)
scoreaff.grid(column=2, row= 1)

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