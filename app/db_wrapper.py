from db_create import *
class DataWrapper():
    def get_blogs_all(self):
        blogs = Blog.query.all()
        return blogs
        
    def get_projects_all(self):
        projects = Project.query.all()
        return projects

    def get_project_by_id(self, proj_id):
        return Project.query.get(proj_id)

    def get_blog_by_id(self, blog_id):
        return Blog.query.get(blog_id)
