from flask import Flask, render_template,request,session,redirect,url_for
import json
import hashlib


class register_class :

    @staticmethod
    def login(username,password):
        try:
            with open('accounts.json', 'r') as f:   #read the json file to check for existing accounts
                data_converted = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):  #if account doesn't exist, redirect to sign up 
            return 'make account first'
        
        data_string = open('accounts.json').read()   
        data_converted=json.loads(data_string)   #getting data from the json file as read only

        if password != None:   #preventing the website from sending empty password once opened 
            hashed_pass=hashlib.sha256(password.encode()).hexdigest()   #hashing the data for user's privacy
        else:
            return render_template('sign-in.html')   #if the website sent empty password reopen the sign-in page
        
        
        if username in data_converted :   #login using emal or username that must be already existing in the json file
            if data_converted[username] == hashed_pass:     #checking that the password given by user is for the correct email/username
                    session.permanent=True                           #making permanent session
                    session['uname'] = request.form['username']      #storing the username in the session  
                    session['pass'] = request.form['password']       #storing the password in the session 
                    return render_template('home_page.html')   #the user now will remain logged in as long as the session remains
            else:
                    return "wrong_password"
        else:
            return "username doesnt exist, make an account"

        
    @staticmethod
    def signup(username,email,password,confirmPassword):
        try:
            with open('accounts.json', 'r') as f:             #checking if the accounts file exists
                 data_converted = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):     
            data_converted = {}                               #if the file doesnt exist then make a dict. , it will be converted into json later on

        if username in data_converted :   #checking that the user has a unique username
            return "<h1>username already taken :O</h1>"
        elif password != confirmPassword:
            return 'Invalid password confirmation. Please try again !'
        elif email in data_converted :   #checking that the username has a unique email
            return "<h1>email already taken :O</h1>"
        
        elif username and password != "":    #preventing the website from sending empty things once opened 
           
            data_converted[username]=hashlib.sha256(password.encode()).hexdigest()   #assigning each email/username to its hashed password 
            data_converted[email]=hashlib.sha256(password.encode()).hexdigest()
            
            with open('accounts.json', 'w') as f:       
                json.dump(data_converted, f, indent = 2)   #saving the user's data in the json file

            return render_template('sign-in.html')
        return render_template('sign-up.html')
           

    @staticmethod
    def forget(username,email,new_password,password_verify):
        try:
            with open('accounts.json', 'r') as f:   
                data_converted = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data_converted = {}
        
        data_string = open('accounts.json').read()   
        data_converted=json.loads(data_string)   #getting data from the json file as read only

       
        if new_password != password_verify:
            return 'Invalid password confirmation. Please try again !'
        elif username and email != "":
            if username in data_converted and email in data_converted:
                if new_password != None:
                    hashed_pass=hashlib.sha256(new_password.encode()).hexdigest() 
                    data_converted[username] = hashlib.sha256(new_password.encode()).hexdigest()
                    data_converted[email] = hashlib.sha256(new_password.encode()).hexdigest()
                    with open('accounts.json', 'w') as f:       
                        json.dump(data_converted, f, indent = 2) 
                    return render_template('sign-in.html')
            else:
                return render_template('sign-up.html')
           
        return render_template('forget-pass.html')
    

                

