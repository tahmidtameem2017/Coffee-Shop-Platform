import mysql.connector
import json

with open("db.json","r",encoding="utf-8") as f :
    data = json.load(f)


def get_connection():
    return mysql.connector.connect(
        host=data["host"],
        port=data["port"],
        user=data["user"],
        password=data["password"],
        database=data["database"]

    )
