from flask import Flask,render_template,request
from flask_mysqldb import MySQL
import json
app=Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sasi@3010'
app.config['MYSQL_DB'] = 'Marks'

mysql = MySQL(app)

@app.route('/', methods = ['GET', 'POST'])
def entry():
        if request.method == 'POST':
            cusd = request.form
            name= cusd["name"]
            tl= cusd["tl"]
            en = cusd["en"]
            mt = cusd["mt"]
            sc = cusd["sc"]
            so = cusd["so"]
            to = cusd["to"]
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO Marksheet(Stu_Name, Tamil, English, Mathematics, Science, Social, Grade) Values(%s, %s, %s, %s, %s, %s, %s)",
                        (name, tl, en, mt, sc, so, to))
            mysql.connection.commit()
            cur.close()
        return render_template('index.html')
@app.route("/card", methods=['GET'])
def employee():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * from Marksheet;")
    data = cursor.fetchall()
    print(data)
    return render_template("card.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
