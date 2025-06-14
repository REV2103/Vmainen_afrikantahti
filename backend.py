from flask import Flask, jsonify, render_template, Response, redirect, request
from flask_cors import CORS
import json
import mysql.connector
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='vmainen_afrikantahti',
    user='mrkill',
    password='nibs',
    autocommit=True,
    collation='utf8mb3_general_ci'
)

@app.route('/cardselect')
def cardselector():
    try:
        card_id = ""
        card_name = ""
        card_effect = ""
        tilakoodi = 200

        num = random.randint(1, 95)

        sql = f"select Cardnum, Name, Effect from cards where Cardnum = '{num}' LIMIT 1;"
        cursor = yhteys.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            card_id = row[0]
            card_name = row[1]
            card_effect = row[2]
        response = {
            "Card ID": card_id,
            "Card Name": card_name,
            "Card Effect": card_effect
        }
    except ValueError: 
        tilakoodi = 400
        response = {
                "status": tilakoodi,
                "teksti": "Virheellinen luku"
            }
    jsonvast = json.dumps(response)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)  # error handling
def page_not_found(error):
    return jsonify({"error": "Not found", "code": 404}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)