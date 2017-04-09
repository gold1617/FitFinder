from flask import Flask, render_template,request,g,session,flash,redirect,url_for,abort,jsonify
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
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    email = Column(String(200))
    bio = Column(String(250))
    age = Column(Integer)
    height = Column(Integer)

    def __init__(self, name,email,bio,age,height):

        self.name = name
        self.bio = bio
        self.age = age
        self.email = email
        self.height = height
        
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route('/')
def start():
    return render_template('start.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/myprofile')
def myprofile():
    me  = User.query.filter_by(id=1).first()
    return jsonify(me.as_dict())

@app.route('/profile',methods=['POST'])
def edit_profile():
    user = User.query.filter_by(id=1).first();
    user.name = request.form['name'];
    user.age = request.form['age'];
    user.height = request.form['height'];
    user.bio = request.form['bio'];
    db_session.commit();
    return index()

@app.route('/logout')
def logout():
    return start()


if __name__ == '__main__':
    init_db();
    app.run()
