from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuração do banco de dados
DATABASE = 'database.db'

# Função para criar a tabela de dados
def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

create_table()

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para lidar com o envio do formulário
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if name and email:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO users (name, email) VALUES (?, ?)''', (name, email))
            conn.commit()
            conn.close()
            return redirect(url_for('success'))
    return redirect(url_for('index'))

# Rota para a página de sucesso
@app.route('/success')
def success():
    return 'Formulário enviado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
