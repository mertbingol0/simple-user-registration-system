from flask import Flask, render_template, request
from users_db import create_db, password_hashing

app = Flask(__name__)

#Endpoint
@app.route('/register', methods = ['POST', 'GET'])
def register():
   
    if request.method == 'POST':
      
        #Here, it sends the data it captures with get to the create_db function.
        username = request.form.get('username')
        password = request.form.get('password')
        hashed_password = password_hashing(password)
        create_db(username, hashed_password)
      
        return "User Created"
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
