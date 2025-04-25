from flask import Flask, render_template, url_for, redirect
from routes.atestados_professor import professor
from routes.atestados_alunos import atestados_alunos
from routes.auth import auth
from routes.scrum import scrum
from routes.scrum_master import scrum_master
import json, os


app = Flask(__name__)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(atestados_alunos, url_prefix='/atestados_alunos')
app.register_blueprint(professor, url_prefix='/professor')
app.register_blueprint(scrum, url_prefix="/scrum")
app.register_blueprint(scrum_master, url_prefix="/scrum_master")


app.config['RA_ATUAL'] = ''
app.config['SENHA_PROF'] = '123'
app.config['SENHA_SCRUM'] = '123'

app.config['SCRUM_LOGADO'] = False


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return redirect(url_for('auth.login'))