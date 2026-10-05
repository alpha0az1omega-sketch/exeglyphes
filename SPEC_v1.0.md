# EXEGLYPHE - Specification v1.0

## 1. Format
Fichier HTML unique, encode UTF-8.

## 2. Balises obligatoires dans head
- meta name=exeglyphe content=1.0
- meta name=hash id=expected-hash content=sha256_hex_64
- meta name=created content=ISO-8601
- meta name=title content=titre

## 3. Balises optionnelles
- meta name=parent content=sha256_hex_64
- meta name=author content=nom
- meta name=license content=MIT|CC-BY

## 4. Section script id=core
- Code de calcul encadre par :
  - Debut : // === EXEGLYPHE COMPUTATION CODE ===
  - Fin :   // === FIN DE LA SECTION HACHEE ===
- Type : text/x-exeglyphe (non execute automatiquement)
- Le hash porte sur le contenu de #core

## 5. Self-verification
Le fichier doit contenir un script qui :
1. Lit le contenu de #core
2. Calcule son SHA-256
3. Compare avec meta name=hash
4. Si identique : execute via new Function(core)
5. Si different : affiche une erreur

## 6. Contraintes
- Taille : < 50 Ko
- Aucun appel reseau
- Aucun cookie
- Aucune dependance externe

## 7. Compatibilite
Chrome, Firefox, Safari, Brave.
Safari iOS : crypto.subtle restreint en file://

## 8. Version
1.0 (2026-10-05)
