from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app
from utils.helpers import *

scrum_master = Blueprint('scrum_master', __name__)


def render_with_info():
    return render_template('scrum_master.html', logado = current_app.config['SCRUM_LOGADO'], 
                        dados_usuario = usuario_atual(),
                        alunos = carregar_alunos()
                        )

@scrum_master.route('/scrum_master', methods=['GET', 'POST'])
def index():
    return render_with_info()

@scrum_master.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        senha = request.form['senha']

        alunos = carregar_alunos()


        if senha == current_app.config['SENHA_SCRUM']:
            current_app.config['SCRUM_LOGADO'] = True
            mudar_valor(current_app.config['RA_ATUAL'], 'função', 'Scrum Master')
    
    return render_with_info()

@scrum_master.route('/definir_nome', methods=['GET', 'POST'])
def definir_nome():

    if request.method == 'POST':

        nome_equipe = request.form['nome-equipe']

        equipes = carregar_equipes()

        for equipe in equipes:
            if equipe == nome_equipe:
                return render_with_info()

        mudar_valor(current_app.config['RA_ATUAL'], 'equipe', nome_equipe)

        equipes[nome_equipe] = {'num_membros': 1, 'membros': {}}
        salvar_equipe(equipes)

    return render_with_info()

@scrum_master.route('/cadastro')
def cadastro():
    return render_with_info()