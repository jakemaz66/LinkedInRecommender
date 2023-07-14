from flask import Flask, render_template, request, jsonify
from quality_search import quality_search

app = Flask(__name__)

#Rendering the website html
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    person_info, profile_pic_url = quality_search(name=name)

    return jsonify(
        {
            "summary": person_info.summary,
            "argument": person_info.argument,
            "facts": person_info.facts,
            "qualifications": person_info.qualifications,
            "picture_url": profile_pic_url,
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)