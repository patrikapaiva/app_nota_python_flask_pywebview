import sqlite3
from flask import Flask,render_template,request,url_for,flash,redirect
from werkzeug.exceptions import abort
import os
import sys
import init_db
import webview

database = os.path.dirname(sys.executable) 

def get_db_connection():             
    print('conectar: ' +database + '/database.db')
    conn = sqlite3.connect(database + '/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('Select * from posts where id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('select * from posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Informe o Titulo!')
        else:
            conn = get_db_connection()
            conn.execute('insert into posts (title, content) values(?,?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash('Informe o Titulo!')
        else:
            conn = get_db_connection()
            conn.execute('update posts set title = ? , content = ? '
                         ' where id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('Delete from posts where id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" nota foi delata com sucesso!'.format(post['title']))
    return redirect(url_for('index'))

if __name__ == '__main__':
    if os.path.exists(database + '/database.db') == False:
        print('criar: ' +database + '/database.db')
        init_db.criarDB(database + '/database.db')
    #app.run(port=8080, debug=True)
    webview.create_window('Notas', app)
    webview.start(debug=True)

