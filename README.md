# Snake-projet
## Qu'est-ce que c'est?

Snake est un jeu apparu dans les années 70!  
Le joueur doit diriger un serpent pour récupérer les pommes qui apparaissent aléatoirement. A chaque pomme mangé le serpent grandit. 

Le but : Manger le plus de pomme.

## Les commandes 

Toutes les commandes sont accéssibles à partir du clavier ou de la souris.
Le déplacement du serpent s'efffectue uniquement avec les fléches du clavier.
Pour les commandes on a voulu choisir des touches instinctives et donc facile d'utilisation.  

### Pour le menus

Nous avons défini deux menus

Un menu principal vous trouverez :   
    * Une zone de texte pour rentrer votre pseudonyme  
    * Un bouton *Options* pour accéder au sous menu permettant de définir la taille de la carte et la vitesse du serpent.  
    * Un bouton *Anciens scores* pour accéder à tout les scores ranger par ordre décroissant   
    * Un bouton *Close* pour fermer la fenêtre  
    * Un bouton *Go!* pour commencer la partie  
    * Le sous menu accéssible en cliquant sur le bouton *Options* est composer de deux parties:
    =>Il y a donc trois niveaux au choix à cocher:  
            - Niveau 1 (facile/ classic)
            - Niveau 2 (difficulté moyenne)
            - Niveau 3 (difficulté maximale)
    => Le choix de la vitesse du serpent au chois à cocher:  
        - Lent  
        - Moyen   
        - Rapide  
On sort de ce sous menu en cliquant sur le bouton *Quitter*  - Retour au menu principal  



### Pour la fenêtre de jeu

Dans cette fenêtre il y a :  
    * Pour déplacer le serpent : il faut utiliser les flèches de son clavier  
        Les déplacement : Haut, Bas, Droite, Gauche  
    * Un bouton *Anciens score* pour accéder à tout les scores ranger par ordre décroissant  

## Autre widgets utilisé
### Pour le menus

On trouvera les widgets suivant:  
    * Un Label pour afficher le titre du menu qui est *Snake*  
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
4- Si le serpent percute le mur ou son propre corps c'est Game Over  
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

### OLIVIER COTTIN

Lors de ce projet, la plus grande difficulté a été le travail en équipe. Comme nous n'avons pas eu beaucoup de jour en présentiel, nous n'avons pas pu nous réunir en présentiel. Nous aurions pu cependant nous obliger à faire des points plus régulier afin de gérer plus facilement la répartition des tâches par rapport à l'avancée du projet.

### Les différents menus

La partie qui m'était attribuée était la création et l'organisation des menus. En effet je m'étais proposé pour créer les menus et les interactions entre les différentes fenêtres car j'avais du faire le même genre de fonctions pour d'autre projets. Ainsi la création des différentes fenêtres et menus étaient assez proche de ce que j'avais fait auparavant. 
Cependant j'ai eu du mal à créer le menu *Options*. En effet j'ai été obligé de créer une nouvelle fonction qui décochait les cases déja coché du même "type" (soit pour ce qui est de la carte, soit la vitesse). 
Pour cela j'ai:
-> attribué une valeur à chacune des cases à cocher: O pour la première, 1 pour la deuxième et 2 pour la troisième.
-> à chaque fois que l'on coche une case j'appelle ainsi une fonction utilisant deux variables: x et y. Cette fonction permet de décocher en faisant .deselect(). Les cibles de cette fonction sont déterminées grâce a x et y qui peuvent avoir une valeur allant de 0 à 2.
-> Cette fonction sert par ailleurs à enregistrer la sélection, en modifiant des variables globales qui définissent certaines règles du jeu (carte et vitesse).

### La sélection de la carte

La sélection de la carte à aussi été une partie difficile à créer. En effet nous avons eu beaucoup de mal (avec Gabriel, nous avons eu beaucoup de mal à le faire, même à deux) à faire en sorte d'ouvrir le fichier et de copier les valeurs du ficher en .txt dans une variable sous forme de liste de liste avec des "int" . En effet au début nous y arrivions mais le format contenu dans la liste de liste (au sein de la variable ' carte ') ne convenait pas au reste des fonctions d'affichage. 
Je pense que nous avons eu des problèmes pour suivre cette consigne car nous nous y sommes pris trop tard par rapport au reste du programme. En effet au début nous n'avions qu'une seule carte, qui était écrite au sein du programme. 
 
