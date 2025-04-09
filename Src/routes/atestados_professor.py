from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app


professor = Blueprint('professor', __name__)


@professor.route('/atestados_professor')
def index():
    return render_template('atestados_professor.html')