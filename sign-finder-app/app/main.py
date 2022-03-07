from flask import Flask, request, render_template 
  
app = Flask(__name__) 
  
@app.route("/", methods =["GET", "POST"]) 
def sign_finder():
    if request.method == "POST":
        num_entered = request.form.get("enumber")
        if int(num_entered) > 0:
            return "The entered number is positive"
        elif int(num_entered) < 0:
            return "The entered number is negative"
        else:
            return "Invalid response please try again"
    return render_template("form.html")
