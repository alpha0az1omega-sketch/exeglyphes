# EXEGLYPHE 001 — Automate Cellulaire Règle 110

## Ce que c'est
Un automate cellulaire qui dessine sa propre évolution.
Chaque pixel est un bit. Chaque bit obéit à une règle.

## Pourquoi
Montrer qu'un visuel peut être un CALCUL, pas une image.
La règle 110 est Turing-complète — elle peut tout calculer.

## Comment
- Une ligne de 240 cellules (0 ou 1)
- Chaque cellule regarde ses 2 voisines
- Un triplet (gauche, centre, droite) donne le bit suivant
- La règle est un nombre binaire : 01101110 (= 110)

## Métriques calculées en direct
- Génération courante
- Cellules vivantes
- Entropie de Shannon

## Interaction
- Clic = nouvelle graine
- Reset automatique après 240 générations

## Fichier
versions/001_regle110/index.html

## Signature
SHA-256 affiché en bas de page (calculé au chargement)

## Ce qui est inédit
Le visuel N'EST PAS DESSINÉ. Il est calculé à chaque frame.
Retirer la règle = retirer l'image.
