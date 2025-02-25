from flask import Flask, request, redirect, url_for
import urllib.parse

app = Flask(__name__)

# A list of valid URLs to which redirection is allowed
VALID_REDIRECTS = [
    '/dashboard',
    '/profile'
]

def is_valid_redirect(url):
    # Parse the URL and check if it's a relative path in the list of valid redirects
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.path in VALID_REDIRECTS

@app.route('/')
def index():
    return 'Welcome to the home page!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assume user login is successful
        next_url = request.args.get('next')
        if next_url and is_valid_redirect(next_url):
            return redirect(next_url)
        return redirect(url_for('dashboard'))
    return 'Login Page'

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'

@app.route('/profile')
def profile():
    return 'Welcome to the profile page!'

if __name__ == "__main__":
    app.run(debug=True)