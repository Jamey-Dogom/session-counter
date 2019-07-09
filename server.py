from flask import Flask, render_template, request, redirect,  session

app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'keep it secret, keep it safe' #set a secret key for security purposes


# handle the form


@app.route("/")
def index():
    if 'count' not in session:
        session["count"] = 0
    #The above lines are there to make sure the count starts at zero    
    session["count"] += 1
    return render_template("index.html", count=session["count"])

@app.route("/add2", methods=["POST"])
def reloadplus2():
    session["count"] += 1
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session["count"] = 0
    return redirect("/")

app.run(debug=True)