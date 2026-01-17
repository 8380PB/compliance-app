import smtplib, os
from email.message import EmailMessage

def send_report(to_email, pdf_path):
    msg = EmailMessage()
    msg["Subject"] = "Your Document Risk Exposure Report"
    msg["From"] = os.getenv("SMTP_USER")
    msg["To"] = to_email
    msg.set_content(
        "Attached is your automated risk exposure report.\n\n"
        "This report is advisory and non-certifying."
    )

    with open(pdf_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename="report.pdf"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        smtp.send_message(msg)