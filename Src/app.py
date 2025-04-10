from flask import Flask, render_template
from routes.atestados_professor import professor
from routes.atestados_alunos import atestados_alunos
from routes.auth import auth
from routes.scrum import scrum
from routes.scrum_master import scrum_master


app = Flask(__name__)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(atestados_alunos, url_prefix='/atestados_alunos')
app.register_blueprint(professor, url_prefix='/professor')
app.register_blueprint(scrum, url_prefix="/scrum")
app.register_blueprint(scrum_master, url_prefix="/scrum_master")


app.config['RA_ATUAL'] = '123'


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')