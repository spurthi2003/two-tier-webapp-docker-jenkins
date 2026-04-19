from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="root123",
        database="mydb"
    )

@app.route("/")
def home():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT message FROM greetings LIMIT 1;")
        row = cursor.fetchone()
        msg = row[0] if row else "No data found"
        conn.close()
    except Exception as e:
        msg = str(e)

    return render_template("index.html", message=msg)

app.run(host="0.0.0.0", port=5000)