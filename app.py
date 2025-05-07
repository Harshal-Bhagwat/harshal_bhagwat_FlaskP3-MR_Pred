from flask import *
from pickle import *

f = open("model.pkl", "rb")
model = load(f)
f.close()

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def home():
	if request.method == "POST":
		d = request.form["rd"]
		readings = d.split()
		readings = [float(value) for value in readings]

		result = model.predict([readings])
		if result == "R":
			msg = "The Object detected is a Rock"
			return render_template("home.html", msg = msg)
		else:
			msg = "The Object detected is a Mine"
			return render_template("home.html", msg = msg)

	else:
		return render_template("home.html")

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)








