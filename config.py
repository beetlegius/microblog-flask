import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'd2b662394c19d7da71765c4879fa0d8456acf7ae4b4b0dfe9bac685b5306b365e974f45b4c16d78229c85b8be22fa07bba8c27e197a226f629b83e1190803c55app'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
