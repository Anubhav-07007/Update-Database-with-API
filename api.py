from flask import Flask,request,jsonify
import mysql.connector as conn
import  logging
logging.basicConfig(filename='api.log',level=logging.DEBUG,format="%(asctime)s,%(name)s,%(levelname)s,%(message)s")

app=Flask(__name__)

try:
    mydb=conn.connect(host="localhost",user="root",passwd="ar@66007")
    logging.info('We are successfully connected with db %s',mydb)
except Exception as e:
    logging.exception(e)

cursor=mydb.cursor()

try:
    cursor.execute('show databases')
    logging.info('The available database name %s', cursor.fetchall())
except Exception as e:
    logging.exception(e)

@app.route('/insert',methods=["POST"])
def insert():
    try:
        if request.method=="POST":
            empid=request.json['empid']
            empname=request.json['empname']
            emp_mail=request.json['emp_mail']
            emp_phone=request.json['emp_phone']
            logging.info('The enter value is %s , %s , %s ,%s',empid,empname,emp_mail,emp_phone)
            cursor.execute("insert into anubhav.python values(%s , %s , %s ,%s)",(empid,empname,emp_mail,emp_phone))
            mydb.commit()
            return jsonify(str("successfully done"))
    except Exception as e:
        logging.exception(e)

if __name__=='__main__':
    app.run()
