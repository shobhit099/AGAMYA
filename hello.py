from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__ , static_folder = 'static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.secret_key = 'super secret key'
db = SQLAlchemy(app)

class emp(db.Model):
    __tablename__ = 'emp'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), nullable= False)
    phone = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(250), nullable= False)
    skill = db.Column(db.String(250), nullable= False)
    username = db.Column(db.String(100), unique= True)
    charge = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(50), nullable = False)
    exp = db.Column(db.String(10), nullable = False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact_us.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup_emp', methods=["POST","GET"])
def signup_emp():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        address = request.form['address']
        skill = request.form['skill']
        username = request.form['username']
        charge = request.form['charge']
        password = request.form['password']
        gender = request.form['gender']
        exp = request.form['exp']
        user = emp(name = name, email = email, phone = phone, city = city, address = address, skill = skill, username = username, charge = charge, password = password, gender = gender, exp = exp)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login_emp'))
    return render_template('signup_emp.html')

@app.route('/login_emp',methods=["POST","GET"])
def login_emp():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = emp.query.filter_by(email = email).first()
        if user:
            if password == user.password:
                return 'success'
    return render_template('login_emp.html')

if __name__ == '__main__':
    app.run(debug=True)