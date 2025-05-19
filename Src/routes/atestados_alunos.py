from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app, send_file
from utils.helpers import *
from uuid import uuid4
from io import BytesIO
from datetime import datetime, timezone


atestados_alunos = Blueprint('atestados_alunos', __name__)

def formatar_data(data):
    return "-".join(data.split('-')[::-1])

@atestados_alunos.route('/atestados_alunos', methods=['POST','GET'])
def index():

    if not current_app.config['RA_ATUAL']:
        return redirect(url_for('auth.login'))

    atestados = []

    for atestado in usuario_atual()['atestados']:
        atestados.append(usuario_atual()['atestados'][atestado])

    return render_template('atestados_alunos.html', atestados = atestados, usuario = usuario_atual())

@atestados_alunos.route('/enviar_atestados', methods =['POST', 'GET'])
def enviar():
    usuario = usuario_atual()
    if not current_app.config['RA_ATUAL']:
        return redirect(url_for('auth.login'))
    
    if request.method == 'POST':
        pdf = request.files['pdf']
        c_afastamento = request.form['c_afastamento']
        f_afastamento = request.form['f_afastamento']
    
    os.makedirs(f"uploads/{current_app.config['RA_ATUAL']}", exist_ok=True)

    pdf_path = f'uploads/{current_app.config['RA_ATUAL']}/{pdf.filename}'
    caminho_pdf = os.path.join(pdf_path)

    pdf.save(caminho_pdf)
    cadastros = carregar_alunos()

    if 'num_atestados' in usuario.keys():
        usuario['num_atestados'] += 1
    else:
        usuario['num_atestados'] = 1

    for i, cadastro in enumerate(cadastros):
        if cadastro['ra'] == usuario['ra']: # ou current_app.config['RA_ATUAL']
           
            if 'num_atestados' in cadastros[i]:
                cadastros[i]['num_atestados'] += 1
            else:
                cadastros[i]['num_atestados'] = 1

            data_criado = str(datetime.now(timezone.utc)).split(' ')[0]

            cadastros[i]['atestados'][f'atestado_{usuario['num_atestados']}'] = {'pdf': pdf_path,
                                                                                'id': str(uuid4()),
                                                                                'data_criado': formatar_data(data_criado),
                                                                                'status': 'Não Verificado',
                                                                                'c_afastamento': formatar_data(c_afastamento),
                                                                                'f_afastamento': formatar_data(f_afastamento)}
    
    salvar_aluno(cadastros)
    return redirect(url_for('atestados_alunos.index'))

@atestados_alunos.route('/download_atestados/<string:id>', methods =['POST', 'GET'])
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

@atestados_alunos.route('/delete/<string:id>')
def delete(id):
    usuario = usuario_atual()

    try:
        os.remove(usuario['atestados'][pegar_atestado(id)]['pdf'])
    except:
        pass

    cadastros = carregar_alunos()
    for cadastro in cadastros:
        if cadastro['ra'] == usuario['ra']:
              cadastro['atestados'].pop(pegar_atestado(id))
    salvar_aluno(cadastros)

    return redirect(url_for('atestados_alunos.index'))

@atestados_alunos.route('/abrir_atestados/<path:pdf>')
def abrir_atestados(pdf):
    return send_file(pdf, mimetype='application/pdf', as_attachment=False)