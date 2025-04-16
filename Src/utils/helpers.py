from flask import current_app
import os, json

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

def usuario_atual():
    alunos = carregar_alunos
    for aluno in alunos:
        if aluno['RA'] == current_app.config['RA_ATUAL']:
            return aluno