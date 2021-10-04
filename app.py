
from flask import Flask,render_template,url_for,request,redirect
from flaskext.mysql import MySQL
from app import views


app=Flask(__name__)
mysql=MySQL()
app.config["MySQL_DATABASE_USER"]="root"
app.config["MySQL_DATABASE_PASSWORD"]=""
app.config["MySQL_DATABASE_DB"]="Insert"
app.config["MySQL_DATABASE_HOST"]="localhost"
mysql.init_app(app)

@app.route("/login",method=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("SELECT * from register where 'username'='"+username+"' and 'password'='"+password+"'")
        data=cur.fetchone()
        if data[2]==username and data[6]==password:
            return redirect(url_for('home',data=data[0]))
        else:
            error="invalid"
            return render_template("login.html")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        username=request.form['username']
        email=request.form['email']
        phone_number=request.form['phone_number']
        gender=request.form['gender']
        password=request.form['password']
        con=mysql.connect()
        cur=con.cursor()
        cur.execute("INSERT INTO register('name','username','email','phone_number','gender','password')VALUES (%s,%s,%s,%s,%s,%s)",(name,username,email,phone_number,gender,password))
        con.commit()
        return redirect('login')
    else:
        return render_template("register.html")

if(__name__=='__main__'):
    app.run(debug=True)