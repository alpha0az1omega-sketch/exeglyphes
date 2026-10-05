# MANIFESTE - EXEGLYPHE

Un exeglyphe est un fichier qui se prouve lui-meme.

## Qu'est-ce que c'est ?

Un fichier HTML autonome. A l'ouverture :
- Il verifie son propre hash SHA-256.
- Si le hash est bon, il s'execute.
- Si le hash est mauvais, il refuse de s'executer.

L'oeuvre n'est pas une image. L'oeuvre est un calcul.

## Qu'est-ce que ce n'est pas ?

- Pas une image : l'image change a chaque frame.
- Pas une video : il n'y a rien de pre-enregistre.
- Pas une app : pas d'installation, pas de permission.
- Pas un NFT : pas de token, pas de blockchain, pas de marketplace.

## Les 5 regles

1. Un seul fichier HTML. Tout est dedans.
2. Aucun appel reseau.
3. Auto-verifie. Le hash SHA-256 est dans le fichier.
4. Portable. Fonctionne hors ligne.
5. Partageable. Par SMS, mail, USB.

## Pourquoi

Parce que l'infrastructure tue l'oeuvre.

Les plateformes meurent (fxhash, aout 2026).
Les blockchains coutent.
Les serveurs tombent.

Un exeglyphe ne depend de rien.
Un fichier. Un hash. Un ecran.

## Comment en creer un

1. Copier exeglyphe_001.html
2. Modifier la section script id=core
3. Lancer : python3 compute_hash.py mon_exeglyphe.html
4. Ouvrir dans un navigateur

## Comment le partager

- Par mail : piece jointe .html
- Par SMS : envoyer le hash (64 caracteres)
- Par cle USB : copier le fichier
- Par GitHub Pages : heberger, partager le lien

## La chaine humaine

Chaque exeglyphe peut contenir un parent hash.
Ce hash pointe vers l'exeglyphe parent.
La chaine n'est pas sur une blockchain. Elle est dans les emails.

## Qui

alpha0az1omega
Cree le 2026-10-05
MIT + CC-BY 4.0
