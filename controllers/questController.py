from flask import Blueprint, render_template, request, redirect, url_for, session

questController = Blueprint("questoes", __name__)

@questController.route("/")
def index():
    return render_template("index.html")

@questController.route("/verifica", methods = ["POST"])
def verifica():
    nome = request.form.get("Nome")
    email= request.form["E-mail"] 
    if email.split("@")[1] == "aluno.ifsp.edu.br":
        session["email"] = email
        session["nome"] = nome
        return redirect(url_for("questoes.questionario"))
    return "E-mail Inválido."

@questController.route("/questionario")
def questionario():
        return render_template("questionario.html")

@questController.route("/logout")
def logout():
    session.pop("email", None)
    session.pop("nome", None)
    return redirect(url_for("questoes.index"))

@questController.before_request
def request_info():
    print("OLÁ")