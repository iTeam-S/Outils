import json

def get(key, lang):
	fichier=open("langs.json")
	trans=json.load(fichier)
	mot_cle=trans.get(key)

	if mot_cle:
		return mot_cle.get(lang) \
	    	if mot_cle.get(lang) else key
	else:
		return key

	return trans.get(key).get(lang)
