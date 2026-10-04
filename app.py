from flask import Flask, render_template, request, redirect, url_for
from tracker import view_applications, update_applications, add_applications, delete_applications

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

@app.route("/edit-application", methods=["POST"])
def edit_application():
    application_id = request.form["application_id"]
    new_company = request.form["company"]
    new_job_title = request.form["job_title"]
    new_location = request.form["location"]
    new_applied_date = request.form["applied_date"]
    new_status = request.form["status"]
    new_remark = request.form["remark"]

    update_applications(application_id, company=new_company, job_title=new_job_title, location=new_location, applied_date=new_applied_date, status=new_status, remark=new_remark)
    return redirect(url_for("home"))

@app.route("/delete-application", methods=["POST"])
def delete_application():
    application_id = request.form["application_id"]

    delete_applications(application_id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
