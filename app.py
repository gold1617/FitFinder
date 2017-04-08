
from flask import Flask, render_template,request,g,session,flash,redirect,url_for,abort
from flask_openid import OpenID

from openid.extensions import pape

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config.update(
        DATABASE_URI  = 'sqlite:///database.db',
        SECRET_KEY = 'dev key',
        DEBUG = 'true'
)

oid = OpenID(app, safe_roots=[], extension_responses=[pape.Response])

# setup sqlalchemy
engine = create_engine(app.config['DATABASE_URI'])
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=True,bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = 'wines'
    id = Column(Integer, primary_key=True)
    kind = Column(String(30))
    country = Column(String(30))
    openid = Column(String(200))

    def __init__(self, kind, country, openid):

        self.kind = kind
        self.country = country
        self.openid = openid


@app.route('/')
def index():
    print(User.query.filter_by(id="*"))
    return render_template('index.html') 


if __name__ == '__main__':
    init_db();
    app.run()
