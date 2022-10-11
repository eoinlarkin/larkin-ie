from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def root():
    # application assumes all content is in a json file
    # see example file in content/content-example.json
    with open("content/content.json") as j_file:
        context = json.load(j_file, strict=False)

    print(context["meta"])

    return render_template(
        "index.html",
        meta=context["meta"][0],
        about=context["about"],
        links=context["links"],
        tools=context["tools"],
        projects=context["projects"],
    )


if __name__ == "__main__":
    # This is used when running locally only. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
