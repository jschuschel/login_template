__author__ = 'slipvyne'
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'development key'

MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'contact@example.com'
MAIL_PASSWORD = 'your-password'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
