from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app, send_file


atestados_alunos = Blueprint('atestados_alunos', __name__)


@atestados_alunos.route('/atestados_alunos')
def index():
    return render_template('atestados_alunos.html')