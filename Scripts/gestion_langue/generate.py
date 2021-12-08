import json
import os
import mysql.connector


def fetch_dico():
    """
        Fetch dictionary from iTeam-s database
        return tuple(keys, vals)
        Details :
            keys = ['keyword', lang1, lang2, ...]
            vals = [val_keyword, value1, value2, ...]
    """
    conn = mysql.connector.connect(
          user=os.environ.get("ITEAMS_USER"),
          host=os.environ.get("ITEAMS_HOST"),
          database=os.environ.get("ITEAMS_DB"),
          password=os.environ.get("ITEAMS_PASS"),
       )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Traduction")

    keys = cursor.column_names
    vals = cursor.fetchall()

    return keys, vals


if __name__ == '__main__':
    """
        Generate json file to contains dictionary
        fetched from database
    """
    keys, vals = fetch_dico()

    fichier = open("langs.json", "w")
    dico = {}

    for val in vals:
        dico[val[1]] = {keys[i]: val[i] for i in range(2, len(keys))}
        fichier_json = json.dumps(dico, indent=2, sort_keys=True)

    fichier.write(fichier_json)
    fichier.close()
