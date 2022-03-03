from flask import Flask, render_template, request, redirect, url_for, flash
from jinja2 import defaults
from forms import LoginForm, RegistrationForm
from flask_mail import Mail,Message
from flask_mysqldb import MySQL


app = Flask(__name__)
# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pythonlogin'

# Intialize MySQL
mysql = MySQL(app)

"""app.config['SECRET_KEY']=''
app.config['MAIL SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='chkartikeya02@gmail.com'
app.config['MAIL_PASSWORD']='password'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
"""
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/aboutus')
def about():
    return render_template("aboutus.html")

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if form.validate() and request.method == 'POST':
       return redirect(url_for('index'))

    return render_template('login.html', form = form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate() and request.method == 'POST':
        return redirect(url_for('login'))
    return render_template('register.html', form = form)

"""@app.route('/user',defaults={'name':'Guest'})
@app.route('/user/<name>')
def user(name):
    context=[
        { 'stuid': '2000042569','stuname': 'Prakash','sub1':89,'sub2':75,'sub3':69 },
        {'stuid': '2000041569', 'stuname': 'Abdul', 'sub1': 58, 'sub2': 79, 'sub3': 59},
        {'stuid': '2000040587', 'stuname': 'Revathi', 'sub1': 89, 'sub2': 87, 'sub3': 69}
    ]
    return render_template('user.html',data = name, con = context)
"""
if __name__ == '__main__':
    app.run(debug=True)