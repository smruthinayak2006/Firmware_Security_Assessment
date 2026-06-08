import os
import sys


from flask import (
    Flask,
    render_template,
    request
)


sys.path.append(
    "analysis"
)


from scanner import scan_firmware



app = Flask(__name__)



UPLOAD_FOLDER = "uploads"


app.config[
    "UPLOAD_FOLDER"
] = UPLOAD_FOLDER



@app.route("/")
def home():

    return render_template(
        "index.html"
    )



@app.route(
    "/scan",
    methods=["POST"]
)
def scan():


    uploaded_file = request.files[
        "firmware"
    ]


    file_path = os.path.join(

        app.config[
            "UPLOAD_FOLDER"
        ],

        uploaded_file.filename
    )


    uploaded_file.save(
        file_path
    )


    results = scan_firmware(
        "sample_firmware"
    )



    return render_template(

        "index.html",

        results=results
    )




if __name__ == "__main__":

    app.run(
        debug=True
    )