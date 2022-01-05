from flask import Blueprint, render_template

bp_dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp_dashboard.route('/')
def dashboard():
    return render_template('dashboard.html')

@bp_dashboard.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')


