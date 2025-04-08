from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login_aluno')
def login_aluno():
    return render_template('login_aluno.html')


@app.route('/login_professor')
def login_professor():
    return render_template('login_professor.html')


@app.route('/cadastro_aluno')
def cadastro_aluno():
    return render_template('cadastro_aluno.html')


@app.route('/atestados_alunos')
def atestados_alunos():
    return render_template('atestados_alunos.html')


@app.route('/atestados_professor')
def atestados_professor():
    return render_template('atestados_professor.html')