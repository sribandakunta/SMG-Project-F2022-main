import sqlite3
import click
from flask import current_app, g 
from flask.cli import with_appcontext

def connect_db():
    r = sqlite3.connect(current_app.config['DATABASE'])
    r.row_factory = sqlite3.Row
    return r

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db
    return g.sqlite_db

def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
    
def init_db():
    db = get_db()
    with current_app.open_resource('model.sql') as tables:
        db.executescript(tables.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Created the Database')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)