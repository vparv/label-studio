from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
#from label_studio import db


db = SQLAlchemy()
class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    num_tasks = db.Column(db.Integer)

# class TaskInfo(db.Model):
# 	__tablename__ = "user_tasks"
# 	id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
