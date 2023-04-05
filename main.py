from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app_context = app.app_context()

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/entrar', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['user', 'password'] = username, password
        return redirect(url_for("painel", username=username, password=password))

@app.route('/painel')
def dashboard(username, password):
    return render_template("dashboard.html")


@app.route('/artigos')
def articles():
    return render_template("articles.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
