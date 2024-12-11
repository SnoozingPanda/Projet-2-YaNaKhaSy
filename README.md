# Recommandation de films v1

Ce projet est le deuxième projet professionnel du bootcamp Data Analyst de la Wild Code School à Paris

Un cinéma de la Creuse en perte de vitesse a décidé de sauter le pas du numérique et a demandé à notre équipe de créer une application de recommandation de films
afin tout autant de fidéliser sa clientèle que d'attirer de nouveaux cinéphiles

J'ai tenu le rôle de Scrum Master dans ce projet, et je me suis occupé d'une partie du nettoyage des données, des systèmes de recommandation, et de l'application Streamlit
Khadija étaot ma partenaire pour la réalisation de ces tâches tandis que Yanis et Naser ont plus particulièrement réalisé les dashboard

Après une première analyse des données fournies et des données socio-démographiques de la Creuse nous avons choisi d'orienter le choix de films vers les films français
sortis entre 1960 et 1990

Le travail de nettoyage des données s'est effectuée avec la librairie Pandas (Python)
En deuxième analyse les différents fltres appliqués aux données ne nous ont pas permis de ne conserver que les films français (trop peu de films français dans les jeux de données), alors nous avons choisi de nous concentrer sur les films sortis entre 1960 et 1990

A l'issue de cette première étape nous avons pu proposer un dashboard des films que nous avons conservé ainsi que des acteurs que les spectateurs pourraient voir dans ces films

Parallèlement à ce travail de présentation, l'application a été réalisée avec le framework Streamlit qui permet de présenter une page web interactive
Deux modèles de machine learning nous ont permis de recommander les films par leurs caractéristiques "numériques" (année de sortie, note, ...) avec un KNearest Neighbors
et une recommandation par mots-clés grâce à un CountVectoriser


NB: Ce projet est une v1.
Une v2 est en cours de développement avec des améliorations significatives notamment une refonte du code pour une meilleure lisibilité
