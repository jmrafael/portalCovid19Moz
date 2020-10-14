import os

from string import Template

from cs50 import SQL
from datetime import datetime, date
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///pcm.db")

#INDEX

@app.route("/")
#@login_required
def index():
    # positivos
    p = db.execute("SELECT count(*) AS p FROM casos WHERE result = :result", result='Positivo')

    # negativos
    n = db.execute("SELECT count(*) AS n FROM casos WHERE result = :result", result='Negativo')

    # obitos
    o = db.execute("SELECT count(*) AS o FROM casos WHERE status = :status", status='d')

    # recuperados
    r = db.execute("SELECT count(*) AS r FROM casos WHERE status = :status", status='r')
    return render_template("index.html", p=p, n=n, o=o, r=r, data=date.today())

# ADMIN

@app.route("/admin/register", methods=["POST"])
def register():
    #If submitting
    if request.method == "POST":

        #VALIDATIONS

        #Validating username filling
        if not request.form.get("username"):
            return render_template("/admin/login.html")

        #Validating password filling
        if not request.form.get("password"):
            return render_template("/admin/login.html")
        if not request.form.get("confirmation"):
            return render_template("/admin/login.html")

        #Validating passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
                return render_template("/admin/login.html")

        #Inserting the user
        query = db.execute("INSERT INTO utilizadores (name, username, password, regdate) VALUES(:name, :username, :password, :regdate)", name=request.form.get("name"), username=request.form.get("username"), password=generate_password_hash(request.form.get("password")), regdate=date.today() )
        #if query didnt go properly
        if not query:
            return render_template("/admin/login.html")

        #get the user Id
        session["user_id"] = query

        # Redirect user to login form
        return redirect("/admin/login")

    #if just opennig
    else:
        return render_template("/admin/login.html")


