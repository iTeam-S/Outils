import os
import requests
import mysql.connector
from bs4 import BeautifulSoup


def add_user_github_pic(database):
    """
        Mettre à jour les liens des avatars github des membres
        dans la base ITEAMS s'il n'y en a pas
        - database: Dict [Info sur la base]
        -> return: None
    """
    db = mysql.connector.connect(**database)
    cursor = db.cursor()

    cursor.execute("""
        SELECT id, user_github FROM membre
        WHERE user_github IS NOT NULL AND user_github_pic IS NULL
    """)

    for val in cursor.fetchall():
        print('\n[INFO] ', val[0], '=>', val[1])
        cursor.execute(
            'UPDATE membre SET user_github_pic=%s WHERE id=%s',
            (get_user_github_pic('https://github.com/'+val[1]), val[0])
        )

    db.commit()
    db.close()


def get_user_github_pic(user_github_url):
    """
        Obtenir le lien de l'avatar d'un membre via le lien de son
        profil github
        - user_github_url: String [Lien du profil]
        -> return: String [Lien de l'avatar]
    """
    r = requests.get(user_github_url)

    print('[STATUS] : ', r.status_code)

    src_code = BeautifulSoup(r.text, 'html.parser')
    for src in src_code.find_all(alt='Avatar'):
        img_link = src.get('src')
        return img_link[:img_link.find('?')]


if __name__ == '__main__':

    database = {
        'user': os.environ.get("ITEAMS_USER"),
        'host': os.environ.get("ITEAMS_HOST"),
        'database': os.environ.get("ITEAMS_DB"),
        'password': os.environ.get("ITEAMS_PASS"),
    }

    add_user_github_pic(database)
