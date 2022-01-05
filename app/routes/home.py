from flask import Blueprint, render_template

bp_home = Blueprint('home', __name__, url_prefix='/')

@bp_home.route('/')
def index():
    return render_template('homepage.html')

@bp_home.route('/login')
def login():
    return render_template('login.html')

@bp_home.route('/post/<id>')
def single(id):
    return render_template('single-post.html')