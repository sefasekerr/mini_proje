import smtplib
from email.mime.text import MIMEText
from users import user
import os
api_key = os.getenv("SENDINBLUE_KEY")

port = 587
smtp_server = "smtp-relay.brevo.com"
login = "9fed03001@smtp-brevo.com"


# user = {
#     "email":"sefaseker92@gmail.com",
#     "namesurname":"sefa şeker"
# }
def send_email(user):
    sender_email = "sefaseker92@gmail.com"
    receiver_email = user["email"]

    text = f"""
    hoşgeldinn {user["namesurname"]}
    vayyyy ilk e-postammm
    python uygulmasından geldi"""
    try:
        message = MIMEText(text,"plain")
        message["Subject"]=f"merhaba {user["namesurname"]}"
        message["From"] = "info@gmail.com"
        message["To"]= receiver_email

        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls()
            server.login(login,api_key)
            server.sendmail(sender_email,receiver_email,message.as_string())
    except smtplib.SMTPAuthenticationError as e:
        print("Kimlik doğrulama hatası:", e)

    except smtplib.SMTPConnectError as e:
        print("Bağlantı hatası:", e)

    except smtplib.SMTPRecipientsRefused as e:
        print("Alıcı reddetti:", e)

    except Exception as e:
        print("Beklenmeyen bir hata oluştu:", e)

    

