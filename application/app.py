from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import urllib.parse  # Use this if you need URL encoding functionality

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jira.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    tasks = db.relationship('Task', backref='project', lazy=True)

# Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    status = db.Column(db.String(50), nullable=False, default='To Do')
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

# Create tables
db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return redirect(url_for('dashboard'))
        flash('Invalid login credentials.')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username already taken.')
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    projects = Project.query.all()
    return render_template('dashboard.html', projects=projects)

@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_project = Project(name=name, description=description)
        db.session.add(new_project)
        db.session.commit()
        flash('Project created successfully!')
        return redirect(url_for('projects'))
    return render_template('create_project.html')

@app.route('/tasks/<int:project_id>')
def tasks(project_id):
    project = Project.query.get_or_404(project_id)
    tasks = Task.query.filter_by(project_id=project.id).all()
    return render_template('tasks.html', project=project, tasks=tasks)

@app.route('/create_task/<int:project_id>', methods=['GET', 'POST'])
def create_task(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']
        assigned_to = request.form.get('assigned_to')
        task = Task(title=title, description=description, status=status, project_id=project.id, assigned_to=assigned_to)
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!')
        return redirect(url_for('tasks', project_id=project.id))
    users = User.query.all()
    return render_template('create_task.html', project=project, users=users)

@app.route('/update_task/<int:task_id>', methods=['GET', 'POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.status = request.form['status']
        task.assigned_to = request.form.get('assigned_to')
        db.session.commit()
        flash('Task updated successfully!')
        return redirect(url_for('tasks', project_id=task.project_id))
    users = User.query.all()
    return render_template('update_task.html', task=task, users=users)

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!')
    return redirect(url_for('tasks', project_id=task.project_id))

if __name__ == "__main__":
    app.run(debug=True)
