# import smtplib
# from email.mime.text import MIMEText
# from users import user
# import os
# api_key = os.getenv("SENDINBLUE_KEY")

# port = 587
# smtp_server = "smtp-relay.brevo.com"
# login = "sefaseker92@gmail.com"


# user = {
#     "email":"sefaseker92@gmail.com",
#     "namesurname":"sefa şeker"
# }
# def send_email(user):
#     sender_email = "sefaseker92@gmail.com"
#     receiver_email = user["email"]

#     text = f"""
#     hoşgeldinn {user["namesurname"]}
#     vayyyy ilk e-postammm
#     python uygulmasından geldi"""
#     try:
#         message = MIMEText(text,"plain")
#         message["Subject"]=f"merhaba {user["namesurname"]}"
#         message["From"] = sender_email
#         message["To"]= receiver_email

#         with smtplib.SMTP(smtp_server,port) as server:
#             server.starttls()
#             server.login(login,api_key)
#             server.sendmail(sender_email,[receiver_email],message.as_string())
#     except smtplib.SMTPAuthenticationError as e:
#         print("Kimlik doğrulama hatası:", e)

#     except smtplib.SMTPConnectError as e:
#         print("Bağlantı hatası:", e)

#     except smtplib.SMTPRecipientsRefused as e:
#         print("Alıcı reddetti:", e)

#     except Exception as e:
#         print("Beklenmeyen bir hata oluştu:", e)
        
        
# send_email(user)
    

import smtplib
from email.mime.text import MIMEText
import os

api_key = os.getenv("SENDINBLUE_KEY")
smtp_server = "smtp-relay.brevo.com"
port = 587
login = "9fed03001@smtp-brevo.com"
# print(api_key)
user = {
    "email": "sefaseker92@gmail.com",
    "namesurname": "sefa şeker"
}

def send_email(user):
    sender_email = "sefaseker92@gmail.com"
    receiver_email = user["email"]

    text = f"""
    hoşgeldin {user["namesurname"]}
    vayyyy ilk e-postammm
    python uygulamasından geldi
    """
    try:
        message = MIMEText(text, "plain", "utf-8")
        message["Subject"] = f"merhaba {user['namesurname']}"
        message["From"] = sender_email
        message["To"] = receiver_email

        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(login, api_key)
            server.sendmail(sender_email, [receiver_email], message.as_string())
        print("Mail başarıyla gönderildi!")

    except Exception as e:
        print("Beklenmeyen bir hata oluştu:", e)

send_email(user)
