from flask import *

app = Flask(__name__)

@app.route('/')  
def home ():  
    return redirect(url_for("appform"))
 
@app.route('/appform')  
def appform():  
    return render_template("index.html");  
 
@app.route('/login')  
def login():  
    return redirect(url_for('success'))
 
@app.route('/success')  
def success():  
    return 'logged in successfully'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
