from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from website import app

#class Note(db.Model):#this is an example data feature from the tutorial
 #   id = db.Column(db.Integer, primary_key=True)
  #  data = db.Column(db.String(100000))
  #  date = db.Column(db.DateTime(timezone=True), default=func.now())
   # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    #notes = db.relationship('Note')
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

with app.app_context():
    db.create_all()


