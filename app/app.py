import os
import sys


from flask import (
    Flask,
    render_template,
    request,
    send_file
)

sys.path.append(
    "analysis"
)

from scanner import scan_firmware
from risk_analyzer import calculate_risk_summary

from database import (
    create_database,
    save_results
)

from report_generator import generate_report

from firmware_extractor import extract_firmware


app = Flask(__name__)
create_database()


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


    extracted_path = extract_firmware(
        file_path
    )

    results = scan_firmware(
        extracted_path
    )

    save_results(
        results
    )

    generate_report(
        results
    )

    summary = calculate_risk_summary(
        results
    )

    return render_template(

        "index.html",

        results=results,

        summary=summary

    )

@app.route("/download-report")
def download_report():


    return send_file(

        "../reports/security_report.json",

        as_attachment=True

    )


if __name__ == "__main__":

    app.run(
        debug=True
    )