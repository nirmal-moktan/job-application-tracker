from flask import Flask, render_template, request, redirect, url_for
from tracker import view_applications, update_applications, add_applications

app = Flask(__name__) 
@app.route("/") 
def home():
    data = view_applications()
    return render_template("index.html", applications = data)
@app.route("/update-status/<int:application_id>", methods=["POST"])
def update_status(application_id):
    new_status = request.form["status"]

    update_applications(application_id, status = new_status)
    return redirect(url_for("home"))

@app.route("/add-application", methods=["POST"])
def add_application():
    new_application = {
        "company": request.form["company"],
        "job_title": request.form["job_title"],
        "location": request.form["location"],
        "applied_date": request.form["applied_date"],
        "status": request.form["status"],
        "remark": request.form["remark"]
    }
    add_applications(new_application)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
