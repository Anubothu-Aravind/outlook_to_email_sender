import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "intelligentsia.techclub@gmail.com"
password = "shqyweynmnnxsaqz"  # Replace with your Gmail password or app password
subject = "Congratulations! Welcome to INTELLIGENTSIA"
telegram_link = "https://t.me/+cYly3NBMztM4MGFl"  # Link valid for 6 days

# List of aspirant IDs
aspirant_ids = [
    "2300030379",
    "2300033155",
    "2300032086",
    "2300033136",
    "2300080009",
    "2300080314",
    "2300080412",
    "2200080137"
]

# Function to send email
def send_email(to_email):
    # Email message content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Set high priority headers
    message["X-Priority"] = "1"  # 1 = High priority
    message["X-MSMail-Priority"] = "High"
    message["Importance"] = "High"

    # Body of the email
    body = f"""
    Dear Aspirant,

    Congratulations on being selected as part of the INTELLIGENTSIA club!

    We are excited to have you on board and can't wait to see the amazing work you'll contribute. 
    As a next step, please join the official Aspirants group using the following link:

    {telegram_link}

    Please note, the link will expire in 6 days.
    When joining the group, use the following format: <ID_NUMBER NAME>

    Best regards,
    INTELLIGENTSIA Team
    Department of AI & DS
    """

    message.attach(MIMEText(body, "plain"))

    # Sending the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, to_email, message.as_string())
    print(f"High-priority email sent to {to_email}")

# Sending email to each aspirant
for aspirant_id in aspirant_ids:
    recipient_email = f"{aspirant_id}@kluniversity.in"
    send_email(recipient_email)
