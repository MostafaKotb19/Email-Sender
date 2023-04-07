import smtplib, ssl
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import urllib.request
from tkinter import *
from tkinter import ttk
from PIL import Image

urllib.request.urlretrieve(
  'https://ci3.googleusercontent.com/mail-sig/AIorK4z7jynaNE4OreZuRnqAF2igfAzi2UJS8yXNJ2srC8h5xLLR8a0tiszL8pdU1TFCZJmy5vb2WVU',
   "club.png")

#vlvsihsmqzpatsrd

img = Image.open("club.png")
img = img.save("club.png")

def formatter(text, variables, sheet, j):
    text_f = text
    for i in variables:
        text_f = text_f.replace(f"{i}", str(sheet[i][j]))
    text_f = text_f.replace("{", "").replace("}", "")
    return text_f

def html_formatter(text, hyper_dict):
    text_br = text.replace("\n", "<br>")
    
    if hyper_dict != {}:
        for i in hyper_dict:
            text_br = text_br.replace(i, f"""<a href={hyper_dict[i]}>{i}</a>""")
    text_h = f"""
<html>
    <body>
        <p>{text_br}<br>
            Sincerely,<br>
            --<br><br>
            <img src="cid:image1" width="200" height="77"><br>
            <i>This email was sent by an automated tool which was completely developed by Robotics Club members.</i><br>
            <font color="#e06666"><b>Info:</b></font> robotics.club@ejust.edu.eg<br>
            <font color="#e06666"><b>FB:</b></font> https://www.facebook.com/EJUST.Robotics/<br><br>
        </p>
    </body>
</html>
"""
    return text_h
def onClick():
    values['email'] = email.get()
    values['pass'] = app_pass.get()
    
    values['book'] = book_link.get()
    values['book'] = values['book'][0 : values['book'].index("edit")]
    values['book'] = values['book'] + "gviz/tq?tqx=out:csv"
    
    values['sheet_name'] = sheet_name.get()
    values['subject'] = subject.get()
    values['text'] = text.get(1.0, "end-1c")
    values['variables'] = variables.get().split(", ")
    values['hyperlinks'] = hyperlinks.get()
    
    if (values['hyperlinks'] != ""):
        raw = values['hyperlinks']
        pairs = raw.split("; ")
        for i in pairs:
            key, value = i.split(", ")
            hyper_dict[key] = value
            
    url = values['book'] + "&sheet=" + values['sheet_name']
    sheet = pd.read_csv(url)
    
    sender_email = values['email']
    password = values['pass']
    
    for i in range(len(sheet['Email'])):
        port = 465 
        smtp_server = "smtp.gmail.com"
        message = MIMEMultipart("alternative")
        message["Subject"] = values['subject']
        message["From"] = sender_email
        receiver_email = sheet['Email'][i]
        message["To"] = receiver_email
        msg = formatter(values['text'], values['variables'], sheet, i)
        
        msg_t = msg + \
        "\nSincerely,\n--\n\nThis email was sent by an automated tool which was completely developed by Robotics Club members.\nInfo: robotics.club@ejust.edu.eg\nFB: https://www.facebook.com/EJUST.Robotics/"
        msg_h = html_formatter(msg, hyper_dict)
        
        fp = open("club.png", 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        part1 = MIMEText(msg_t, "plain")
        part2 = MIMEText(msg_h, "html")
        
        message.attach(part1)
        message.attach(part2)

        msgImage.add_header('Content-ID', '<image1>')
        message.attach(msgImage)
  
        
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong….", ex)

    
    


values = dict()
hyper_dict = dict()

window = Tk()
window.geometry("500x750")

Label(window, text = "Email").place(x = 30, y = 30)
Label(window, text = "App Password").place(x = 30, y = 70)
Label(window, text = "Workbook Link").place(x = 30, y = 110)
Label(window, text = "Sheet Name").place(x = 30, y = 150)
Label(window, text = "Mail Subject").place(x = 30, y = 190)
Label(window, text = "Hyperlinks").place(x = 30, y = 230)
Label(window, text = "In this format: \"Word, Link; Word, Link\"").place(x = 120, y = 250)
Label(window, text = "Variables").place(x = 30, y = 270)
Label(window, text = "Separated by \", \"").place(x = 120, y = 290)
Label(window, text = "Mail").place(x = 30, y = 310)

email = ttk.Entry(window, width = 40)
email.place(x = 120, y = 30)
app_pass = ttk.Entry(window, width = 40)
app_pass.place(x = 120, y = 70)
book_link = ttk.Entry(window, width = 40)
book_link.place(x = 120, y = 110)
sheet_name = ttk.Entry(window, width = 40)
sheet_name.place(x = 120, y = 150)
subject = ttk.Entry(window, width = 40)
subject.place(x = 120, y = 190)
hyperlinks = ttk.Entry(window, width = 40)
hyperlinks.place(x = 120, y = 230)
variables = ttk.Entry(window, width = 40)
variables.place(x = 120, y = 270)
text = Text(window, width = 50, height = 20)
text.place(x = 30, y = 340)

send = ttk.Button(window, text = "Send", command = onClick)
send.place(x = 200, y = 680)

window.mainloop()