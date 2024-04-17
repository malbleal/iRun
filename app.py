from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        login = request.form['login']
        senha = request.form['senha']
        idade = request.form['idade']
        data_nascimento = request.form['data_nascimento']
        cpf = request.form['cpf']
        sexo = request.form['sexo']
        telefone = request.form['telefone']
        email = request.form['email']
        cep = request.form['cep']
        
        with open('users.csv', 'a', newline='') as csvfile:
            fieldnames = ['nome', 'login', 'senha', 'idade', 'data_nascimento', 'cpf', 'sexo', 'telefone', 'email', 'cep']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Verifica se o arquivo CSV já existe e escreve o cabeçalho caso não exista
            if csvfile.tell() == 0:
                writer.writeheader()
                
            writer.writerow({'nome': nome, 'login': login, 'senha': senha, 'idade': idade, 'data_nascimento': data_nascimento,
                              'cpf': cpf, 'sexo': sexo, 'telefone': telefone, 'email': email, 'cep': cep})
        
        return redirect(url_for('menu'))
    return render_template('register.html')

@app.route('/menu.html')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)
