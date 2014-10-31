from flask import Flask,render_template,request,redirect
import utils

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        # post
        button = request.form["b"]
        uname  = request.form["uname"]
        pword  = request.form['pword']
        valid_user = utils.authenticate(uname,pword)
        error=None
        if button=="clear":
            return render_template("login.html")
        if button=="newUser":
            return redirect('/newUser')
        elif valid_user is False:
            error= "Did not match our records. Please try again or create a new account"
            return render_template("login.html",error=error)
        elif valid_user is True:
            return render_template("welcome.html",name=uname, error=error)



@app.route("/newUser", methods=["GET", "POST"])
def newUser():
    if request.method=="GET":
        return render_template("newUser.html")


if __name__=="__main__":
    app.debug=True
    app.run();
