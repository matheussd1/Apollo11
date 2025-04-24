from flask import current_app
import os, json

USUARIOS_JSON = 'data/usuarios.json'
EQUIPES_JSON = 'data/equipes.json'


def pegar_atestado(id):
    usuario = usuario_atual()
    for atestado in usuario['atestados']:
        if usuario['atestados'][atestado]['id'] == id:
            return atestado


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

def usuario_atual():
    alunos = carregar_alunos()
    for aluno in alunos:
        if aluno['ra'] == current_app.config['RA_ATUAL']:
            return aluno


def mudar_valor(ra, valor, novo_valor):
    alunos = carregar_alunos()

    for i, aluno in enumerate(alunos):
        if aluno['ra'] == ra:
            alunos[i][valor] = novo_valor
        
    salvar_aluno(alunos)

def pegar_valor(ra, valor):
    alunos = carregar_alunos()
    for i, aluno in enumerate(alunos):
        if aluno['ra'] == ra:
            return aluno[valor]
    return []

# EQUIPES ÁGEIS
def carregar_equipes():
    if not os.path.exists(USUARIOS_JSON):
        return []

    with open(EQUIPES_JSON, 'r', encoding='utf-8') as file:
        return json.load(file)

def adicionar_membro(nome_equipe, membro, função):
    equipes = carregar_equipes()
    
    for aluno in carregar_alunos():
        if aluno.ra == membro:
            nome = aluno.nome

    for equipe in equipes:
        if equipe == nome_equipe:
            equipes[equipe]['membros'][membro] = {}

def salvar_equipe(equipe):
    if not os.path.exists(EQUIPES_JSON):
        return []

    with open(EQUIPES_JSON, 'w', encoding='utf-8') as file:
        json.dump(equipe, file, indent=4, ensure_ascii=False)

def equipe_atual():
    for equipe in carregar_equipes():
        if equipe == usuario_atual()['equipe']:
            return equipe
    return []

