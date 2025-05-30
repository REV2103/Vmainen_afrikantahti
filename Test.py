from flask import Flask, jsonify, render_template, Response, redirect, request
from flask_cors import CORS
import json
import mysql.connector
import random

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='vmainen_afrikantahti',
    user='mrkill',
    password='nibs',
    autocommit=True,
    collation='utf8mb3_general_ci'
)


num = random.randint(1, 95)

sql = f"select Cardnum, Name, Effect from cards where Cardnum = '{num}' LIMIT 1;"
cursor = yhteys.cursor()
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    card_id = row[0]
    card_name = row[1]
    card_effect = row[2]
print(card_id, card_name, card_effect)
