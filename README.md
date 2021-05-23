# Snake-projet
## Qu'est-ce que c'est?

Snake est un jeu apparu dans les années 70!  
Le joueur doit diriger un serpent pour récupérer les pommes qui apparaissent aléatoirement. A chaque pomme mangé le serpent grandit. 

Le but : Manger le plus de pomme.

## Les commandes 

Toutes les commandes sont accéssibles à partir du clavier ou de la souris.
Le déplacement du serpent s'efffectue uniquement avec les fléches du clavier.
Pour les commandes ont a voulu choisir des touches instinctives et donc facile d'utilisation.  

### Pour le menus

Nous avons défini deux menus

Un menu principal vous trouverez :   
    * Une zone de texte pour rentrer votre pseudonyme  
    * Un bouton *Options* pour accéder au sous menu permettant de définir la taille de la carte et la vitesse du serpent.  
    * Un bouton *Ancien score* pour accéder à tout les scores ranger par ordre décroissant   
    * Un bouton *close* pour fermer la fenêtre  
    * Un bouton *Go!* pour commencer la partie  
    * Le sous menu accéssible en cliquant sur le bouton *Options* est composer de deux parties:
    =>Il y a donc trois niveaux au choix à cocher:  
            - Niveau 1 (facile/ classic)
            - Niveau 2 (difficulté moyenne)
            - Niveau 3 (difficulté maximale)
    => Le choix de la vitesse du serpent :  
        - Lent  
        - Moyen   
        - Rapide  
    que l'on selectionne par une case a chocher.  
On sort de ce sous menu en cliquant sur le bouton *Quitter*  - Retour au menu principal  



### Pour la fenêtre de jeu

Dans cette fenêtre il y a :  
    * Pour déplacer le serpent : il faut utiliser les flèches de son clavier  
        Les déplacement : Haut, Bas, Droite, Gauche  
    * Un bouton *Ancien score* pour accéder à tout les scores ranger par ordre décroissant  

## Autre widgets utilisé
### Pour le menus

On trouvera les widgets suivant:  
    * Un Label pour afficher le titre du menus qui est *Snake*  
    * Un Label qui affiche *Pseudo* à côté de la zone de texte  

### Pour la fenêtre de jeu

On trouvera sur cette fenêtre:  
    * En haut a droite : un Label pour afficher le pseudo choisi par le joueur  
    * En haut à gauche : un Label qui affiche le score en temps réel  
    * Au centre il y aura le canvas où le jeu se passera   

## Les règles

1- Le serpent peut se diriger dans 4 directions : Droite, gauche, en haut et en bas  
2- Il doit ramasser le plus de pomme possible  
3- Une pomme fait remporter un point  
4- Si le serpent percute le mur ou son propre corp c'est Game Over  
5- Il n'y a pas de limite de temps  

## Les difficultés rencontrées  

### LARA ESPINASSE

#### Difficultés du travail en équipe

Lors de ce projet une des difficultés que j'ai rencontré est celle du travail en équipe. Répartition des taches, force et faiblesse de chacun, choix de solution différentes. De plus nous n'avons eu l'occasion de se réunir en presentiel pour apprendre à se connaitre.   
Les façons de travailler de chacun sont differentes et difficile à concillier.  
Nous aurions pu, peut être, monter des points plus réguliers pour essayer de partager nos divergences.  

#### L'affichage des score

En effet, je me demandais comment j'allais afficher les scores.   
Est-ce que je devais créer un bouton qui générait la page de tout les fichiers présent sur notre ordinateur et aller le chercher nous même?   
Est-ce que je devais seulement enregistrer les score dans un fichier?  
Je me posais plein de questions. Ce que j'ai donc fait:   
    J'ai fait un bouton qui génère une page où tous les scores s'affichent par ordre décroissant.  
    La création de fichier se fait par la fonction *save* que j'appelle dans le fonction *game_over*. De ce fait lorsque le tout premier joueur perd, un fichier se créer à l'emplacement initial où se trouve le joueur.  

#### Le serpent

En soit, le serpent n'était pas compliqué à créer, cependant on aurait bien voulu faire la distinction entre la tête et le corps. A ce jour, le serpent est entièrement d'un vert uniforme. L'idéal aurait été que la tête soit plus foncé ou plus clair mais nous n'avons pas trouvé comment faire.