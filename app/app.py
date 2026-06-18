from flask import Flask, render_template, request, send_file, redirect, session

import os

import sys



sys.path.append(

    os.path.abspath("analysis")

)



from scanner import scan_firmware

from firmware_extractor import extract_firmware

from risk_analyzer import calculate_risk_summary

from report_generator import generate_report

from firmware_analyzer import analyze_firmware

from hash_analyzer import calculate_hash

from database import save_results, get_scan_history





app = Flask(__name__)



app.secret_key = "firmware_security_secret_key"



UPLOAD_FOLDER = "uploads"


app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER





@app.route("/login", methods=["GET", "POST"])


def login():



    if request.method == "POST":



        username = request.form["username"]


        password = request.form["password"]




        if username == "admin" and password == "admin123":



            session["logged_in"] = True



            return redirect("/")




    return render_template(

        "login.html"

    )








@app.route("/logout")


def logout():



    session.clear()



    return redirect(

        "/login"

    )










@app.route("/")


def home():



    if "logged_in" not in session:



        return redirect(

            "/login"

        )





    return render_template(

        "index.html",

        results=None,

        summary=None,

        filename=None

    )











@app.route("/scan", methods=["POST"])


def scan():



    if "logged_in" not in session:



        return redirect(

            "/login"

        )






    uploaded_file = request.files["firmware"]





    file_path = os.path.join(

        app.config["UPLOAD_FOLDER"],

        uploaded_file.filename

    )





    uploaded_file.save(

        file_path

    )






    firmware_info = analyze_firmware(

        file_path

    )





    firmware_hash = calculate_hash(

        file_path

    )






    extracted_path = extract_firmware(

        file_path

    )





    results = scan_firmware(

        extracted_path

    )






    summary = calculate_risk_summary(

        results

    )





    save_results(

        results

    )






    generate_report(

        results,

        summary,

        firmware_info,

        firmware_hash

    )






    return render_template(

        "index.html",

        results=results,

        summary=summary,

        filename=uploaded_file.filename,

        firmware=firmware_info,

        firmware_hash=firmware_hash

    )









@app.route("/history")


def history():



    if "logged_in" not in session:



        return redirect(

            "/login"

        )





    scan_history = get_scan_history()





    return render_template(

        "history.html",

        history=scan_history

    )










@app.route("/download")


def download():



    if "logged_in" not in session:



        return redirect(

            "/login"

        )





    return send_file(

        "../reports/security_report.json",

        as_attachment=True

    )








if __name__ == "__main__":



    app.run(

        debug=True

    )