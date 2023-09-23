from flask import Flask, render_template,request

from shop import app, db, test_collection, test_collection2
import os


picfolder = os.path.join('static','images')
app.config['UPLOAD_FOLDER'] =picfolder
@app.route('/')
def home1():
    pic1= os.path.join(app.config['UPLOAD_FOLDER'],'4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')


    return render_template("index.html",**locals())
@app.route('/home')
def home():
    pic1= os.path.join(app.config['UPLOAD_FOLDER'],'4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')


    return render_template("index.html",**locals())

@app.route('/aboutus')
def aboutus():
    pic1= os.path.join(app.config['UPLOAD_FOLDER'],'4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')

    return render_template("aboutus.html",**locals())

@app.route('/mobile')
def mobile_categories():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    return render_template("index2.html",**locals())

@app.route('/computer')
def computer_categories():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    return render_template("computer.html",**locals())

@app.route('/headphone')
def headphone_categories():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    return render_template("headphone.html",**locals())


@app.route("/registration",methods=['GET','POST'])
def registration():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')


    post=False
    if request.method=='POST':
        post=True
        username=request.form['username']
        password=request.form['password']
        cpassword=request.form['cpassword']
        error=""
        if password != cpassword:
            error="Password didn't match"
        elif password==cpassword:
            result = test_collection.find_one({"username": username})
            if result is not None:
                error="User already exists."
            else:
                test_collection.insert_one(dict(request.form))
                error=username+" added successfully,Go to login page"
    return render_template("registration.html",**locals())


@app.route("/login",methods=["GET","POST"])
def login():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')


    post = False
    if request.method == 'POST':
        post = True
        username = request.form['username']
        password = request.form['password']
        error = ""
        result = test_collection.find_one({"username": username,"password":password})
        if result is None:
            error = "Password Did not match"
        else:
            error = "Login Successful."
    return  render_template("login.html",**locals())



