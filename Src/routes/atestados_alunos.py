from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app, send_file
from utils.helpers import *


atestados_alunos = Blueprint('atestados_alunos', __name__)


@atestados_alunos.route('/atestados_alunos', methods=['POST','GET'])
def index():
    return render_template('atestados_alunos.html')

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
    
    

    return render_template('atestados_alunos.html')

# @atestados_alunos.route('/download_atestados', methods =['POST', 'GET'])
# def download():
#     return render_template('atestados_alunos.html')

@atestados_alunos.route('/delet_atestados', methods =['POST', 'GET'])
def delet():
    return render_template('atestados_alunos.html')

# @atestados_alunos.route('/abrir_atestados', methods =['POST', 'GET'])
# def abrir():
#     return render_template('atestados_alunos.html')