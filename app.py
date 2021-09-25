from flask import *
import os,json


app = Flask(__name__)
app.secret_key = "4yuugkg7iinyvvr9mm"
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# login page
@app.route("/login")
def login():
    return render_template("login.html")


# authentication for login
@app.route("/authenticate" , methods = ["GET","POST"])
def authenticate():
    name = request.form["name"]
    if name == "user" :
        return redirect(url_for("home"))
    else :
        return "Invalid Credentials "


# home page
@app.route("/home")
def home():
    f=open("data.csv","a")
    
    data = []
    for line in f:
        data.append(line.split(","))
    f.close()
    # return {"data":data}
    return render_template("home.html")


# ajax api (returns data to frontend from backend)
@app.route("/ajax_api")
def ajax_api():
    files = open("data.csv","r")
    data = []
    for x in files:
        data.append(x.split(","))
        
    files.close()
    return {"data" : data}


# ajax test 
@app.route("/ajax_test")
def ajax_test():
    return render_template("ajax_api.html")

    
if __name__ == "__main__":
    app.run(host = "localhost") 
