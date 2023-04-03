from flask import Flask, render_template

app = Flask(__name__)
app_context = app.app_context()

@app.route('/')
def homepage():
    return render_template("homepage.html")

@app.route('/artigos')
def articles():
    return render_template("articles.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
