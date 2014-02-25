from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from . import app
db = SQLAlchemy(app)
blog_tags = db.Table('tags_blog',                                                                                                            
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),                  
    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id')),          
)       
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10), unique = True)
    email = db.Column(db.String(50), unique = True)
    created_time = db.Column(db.DateTime, default = datetime.now())
    modified_time = db.Column(db.DateTime, default = datetime.now())

    def __repr__(self):
        return self.name

class Project(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True)
    intro = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',\
        backref=db.backref('projects',lazy='dynamic'), lazy='select')
    created_time = db.Column(db.DateTime, default = datetime.now())
    modified_time = db.Column(db.DateTime, default = datetime.now())

    def __repr__(self):
        return self.name


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50), unique = True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User',\
        backref=db.backref('blogs',lazy='dynamic'), lazy='select')
    proj_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship('Project',\
        backref=db.backref('blogs', lazy='dynamic'), lazy='select')
    created_time = db.Column(db.DateTime, default = datetime.now())
    modified_time = db.Column(db.DateTime, default = datetime.now())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('blogs',lazy='dynamic'), lazy='select')
    tags = db.relationship('Tag', secondary=blog_tags,\
            backref=db.backref('blogs', lazy='dynamic'))

    def __repr__(self):
        return self.title

class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True)

    def __repr__(self):
        return self.name

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True)

    def __repr__(self):
        return self.name

if __name__ == "__main__":
    db.create_all()
