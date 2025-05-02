from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app
from utils.helpers import *

scrum = Blueprint('scrum', __name__)

def render_with_info():
    if equipe_atual():
        equipe = carregar_equipes()[equipe_atual()]
    else:
        equipe = {}

    return render_template('scrum.html', logado = current_app.config['SCRUM_LOGADO'], 
                        dados_usuario = usuario_atual(),
                        alunos = carregar_alunos(),
                        equipe = equipe,
                        pegar_valor = pegar_valor)

@scrum.route('/scrum')
def index():
    if not current_app.config['RA_ATUAL']:
        return redirect(url_for('auth.login'))

    return render_with_info()


@scrum.route('/avaliar_membro/<string:ra>')
def avaliar_membro(ra):
    return render_template('avaliação.html', membro=pegar_membro(ra))