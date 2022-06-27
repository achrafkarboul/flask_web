import cur as cur
from flask import Flask, request, render_template
import  psycopg2

app: Flask = Flask(__name__)



def get_db_connection():
    conn = psycopg2.connect(
        dbname='akuvitBD',
        user='akuvitpostgresql@akuvitpostgresql',
        host='akuvitpostgresql.postgres.database.azure.com',
        password='Achrafkarboul123456',
        port='5432')
    conn.autocommit = True
    return  conn



@app.route('/')
def main():
    return render_template('main.html')

@app.route('/main',methods=['POST'])
def submit():
    if request.method == 'POST':
        id = request.form['id']
        idb = request.form['idB']
        disp = request.form['disp']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO customers VALUES(id,idb,disp,current_timestamp);)""")
        conn.commit()
        cur.close()
        conn.close()
        return render_template('main.html')

