'''
GCP 寄email會有問題QQ，待研究...
這份檔案是做email通知的功能，如果程式出錯，無法及時刷新到最新中獎號時，會寄email通知我來修XD
'''
import smtplib
import os


def send_alert():
    my_email = "beta.lin.tw@gmail.com"
    sender_pw = os.environ["sender_pw"]
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=sender_pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="sb2828sb@gmail.com",
            msg=f"Subject:5000-quick-search danger\n\nSource code changed, it's not real-time data now.\n\n"
                f"Take some time to fix your code and update backup data!"
        )
