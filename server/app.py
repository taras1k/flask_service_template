import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_CONFIG_CLASS'))

db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    manager.run()
