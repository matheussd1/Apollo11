from flask import Blueprint, Flask, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

senha_prof = '123'

@auth.route('/auth/professor', methods=['GET', 'POST'])
def login_professor():
    if request.method == 'POST':
        senha = request.form.get('senha')

        if senha == senha_prof:
            return redirect(url_for('atestados_professor'))
        
    return render_template('login_professor.html')