import requests, mysql.connector
from bs4 import BeautifulSoup
from config import DATABASE


def add_user_github_pic():
    db = mysql.connector.connect(**DATABASE)
    cursor = db.cursor()

    cursor.execute("""
        SELECT id, user_github FROM membre 
        WHERE user_github IS NOT NULL AND user_github_pic IS NULL
    """)

    for val in cursor.fetchall():
        print('\n[INFO] ', val[0], '=>', val[1])
        cursor.execute('UPDATE membre SET user_github_pic=%s WHERE id=%s', (get_user_github_pic('https://github.com/'+val[1]), val[0]))
    db.commit()
    db.close()


def get_user_github_pic(user_github_url):
    r = requests.get(user_github_url)

    print('[STATUS] : ', r.status_code)

    src_code = BeautifulSoup(r.text,'html.parser')
    for src in src_code.find_all(alt='Avatar'):
        img_link = src.get('src')
        return img_link[:img_link.find('?')]


if __name__ == '__main__':
    add_user_github_pic()