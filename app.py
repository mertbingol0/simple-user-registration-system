from flask import Flask, render_template, request
from users_db import create_db

app = Flask(__name__)

#Endpoint
@app.route('/register', methods = ['POST', 'GET'])
def register():
   
    if request.method == 'POST': 
        #Here, it sends the data it captures with get to the create_db function.
        create_db(request.form.get('username'), request.form.get('password')) 
        #Run html file with render_template.
        return render_template('register.html')
    else:
        return render_template('Server Side Error')

if __name__ == '__main__':
    app.run(debug=True)