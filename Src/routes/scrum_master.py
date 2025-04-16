from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app
from utils.helpers import salvar_aluno, carregar_alunos, usuario_atual

scrum_master = Blueprint('scrum_master', __name__)


@scrum_master.route('/scrum_master', methods=['GET', 'POST'])
def index():
    return render_template('scrum_master.html', logado = current_app.config['SCRUM_LOGADO'])

@scrum_master.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        senha = request.form['senha']

        alunos = carregar_alunos()


        if senha == current_app.config['SENHA_SCRUM']:
            current_app.config['SCRUM_LOGADO'] = True
            for i, aluno in enumerate(alunos):
                if aluno['ra'] == current_app.config['RA_ATUAL']:
                    alunos[i]['scrum_master'] = True
        
        salvar_aluno(alunos)
    
    return render_template('scrum_master.html', logado = current_app.config['SCRUM_LOGADO'])


@scrum_master.route('/cadastro')
def cadastro():
    return render_template('scrum_master.html')