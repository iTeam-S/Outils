import requests
import mysql.connector
from bs4 import BeautifulSoup
from config import DATABASE

def add_user_github_pic():
    db = mysql.connector.connect(
        host = DATABASE['host'],
        user = DATABASE['user'],
        password = DATABASE['password'],
        database = DATABASE['database']
    )

    cursor = db.cursor()

    cursor.execute("SELECT id, user_github FROM membre WHERE user_github_pic IS NULL;")

    result = cursor.fetchall()

    for tuple in result:
        if tuple[1] != 'null' and tuple[1] != None:
            print('\n[INFO] ', tuple[0], '=>', tuple[1])
            cursor.execute('UPDATE membre SET user_github_pic=%s WHERE id=%s', (get_user_github_pic('https://github.com/'+tuple[1]), tuple[0]))
            db.commit()

    cursor.close()
    db.close()

def get_user_github_pic(user_github_url):
    r = requests.get(user_github_url)

    print('[STATUS] : ', r.status_code)

    src_code = BeautifulSoup(r.text,'html.parser')

    for src in src_code.find_all(alt='Avatar'):
        img_link = src.get('src')
        return img_link[:img_link.find('?')]

add_user_github_pic()