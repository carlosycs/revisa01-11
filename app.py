from flask import Flask, render_template, session, redirect, url_for, request
from controllers.questController import questController

app = Flask(__name__)
app.secret_key = "chavesecreta123"

app.register_blueprint(questController)

@app.route("/")
def hello_world():
    return render_template("index.html")

rotas_publicas= ["questoes.index", "questoes.verifica"]

@app.before_request
def verificarIdentifica():
    if request.endpoint in rotas_publicas:
        return

    if "email" in session:
        return 
    return redirect(url_for("questoes.index"))

if __name__== "__main__":
    app.run(debug=True)