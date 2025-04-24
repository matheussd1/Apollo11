from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app
import os, json
from utils.helpers import salvar_aluno, carregar_alunos

auth = Blueprint('auth', __name__)

#request.form[]

@auth.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        ra = request.form['RA']
        password = request.form['password']
    
        usuarios = carregar_alunos()

        for usuario in usuarios:
            if usuario['RA'] == ra and usuario['password'] == password:
                current_app.config['RA_ATUAL'] = usuario['RA']
                return redirect(url_for('atestados_aluno.index'))
    
    return render_template('login_aluno.html')


@auth.route('/login_professor')
def login_professor():
    return render_template('login_professor.html')


@auth.route('/cadastro_aluno', methods=['POST', 'GET'])
def cadastro_aluno():

    if request.method == 'POST':
        dados = {'nome': request.form['nome'],
                 'ra': request.form['ra'],
                 'senha': request.form['senha'],
                 'num_atestados': 0,
                 'atestados': {},
                 'equipe': 'Nenhuma',
                 'função': 'DevTeam',
                 "notas": {"Proatividade": [], "Autonomia": [], "Colaboração": [], "Entrega de Resultados": []}}


        alunos = carregar_alunos()

        for aluno in alunos:
            if aluno['ra'] == dados['ra']:
                return redirect(url_for('auth.cadastro_aluno'))
        
        alunos.append(dados)
        salvar_aluno(alunos)

    return render_template('cadastro_aluno.html')