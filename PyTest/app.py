from flask import *

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/registrazione')
def registrazione():
    return render_template('registrazione.html')

@app.route('/registrazione', methods=['POST'])
def registrazione_post():
    nome = request.form['nome']
    cognome = request.form['cognome']
    email = request.form['email']
    
    return redirect(url_for('login'))

if (__name__ == '__main__'):
    # app.run(port=80)
    app.run(host='0.0.0.0', port=443, ssl_context=('SSL/certificate.crt', 'SSL/private.key'))