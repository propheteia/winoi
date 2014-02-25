from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from . import app
from db_create import db, User, Project, Blog, Category, Tag

class MyModelView(ModelView):
    #form_overrides = dict(content=wtforms.TextAreaField)
    create_template = "edit.html"
    edit_template = "edit.html"

admin = Admin(app, url="/admin")
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Project, db.session))
admin.add_view(MyModelView(Blog, db.session))
admin.add_view(MyModelView(Category, db.session))
admin.add_view(MyModelView(Tag, db.session))
