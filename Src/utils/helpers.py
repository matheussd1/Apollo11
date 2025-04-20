from flask import current_app
import os, json

USUARIOS_JSON = 'data/usuarios.json'
EQUIPES_JSON = 'data/equipes.json'


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


# EQUIPES ÁGEIS
def carregar_equipes():
    if not os.path.exists(USUARIOS_JSON):
        return []

    with open(EQUIPES_JSON, 'r', encoding='utf-8') as file:
        return json.load(file)

def adicionar_membro(nome_equipe, membro, função):
    equipes = carregar_equipes()
    
    for i, equipe in enumerate(equipes):
        if equipe['nome'] == nome_equipe:
            equipe['num_membros'] += 1
            # equipe['membros']['membro_0'+str(equipe['num_membros'])] = {'nome': '',
            #                                                             'função': '',
            #                                                             'notas': {}}
            equipe['membros']['membro_0'+str(equipe['num_membros'])].update({'nome': membro,
                                                                            'função': função})

def salvar_equipe(equipe):
    if not os.path.exists(EQUIPES_JSON):
        return []

    with open(EQUIPES_JSON, 'w', encoding='utf-8') as file:
        json.dump(equipe, file, indent=4, ensure_ascii=False)
