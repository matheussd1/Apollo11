from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app
from utils.helpers import *

atestados_professor = Blueprint('atestados_professor', __name__)

CADASTROS_JSON = "data/usuarios.json"

@atestados_professor.route('/index', methods=['GET', 'POST'])
def index():
    usuarios = []
    with open(CADASTROS_JSON, 'r', encoding='UTF-8') as file:
        usuarios = json.load(file)
    if request.method == 'POST':
        pesquisa = request.form['Pesquisar']
        classificar = request.form['classificar']
        
        usuarios_filtrados = [usuario for usuario in usuarios if pesquisa in usuario['ra'] or pesquisa.lower() in usuario['nome'].lower()]

        if classificar == 'alfabetica':
            usuarios_filtrados = sorted(usuarios_filtrados, key=lambda x: x['nome'].lower())


        return render_template("atestados_professor.html", usuarios=usuarios_filtrados)
    return render_template('atestados_professor.html', usuarios=usuarios)

@atestados_professor.route('/abrir_atestados/<path:pdf>')
def abrir_atestados(pdf):
    return send_file(pdf, mimetype='application/pdf', as_attachment=False)

@atestados_professor.route('/download_atestados/<string:id>', methods =['POST', 'GET'])
def download(id):
    usuario = usuario_atual()
    atestado = pegar_atestado(id=id)

    nome_arquivo = f'Atestado {usuario['atestados'][atestado]['data_criado']} {usuario['nome']}.pdf'
    caminho = usuario['atestados'][atestado]['pdf']
    with open(caminho, "rb") as file:
        pdf_bytes = BytesIO(file.read())
    return send_file(pdf_bytes,
                     mimetype= 'application/pdf',
                     as_attachment=True,
                     download_name=nome_arquivo)


@atestados_professor.route('/verificar/<string:id>/<string:ra>/<string:status>')
def verificar(id, ra, status):
    
    with open(CADASTROS_JSON, 'r', encoding='utf-8') as file:
        usuarios = json.load(file)

    usuario_atual = {}
    position = 0
    for i, usuario in enumerate(usuarios):
        if usuario['ra'] == ra:
            usuario_atual = usuario
            position = i

    atestado_atual = ""
    for atestado in usuario_atual:
        if 'atestado' in atestado:
            if usuario_atual[atestado]['id'] != id:
                continue
            atestado_atual = atestado
            break
    
    usuarios[position][atestado_atual]['status'] = status

    with open(CADASTROS_JSON, 'w', encoding='utf-8') as file:
        json.dump(usuarios, file, indent=4, ensure_ascii=False)

    return redirect(url_for('atestados_professor.index'))