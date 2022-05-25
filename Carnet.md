# Jeu de Survie - Duthé Ryan

### Commit 23/03/2033

== Documentation == 

Modularité : https://youtu.be/A2aD4eQP0qU  
POO : https://youtu.be/s2pnrMKpEp0 / https://youtu.be/h6jciR8K43E / https://youtu.be/fW4818AS88I / https://youtu.be/91dPooHyNIo  
Exemple de création de jeu sous PyGame : https://youtu.be/ooITOxbYVTo (Visionné jusqu'à la moitié)  

== Code == 

- Installation des modules nécessaires
- Création et Implémentation de la Carte
- Création du joueur + déplacements de base

### Commit 30 / 03 / 2022

== Documentation == 

Exemple de création de jeu sous PyGame : https://youtu.be/ooITOxbYVTo

== Code == 

- Ajout déplacement en diagonales
- Correction des calques de la carte
- Ajout de détails sur la carte
- Sprite ajouté selon les déplacements (aucune animation pour le moment)
- Ajout des collisions + correction des zones de collisions
- Ajout jeu de tuiles pour la Maison
- Création de la Carte Maison

## Commit 06 / 04 / 2022

== Documentation == 

Exemple de création de jeu sous PyGame : https://youtu.be/ooITOxbYVTo (vidéo finie) -> Code non copié-collé en une fois, écrit progressivement durant la vidéo  
Seconde Partie : https://youtu.be/clcmhmpyYSc  

== Code ==

- Finalisation de la map house.tmx
- Code pour rentrer & sortir de la maison
- Correction des collisions

## Commit 08 / 05 / 2022 (absences + vacances)

== Code ==

- Apparition des premiers PNJ et de leurs dialogues
- Création d'un semblant de Lore
- Correction d'un bug de fichiers (pas trouvé de réelle solution), retour au dernier commit

# Commit 17/05/2022

== Documentation == 

Tuto Graven (fini) : https://youtu.be/clcmhmpyYSc

== Code ==

- Refonte de la gestion de cartes / changement de carte
- Animation du Player
- Apparition des PNJ et de leur dialogue (espace pour leur parler)
- Apparition des 10 zombies sur une troisième map (au nord)
- Fonction pour faire des dégâts aux zombies faites
- Correction graphique : on passe maintenant derrière les arbres / la maison

# Commit 23/05/2022

Plus aucune documentation

== Code ==

- Damage des zombies + mort des zombies + respawn des zombies aléatoirement en haut de map
- Déplacement et animation des zombies
- Damage du joueur + mort du joueur
- Apparition du score
- Apparition des points de competences
- Apparition des améliorations de stats (vie et damage)
- Affichage des données (points de vie, damage, score et score max)
- Amélioration des zombies en fonction du score (-> Données)


== Commades ==

- Attaquer les zombies : espace
- Dialogue des PNJ : espace
- Amélioration de la vie : a
- Amélioration des déâts : z
- Déplacement : fleches

== Données ==

- 1 point de competence gagné tous les 10 zombies tués
- 1 point de score par zombie tué
- Score de l'amélioration des points de vie : 7 (+50) 
- Score de l'amélioration des degats : 10 (+2)

- Vie de base : 300
- Dégâts de base : 15
- Vitesse : 2
- Amélioration de la vie : +50 et régéneration de la vie au max 
- Amélioration des dégâts : 2

- Vie de base des zombies : 150
- Vitesse des zombies : de 0.7 à 1.6
- Dégâts des zombies : 5 (attaque apres deux secondes de contact continu ou discontinu)
- Amélioration des zombies tous les 100 de score : +1 damage et +20 vie

# Commit 24/05/2022

== Code ==

- Reset de la map "zombie" lors de la mort du joueur (replacement des zombies + retour aux stats de base)
- 