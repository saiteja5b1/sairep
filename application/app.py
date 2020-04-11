from flask import Flask,render_template,url_for,request
from flask_login import login_required
import json
from db_connect import connect
from cc import cc


app=Flask(__name__)

""" creating different routes for different webpages """
@app.route('/')
def home():
    # data=['yesu','10','9849643914','kankipadu','ANDHRA PRADESH','KRISHNA','KANKIPADU']
    # connect(data)
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/services')
def services():
    return render_template('farmersearch.html')

@app.route('/about')
def aboutus():
    return render_template('aboutus.html')

@app.route('/contact')
def contactus():
    return render_template('contactus.html')
# @app.login('/login',methid)

@app.route('/register',methods=['GET'])
def register():
    with open('datasets/dat.json','r') as f:
        datalist=json.load(f)
    dist=list(datalist.keys())    
    return render_template('register.html',datalist=datalist,districts=dist)

# @app.route('/register',methods=['POST'])
# def getvalue():
#     name=request.form['Name']
#     age=request.form['Age']
#     phone=request.form['PhnNo']
#     address=request.form['Address']
#     district=request.form['District']
#     mandal=request.form['Mandal']
#     connect('yesu4658',[name,age,phone,address,'andhrapradesh',district,mandal])
#     return render_template('hello.html',name=name,age=age,phno=phone,address=address,district=district,mandal=mandal)

@app.route('/arable',methods=['GET','POST'])
def arable():
    with open('datasets/arable.json') as f:
        crops=json.load(f)
    return render_template('arable.html',datalist=crops)

@app.route('/view')
@login_required
def viewProfile():
    return render_template('login.html')


""" main app calling """
if __name__=="__main__":
    app.run(debug=True)