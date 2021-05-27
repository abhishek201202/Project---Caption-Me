from flask import Flask, render_template, request
from numpy.lib.utils import info
import ImageCaptioning

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods = ["POST"])
def submit_data():
    if(request.method == "POST"):
       f = request.files["userfile"]
       imgPath = "./static/images/{}".format(f.filename)
       f.save(imgPath)
       caption = ImageCaptioning.PredictCaption(imgPath)
       res = {
           "Path": imgPath,
           "Caption": caption
       }
       print(caption)
    return render_template("index.html", Prediction = res)


if(__name__ == "__main__"):
    app.run(debug=True)

