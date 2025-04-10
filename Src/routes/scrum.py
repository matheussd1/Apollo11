from flask import Blueprint, Flask, redirect, request, render_template, url_for, current_app


scrum = Blueprint('scrum', __name__)


@scrum.route('/scrum')
def index():
    return render_template('scrum.html')