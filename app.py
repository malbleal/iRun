from flask import Flask, render_template, session, redirect, url_for
from register import register
from login import login

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Importa as rotas do registro e login
app.register_blueprint(register)
app.register_blueprint(login)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu.html')
def menu():
    if 'username' in session:
        print(session)
        full_name = session['username'].split()  # Divide o nome completo em partes
        first_name = full_name[0]  # Obtém o primeiro nome
        last_name = full_name[-1]  # Obtém o último nome
        tipo = session['tipo']

        return render_template('menu.html', first_name=first_name, last_name=last_name, tipo=tipo)

    # if session.get('tipo') == 'administrador':
    #    return render_template('menu.html', username=session['username'])
    #
    # else:
    #    return render_template('menu.html', username=session['username'])
    #
    # return redirect(url_for('login.login_user'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('tipo', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