@app.route("/admin/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("/admin/login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("/admin/login.html")

        # Query database for username
        rows = db.execute("SELECT * FROM utilizadores WHERE username = :username", username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return render_template("/admin/login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Flash info for the user
        #flash(f"Logged in as {request.form.get("username"))}")

        # Redirect user to home page
        return redirect("/admin/index")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("/admin/login.html")

@app.route("/admin/index", methods=["GET", "POST"])
@login_required
def adminIndex():
    # MAIN DATA
    # todos testados
    t = db.execute("SELECT count(*) AS testados FROM casos ")

    # positivos
    p = db.execute("SELECT count(*) AS positivos FROM casos WHERE result = :result", result='Positivo')

    # negativos
    n = db.execute("SELECT count(*) AS negativos FROM casos WHERE result = :result", result='Negativo')

    # obitos
    o = db.execute("SELECT count(*) AS obitos FROM casos WHERE status = :status", status='d')

    # recuperados
    r = db.execute("SELECT count(*) AS recuperados FROM casos WHERE status = :status", status='r')

    ############# Casos por Província: POSITTIVOS / NEGATIVOS / TOTAL ##################
    # Maputo Cidade
    mpCP = db.execute("SELECT count(*) AS mpCP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Maputo Cidade')
    mpCN = db.execute("SELECT count(*) AS mpCN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Maputo Cidade')
    mpCT = db.execute("SELECT count(*) AS mpCT FROM casos WHERE province=:province", province='Maputo Cidade')

    # Maputo Província
    mpPP = db.execute("SELECT count(*) AS mpPP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Maputo Provincia')
    mpPN = db.execute("SELECT count(*) AS mpPN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Maputo Provincia')
    mpPT = db.execute("SELECT count(*) AS mpPT FROM casos WHERE province=:province", province='Maputo Provincia')

    # Gaza
    gzP = db.execute("SELECT count(*) AS gzP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Gaza')
    gzN = db.execute("SELECT count(*) AS gzN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Gaza')
    gzT = db.execute("SELECT count(*) AS gzT FROM casos WHERE province=:province", province='Gaza')

    # Inhambane
    imbP = db.execute("SELECT count(*) AS imbP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Inhambane')
    imbN = db.execute("SELECT count(*) AS imbN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Inhambane')
    imbT = db.execute("SELECT count(*) AS imbT FROM casos WHERE province=:province", province='Inhambane')

    # Sofala
    sfP = db.execute("SELECT count(*) AS sfP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Sofala')
    sfN = db.execute("SELECT count(*) AS sfN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Sofala')
    sfT = db.execute("SELECT count(*) AS sfT FROM casos WHERE province=:province", province='Sofala')

    # Manica
    mnP = db.execute("SELECT count(*) AS mnP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Manica')
    mnN = db.execute("SELECT count(*) AS mnN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Manica')
    mnT = db.execute("SELECT count(*) AS mnT FROM casos WHERE province=:province", province='Manica')

    # Tete
    ttP = db.execute("SELECT count(*) AS ttP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Tete')
    ttN = db.execute("SELECT count(*) AS ttN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Tete')
    ttT = db.execute("SELECT count(*) AS ttT FROM casos WHERE province=:province", province='Tete')

    # Zambezia
    zmP = db.execute("SELECT count(*) AS zmP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Zambézia')
    zmN = db.execute("SELECT count(*) AS zmN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Zambézia')
    zmT = db.execute("SELECT count(*) AS zmT FROM casos WHERE province=:province", province='Zambézia')

    # Niassa
    nsP = db.execute("SELECT count(*) AS nsP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Niassa')
    nsN = db.execute("SELECT count(*) AS nsN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Niassa')
    nsT = db.execute("SELECT count(*) AS nsT FROM casos WHERE province=:province", province='Niassa')

    # Nampula
    npP = db.execute("SELECT count(*) AS npP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Nampula')
    npN = db.execute("SELECT count(*) AS npN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Nampula')
    npT = db.execute("SELECT count(*) AS npT FROM casos WHERE province=:province", province='Nampula')

    # Cabo Delgado
    cdP = db.execute("SELECT count(*) AS cdP FROM casos WHERE result = :result AND province=:province", result='Positivo', province='Cabo Delgado')
    cdN = db.execute("SELECT count(*) AS cdN FROM casos WHERE result = :result AND province=:province", result='Negativo', province='Cabo Delgado')
    cdT = db.execute("SELECT count(*) AS cdT FROM casos WHERE province=:province", province='Cabo Delgado')

    ############# Casos por Gênero: POSITTIVOS / NEGATIVOS / OBITOS / TOTAL DE TESTADOS ##################
    # Masculino
    mP = db.execute("SELECT count(*) AS mP FROM casos WHERE result = :result AND gender=:gender", result='Positivo', gender='Masculino')
    mN = db.execute("SELECT count(*) AS mN FROM casos WHERE result = :result AND gender=:gender", result='Negativo', gender='Masculino')
    mR = db.execute("SELECT count(*) AS mR FROM casos WHERE status = :status AND gender=:gender", status='r', gender='Masculino')
    mO = db.execute("SELECT count(*) AS mO FROM casos WHERE status = :status AND gender=:gender", status='d', gender='Masculino')
    mT = db.execute("SELECT count(*) AS mT FROM casos WHERE gender=:gender", gender='Masculino')

    # Feminino
    fP = db.execute("SELECT count(*) AS fP FROM casos WHERE result = :result AND gender=:gender", result='Positivo', gender='Feminino')
    fN = db.execute("SELECT count(*) AS fN FROM casos WHERE result = :result AND gender=:gender", result='Negativo', gender='Feminino')
    fR = db.execute("SELECT count(*) AS fR FROM casos WHERE status = :status AND gender=:gender", status='r', gender='Feminino')
    fO = db.execute("SELECT count(*) AS fO FROM casos WHERE status = :status AND gender=:gender", status='d', gender='Feminino')
    fT = db.execute("SELECT count(*) AS fT FROM casos WHERE gender=:gender", gender='Feminino')

    return render_template("/admin/index.html", t=t, p=p, n=n, o=o, r=r, mP=mP, mN=mN, mR=mR, mO=mO, mT=mT, fP=fP, fN=fN, fR=fR, fO=fO, fT=fT, mpCP=mpCP, mpCN=mpCN, mpCT=mpCT, mpPP=mpPP, mpPN=mpPN, mpPT=mpPT, gzP=gzP, gzN=gzN, gzT=gzT, imbP=imbP, imbN=imbN, imbT=imbT, sfP=sfP, sfN=sfN, sfT=sfT, mnP=mnP, mnN=mnN, mnT=mnT, ttP=ttP, ttN=ttN, ttT=ttT, zmP=zmP, zmN=zmN, zmT=zmT, nsP=nsP, nsN=nsN, nsT=nsT, npP=npP, npN=npN, npT=npT, cdP=cdP, cdN=cdN, cdT=cdT)

@app.route("/admin/page-user", methods=["GET", "POST"])
@login_required
def pageUser():
    if request.method == "POST":

        password = request.form.get("password")

        # Validate and Update
        if password:
            update = db.execute("UPDATE utilizadores SET name=:name, username=:username, password=:password WHERE id=:id", id=int(session["user_id"]), name=request.form.get("name"), username=request.form.get("username"), password=generate_password_hash(request.form.get("password")) )
            return redirect("/admin/login")
        else:
             return render_template("/admin/index")
    else:
        user = db.execute("SELECT * FROM utilizadores WHERE id = :id", id=int(session["user_id"]))
        return render_template("/admin/page-user.html", user=user)

@app.route("/admin/cases-create", methods=["GET", "POST"])
@login_required
def caseCreate():
    if request.method == "POST":
        #VALIDATIONS
        if not request.form.get("result"):
            return render_template("/admin/cases-create.html")
        if not request.form.get("age"):
            return render_template("/admin/cases-create.html")
        if not request.form.get("contacts"):
            return render_template("/admin/cases-create.html")
        if not request.form.get("telephone"):
            return render_template("/admin/cases-create.html")
        if not request.form.get("province"):
            return render_template("/admin/cases-create.html")
        if not request.form.get("gender"):
            return render_template("/admin/cases-create.html")


        #Inserting the user
        query = db.execute("INSERT INTO casos (result, age, contacts, email, telephone, alt_telephone, province, qrHouse, nrHouse, address, gender, obs, userid, regdate) VALUES(:result, :age, :contacts, :email, :telephone, :alt_telephone, :province, :qrHouse, :nrHouse, :address, :gender, :obs, :userid, :regdate)", result=request.form.get("result"), age=request.form.get("age"), contacts=request.form.get("contacts"), email=request.form.get("email"), telephone=request.form.get("telephone"), alt_telephone=request.form.get("alt_telephone"), province=request.form.get("province"), qrHouse=request.form.get("qrHouse"), nrHouse=request.form.get("nrHouse"), address=request.form.get("address"), gender=request.form.get("gender"), obs=request.form.get("obs"), userid=int(session["user_id"]), regdate=date.today())
        #if query didnt go properly
        if not query:
            return render_template("/admin/cases-create.html")

        # Redirect user to list
        return redirect("/admin/cases-list")

    #if just opennig
    else:
        return render_template("/admin/cases-create.html")

@app.route("/admin/cases-list", methods=["GET", "POST"])
@login_required
def caseList():
    cases = db.execute("SELECT * FROM casos")
    return render_template("/admin/cases-list.html", cases=cases)

@app.route("/admin/case-details/<case_id>", methods=["GET", "POST"])
@login_required
def caseDetails(case_id):
    caseData = db.execute("SELECT * FROM casos WHERE id=:id", id=case_id)
    return render_template("/admin/case-details.html", caseData=caseData)

@app.route("/admin/case-recovered/<case_id>", methods=["GET", "POST"])
@login_required
def caseRecovered(case_id):
    if request.method == "GET":
        recovered = db.execute("UPDATE casos SET status=:status WHERE id = :id", status="r", id=case_id)
        return redirect("/admin/cases-list")

@app.route("/admin/case-death/<case_id>", methods=["GET", "POST"])
@login_required
def caseDeath(case_id):
    if request.method == "GET":
        recovered = db.execute("UPDATE casos SET status=:status WHERE id = :id", status="d", id=case_id)
        return redirect("/admin/cases-list")

@app.route("/admin/logout", methods=["GET", "POST"])
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/admin/login")