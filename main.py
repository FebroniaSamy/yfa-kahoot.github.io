from flask import Flask, render_template,request,session,redirect,url_for,make_response
from register import register_class
import json
import hashlib


app=Flask(__name__, template_folder='templates', static_folder='Static')
app.secret_key="STP"




@app.route('/Kahoot')
def Kahoot():
    return render_template('Kahoot.html')


@app.route('/sign in', methods=["GET","POST"])
def sign_in ():
    if 'uname' in session:
        return redirect(url_for('index'))
    
    else:
        username = request.form.get('username')
        email = request.args.get('email')
        password = request.form.get('password')

        return register_class.login(username,password)
        
@app.route('/sign up')
def sign_up():
    username = request.args.get('username')
    email = request.args.get('email')
    password = request.args.get('password')
    confirmPassword = request.args.get('confirmPassword') 
    if username and email:
        session.permanent=True
        session['profileName'] = username  
        session['profilemail'] = email 
        
     
    return register_class.signup(username,email,password,confirmPassword)


@app.route('/profile')
def profile():
    if "uname" in session:
        username = session.get('profileName')
        email = session.get('profilemail')
        return render_template('profile.html',Username=username,Email=email)
    
    else:
        return render_template('sign-in.html')
    

@app.route('/')
def index():
    if "uname" in session:
        return render_template('home_page.html', )
    
    else:
        return render_template('sign-in.html')



@app.route('/forget-pass', methods=["GET","POST"])
def forget():
    username = request.args.get('username')
    email = request.args.get('email')
    new_password = request.args.get('password')
    return register_class.forget(username,email,new_password)




    
@app.route('/logout')
def logout():

        session.pop('uname')
        session.pop('pass')
        return render_template('sign-in.html')



if __name__=='__main__':
    app.run(debug=True)
    