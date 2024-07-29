import csv
import bcrypt
from flask import Blueprint, render_template, request, redirect, url_for, session

login = Blueprint('login', __name__)

@login.route('/login.html', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        login_input = request.form['login']
        senha_input = request.form['senha']

        with open('users.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            linhas = list(reader)  # Converte o reader em uma lista para edição
            for indice, row in enumerate(linhas):
                if row['login'] == login_input:
                    if row['primeiro_acesso'] == 'True':  # Corrigido para comparar como string
                        session['username'] = row['nome']
                        session['tipo'] = row['tipo']
                        linhas[indice]['primeiro_acesso'] = 'False'  # Atualiza para string 'False'

                        with open('users.csv', 'w', newline='') as csvfile:
                            fieldnames = ['nome', 'login', 'senha', 'idade', 'data_nascimento', 'cpf', 'sexo', 'telefone', 'email', 'cep', 'tipo', 'primeiro_acesso']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerows(linhas)

                        return redirect(url_for('menu'))

                    if bcrypt.checkpw(senha_input.encode('utf-8'), row['senha'].encode('utf-8')):
                        session['username'] = row['nome']
                        session['tipo'] = row['tipo']
                        return redirect(url_for('menu'))
            
        error_message = "Credenciais inválidas. Por favor, tente novamente."
        return render_template('login.html', error_message=error_message)

    return render_template('login.html')
