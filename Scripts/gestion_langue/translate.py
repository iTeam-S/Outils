import json


def get(key, lang):
    fichier = open("langs.json")
    mot_cle = json.load(fichier).get(key)

    return mot_cle.get(lang) or key if mot_cle else key
