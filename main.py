from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app_context = app.app_context()
app.secret_key = 'relou'

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/entrar', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        for key in request.form.keys():
            session[key] = request.form[key]
        return redirect(url_for("dashboard"))

@app.route('/painel')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template("dashboard.html", username=username)

@app.route('/artigos')
def articles():
    return render_template("articles.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
