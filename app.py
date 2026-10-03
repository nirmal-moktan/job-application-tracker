from flask import Flask, render_template
from tracker import view_applications

app = Flask(__name__) 
@app.route("/")  
def home():
    data = view_applications()
    return render_template("index.html", applications = data)

if __name__ == "__main__":
    app.run(debug=True)
