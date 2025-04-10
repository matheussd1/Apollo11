from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app


scrum_master = Blueprint('scrum_master', __name__)


@scrum_master.route('/scrum_master')
def index():
    return render_template('scrum_master.html')

@scrum_master.route('/cadastro')
def cadastro():
    return render_template('scrum_master.html')