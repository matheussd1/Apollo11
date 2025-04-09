from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login_aluno.html')


@auth.route('/login_professor')
def login_professor():
    return render_template('login_professor.html')


@auth.route('/cadastro_aluno')
def cadastro_aluno():
    return render_template('cadastro_aluno.html')