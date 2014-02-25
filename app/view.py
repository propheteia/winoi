#coding=UTF-8
from . import app
from flask import render_template
from db_wrapper import DataWrapper
from html2text import  html2text
dw = DataWrapper()

app.jinja_env.filters['html2text'] = html2text

def date_format(date):
    return u"%d年%d月%d日"%(date.year, date.month, date.day)
app.jinja_env.filters['dateformat'] = date_format

@app.route('/')
def index():
    blogs = dw.get_blogs_all() 
    return render_template('index.html',
            blogs = blogs,
            )

@app.route('/project')
def project():
    projects = dw.get_projects_all()
    return render_template('project.html',
                projects = projects,
                )
@app.route('/project_details/<project_id>')
def project_details(project_id):
    project = dw.get_project_by_id(project_id)
    return render_template('project-single.html',
                project = project,
                )
@app.route('/blog/<blog_id>')
def blog(blog_id):
    blog = dw.get_blog_by_id(blog_id) 
    return render_template('blog.html',
                blog = blog,
                )

