from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app
import os, json

auth = Blueprint('auth', __name__)

USUARIOS_JSON = 'usuarios.json'

def salvar_aluno(alunos):

    if not os.path.exists(USUARIOS_JSON):
        return []

    with open(USUARIOS_JSON, 'w', encoding='utf-8') as file:
        json.dump(alunos, file, indent=4, ensure_ascii=False)


def carregar_alunos():
    if not os.path.exists(USUARIOS_JSON):
        return []
    

    with open(USUARIOS_JSON, 'r', encoding='utf-8') as file:
        return json.load(file)

@auth.route('/login')
def login():
    return render_template('login_aluno.html')


@auth.route('/login_professor')
def login_professor():
    return render_template('login_professor.html')


@auth.route('/cadastro_aluno', methods=['POST', 'GET'])
def cadastro_aluno():

    if request.method == 'POST':
        dados = {'nome': request.form['nome'],
                 'ra': request.form['ra'],
                 'senha': request.form['senha']}


        alunos = carregar_alunos()

        for aluno in alunos:
            if aluno['ra'] == dados['ra']:
                return redirect(url_for('auth.cadastro_aluno'))
        
        alunos.append(dados)
        salvar_aluno(alunos)

    return render_template('cadastro_aluno.html')