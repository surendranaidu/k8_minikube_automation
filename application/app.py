from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Basic in-memory login storage for demonstration
users = {'admin': 'password123'}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if users.get(username) == password:
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials, please try again.", 401

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        # Placeholder for ChatGPT search functionality
        result = f"Search results for: {query}"  # Example, integrate ChatGPT API here
        return render_template('search_result.html', result=result)

    return render_template('search.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
