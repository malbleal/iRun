from flask import Blueprint, render_template, request, redirect, url_for
import csv
import bcrypt
from login import login


register = Blueprint('register', __name__)

@register.route('/register.html', methods=['GET', 'POST'])
def register_user():
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
        
        # Define o tipo de usuário como 'normal_user'
        tipo = 'normal_user'
        primeiro_acesso = True

        # Hash da senha usando bcrypt
        hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

        with open('users.csv', 'a', newline='') as csvfile:
            fieldnames = ['nome', 'login', 'senha', 'idade', 'data_nascimento', 'cpf', 'sexo', 'telefone', 'email', 'cep', 'tipo', 'primeiro_acesso']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Verifica se o arquivo CSV já existe e escreve o cabeçalho caso não exista
            if csvfile.tell() == 0:
                writer.writeheader()
                
            writer.writerow({'nome': nome, 'login': login, 'senha': hashed_password.decode('utf-8'), 'idade': idade, 'data_nascimento': data_nascimento,
                              'cpf': cpf, 'sexo': sexo, 'telefone': telefone, 'email': email, 'cep': cep, 'tipo': tipo, 'primeiro_acesso': primeiro_acesso})
        
        return redirect(url_for('login.login_user'))
    return render_template('register.html')
