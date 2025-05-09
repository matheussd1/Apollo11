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
                        pegar_valor = pegar_valor,
                        pegar_notas = pegar_notas)

@scrum.route('/scrum')
def index():
    if not current_app.config['RA_ATUAL']:
        return redirect(url_for('auth.login'))

    return render_with_info()


@scrum.route('/avaliar_membro/<string:ra>')
def avaliar_membro(ra):
    return render_template('avaliação.html', membro=pegar_membro(ra))


@scrum.route('/finalizar/<string:ra>', methods=['GET', 'POST'])
def finalizar(ra):
    if request.method == 'POST':
        dados = request.form.to_dict()
        
        membros = carregar_alunos()
        avaliado = pegar_membro(ra)

        for nota in avaliado.get('notas'):
            for nota_avaliador in dados:
                if nota.lower() == nota_avaliador:
                    for i, membro in enumerate(membros):
                        if membro.get('ra') == ra:
                            membros[i]['notas'][nota].append([current_app.config['RA_ATUAL'], dados.get(nota_avaliador)])
                            break
        salvar_aluno(membros)

    return redirect(url_for('scrum.index'))

@scrum.route('/notas_usuario')
def notas_usuario():
    return render_template('notas_usuario.html', dados_usuario = usuario_atual())