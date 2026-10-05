#!/usr/bin/env python3
import hashlib, re, sys, os

def valider(path):
    erreurs = []
    if not os.path.isfile(path):
        return ["Fichier introuvable"]
    taille = os.path.getsize(path)
    if taille > 50 * 1024:
        erreurs.append("Taille > 50 Ko")
    with open(path, 'r', encoding='utf-8') as f:
        contenu = f.read()
    for balise in ['exeglyphe', 'hash', 'created', 'title']:
        if not re.search('<meta name="' + balise + '"', contenu):
            erreurs.append("Balise manquante : " + balise)
    match = re.search('<meta name="exeglyphe" content="([^"]+)"', contenu)
    if match and match.group(1) != "1.0":
        erreurs.append("Version non supportee")
    match_core = re.search('<script id="core"[^>]*>(.*?)</script>', contenu, re.DOTALL)
    if not match_core:
        erreurs.append("Section core introuvable")
    else:
        core = match_core.group(1)
        h_calcule = hashlib.sha256(core.encode('utf-8')).hexdigest()
        match_hash = re.search('<meta name="hash" id="expected-hash" content="([^"]+)"', contenu)
        if match_hash:
            h_declare = match_hash.group(1)
            if h_declare == "REMPLACER_PAR_HASH":
                erreurs.append("Hash non configure")
            elif h_calcule != h_declare:
                erreurs.append("Hash incoherent")
    if re.search(r'fetch\s*\(|XMLHttpRequest|cdn\.', contenu):
        erreurs.append("Appel reseau detecte")
    return erreurs

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage : python3 validator.py fichier.html")
        sys.exit(1)
    path = sys.argv[1]
    erreurs = valider(path)
    print("=" * 60)
    print("VALIDATION :", path)
    print("=" * 60)
    if not erreurs:
        print("OK - EXEGLYPHE VALIDE v1.0")
    else:
        print("INVALIDE :")
        for e in erreurs:
            print("  -", e)
        sys.exit(1)
