from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.pagesizes import letter

from datetime import datetime





def generate_pdf_report(

    results,

    summary,

    firmware,

    firmware_hash,

    security_score

):




    pdf = SimpleDocTemplate(

        "reports/security_report.pdf",

        pagesize=letter

    )




    styles = getSampleStyleSheet()



    content = []







    content.append(

        Paragraph(

            "Firmware Security Assessment Report",

            styles["Title"]

        )

    )





    content.append(

        Spacer(1, 20)

    )







    content.append(

        Paragraph(

            "Report Information",

            styles["Heading2"]

        )

    )






    content.append(

        Paragraph(

            "Generated Time: "

            + str(datetime.now()),

            styles["Normal"]

        )

    )






    content.append(

        Paragraph(

            "Tool: Automated Firmware Security Assessment",

            styles["Normal"]

        )

    )







    content.append(

        Spacer(1, 20)

    )









    content.append(

        Paragraph(

            "Executive Summary",

            styles["Heading2"]

        )

    )







    content.append(

        Paragraph(

            "Firmware Risk Score: "

            + str(security_score["risk_score"])

            + "/100",

            styles["Normal"]

        )

    )






    content.append(

        Paragraph(

            "Risk Level: "

            + security_score["risk_level"],

            styles["Normal"]

        )

    )






    content.append(

        Paragraph(

            "Total Vulnerabilities: "

            + str(summary["total"]),

            styles["Normal"]

        )

    )








    content.append(

        Spacer(1,20)

    )









    content.append(

        Paragraph(

            "Firmware Details",

            styles["Heading2"]

        )

    )






    firmware_table = [


        [

            "Name",

            firmware["name"]

        ],


        [

            "Size",

            str(firmware["size"])

            + " bytes"

        ],


        [

            "MD5",

            firmware_hash["md5"]

        ],


        [

            "SHA256",

            firmware_hash["sha256"]

        ]

    ]








    table = Table(

        firmware_table

    )






    table.setStyle(

        TableStyle(

            [

                ("GRID",(0,0),(-1,-1),0.5,None)

            ]

        )

    )





    content.append(

        table

    )









    content.append(

        Spacer(1,25)

    )









    content.append(

        Paragraph(

            "Vulnerability Findings",

            styles["Heading2"]

        )

    )









    vuln_table = [

        [

            "Issue",

            "Severity",

            "Recommendation"

        ]

    ]








    for item in results:



        vuln_table.append(

            [

                item["finding"]["issue"],

                item["finding"]["severity"],

                item["recommendation"]

            ]

        )









    vulnerability_table = Table(

        vuln_table,

        repeatRows=1

    )








    vulnerability_table.setStyle(

        TableStyle(

            [

                ("GRID",(0,0),(-1,-1),0.5,None)

            ]

        )

    )







    content.append(

        vulnerability_table

    )








    content.append(

        Spacer(1,25)

    )









    content.append(

        Paragraph(

            "Security Recommendation",

            styles["Heading2"]

        )

    )








    content.append(

        Paragraph(

            "Review all detected vulnerabilities, apply remediation steps, "

            "and validate firmware before production deployment.",

            styles["Normal"]

        )

    )










    pdf.build(

        content

    )