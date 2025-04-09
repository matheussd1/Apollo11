from flask import Flask, render_template
from routes.atestados_professor import professor
from routes.atestados_alunos import atestados_alunos
from routes.auth import auth


app = Flask(__name__)

app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(atestados_alunos, url_prefix='/atestados_alunos')
app.register_blueprint(professor, url_prefix='/professor')


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')