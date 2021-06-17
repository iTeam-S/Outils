import json
import os
import mysql.connector

conn = mysql.connector.connect(user=os.environ.get("ITEAMS_USER"), password=os.environ.get("ITEAMS_PASS"),
                              host=os.environ.get("ITEAMS_HOST"),database=os.environ.get("ITEAMS_DB"))

fichier=open("langs.json","w")   
dico={}
select_Traduction= """ SELECT*FROM Traduction"""
cursor=conn.cursor()
cursor.execute(select_Traduction)
row=cursor.column_names
result=cursor.fetchall()
for cle in result:
   dico[cle[1]] = {row[i]:cle[i] for i in range (2, len(row))}
   fichier_json = json.dumps(dico, indent=2, sort_keys=True)

fichier.write(fichier_json)
fichier.close()
