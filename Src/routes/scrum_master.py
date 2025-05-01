from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app
from utils.helpers import *

scrum_master = Blueprint('scrum_master', __name__)


def render_with_info():

    if equipe_atual():
        equipe = carregar_equipes()[equipe_atual()]
    else:
        equipe = {}

    return render_template('scrum_master.html', logado = current_app.config['SCRUM_LOGADO'], 
                        dados_usuario = usuario_atual(),
                        alunos = carregar_alunos(),
                        equipe = equipe,
                        pegar_valor = pegar_valor)

@scrum_master.route('/scrum_master', methods=['GET', 'POST'])
def index():

    if not current_app.config['RA_ATUAL']:
        return redirect(url_for('auth.login'))

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

        equipes[nome_equipe] = {'num_membros': 1, "avaliação": False, 'membros': [usuario_atual()['ra']]}
        salvar_equipe(equipes)

    return redirect(url_for('scrum_master.index'))


@scrum_master.route('/adicionar_membro', methods=['GET', 'POST'])
def adicionar_membro():

    if request.method == 'POST':
        mudar_valor(request.form['ra-aluno'], 'equipe', usuario_atual()['equipe'])
        mudar_valor(request.form['ra-aluno'], 'função', request.form['função'])

        equipes = carregar_equipes()
        equipes[equipe_atual()]['membros'].append(request.form['ra-aluno'])
        equipes[equipe_atual()]['num_membros'] = len(equipes[equipe_atual()]['membros'])
        salvar_equipe(equipes)

        return redirect(url_for('scrum_master.index'))


@scrum_master.route('/abrir_avaliação')
def abrir_avaliação():
    
    equipe_usuario = equipe_atual()
    equipes = carregar_equipes()

    for equipe in equipes:
        if equipe_usuario == equipe:
            equipes[equipe]['avaliação'] = True
    
    salvar_equipe(equipes)

    return redirect(url_for('scrum_master.index'))



# DEBUG

@scrum_master.route('/debug')
def debug():
    for aluno in carregar_alunos():
        mudar_valor(aluno['ra'], 'função', 'DevTeam')
        mudar_valor(aluno['ra'], 'equipe', 'Nenhuma')
    salvar_equipe({})
    return redirect(url_for('auth.login'))