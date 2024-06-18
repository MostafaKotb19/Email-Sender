import tkinter as tk
from tkinter.ttk import Label, Style
from ttkthemes import ThemedTk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import font
import pandas as pd
import threading
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from screeninfo import get_monitors

import data, pics, log, utils

class mail_sender(ThemedTk):
    """
    The main class that contains the GUI of the app.
    Inherits from ThemedTk to use the ttkthemes library.

    Args:
        geometry (Monitor): The geometry of the monitor to display the app on.
    """
    def __init__(self, geometry):
        super().__init__()
        self.configure(theme="arc")
        self.geometry(f"{geometry.width}x{geometry.height}")
        self.title("Robotics Club Mail Sender")

        icon_url = "https://drive.google.com/uc?id=1ath41s8lVndtejYcaU7St6cfhj-MjY7n"
        self.icon_response = requests.get(icon_url)

        self.iconphoto(True, tk.PhotoImage(data=self.icon_response.content))
        self.configure(bg="#FFFFFF")

        self.values = dict()             # Dictionary to store the values of the fields.
        self.hyper_dict = dict()         # Dictionary to store the hyperlinks.
        self.sending_emails = False      # Flag to control sending emails.
        self.sending_thread = None       # Thread to send emails.
        self.log_text = ""               # Text to be displayed in the log.

        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets of the app.
        """
        logo_url = "https://drive.google.com/uc?id=1SW77mzDnlTqWE2vhLk-U6j27w6mEgx6V"
        self.logo_response = requests.get(logo_url)
        self.logo = Image.open(BytesIO(self.logo_response.content))

        self.icon = Image.open(BytesIO(self.icon_response.content))

        # Fonts
        self.title_font = font.Font(family="Roboto", size=24, weight="bold")
        self.label_font = font.Font(family="Roboto", size=10)
        self.entry_font = font.Font(family="Roboto", size=10)
        self.button_font = font.Font(family="Roboto", size=10, weight="bold")

        self.configure_styles()

        # Title
        title = Label(self, text="Robotics Club Mail Sender", font=self.title_font, 
                      background="#FFFFFF", anchor="center")
        title.grid(column=0, row=0, pady=10, columnspan=5, sticky="ew")

        self.logo = self.logo.resize((200, 77), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        logo_label = Label(self, image=self.logo, background="#FFFFFF")
        logo_label.grid(row=2, column=0, padx=10, pady=10, sticky="sw", columnspan=4)

        self.data = data.data(self)
        self.pics = pics.pics(self)
        self.log = log.log(self)

    def configure_styles(self):
        """
        Configure the styles of the widgets.
        """
        self.style = Style(self)
        self.style.configure("TFrame", background="#FFFFFF")
        self.style.configure("TLabel", background="#FFFFFF")
        self.style.configure("TButton", background="#FFFFFF", font=self.button_font)
        self.style.configure("TEntry", background="#f8f8f8", bordercolor="#FF0000")

    def onClick(self):
        """
        Collects the values from the fields and starts sending the emails.
        """
        self.sending_emails = True
        self.log_text = ""
        
        self.values['email'] = self.data.email.get()
        self.values['pass'] = self.data.app_pass.get()
        
        self.values['book'] = self.data.book_link.get()
        self.values['book'] = self.values['book'][0 : self.values['book'].index("edit")]
        self.values['book'] = self.values['book'] + "gviz/tq?tqx=out:csv"
        
        self.values['sheet_name'] = self.data.sheet_name.get()
        self.values['subject'] = self.data.subject.get()
        self.values['text'] = self.data.text.get(1.0, "end-1c")
        self.values['variables'] = self.data.variables.get().split(", ")
        self.values['hyperlinks'] = self.data.hyperlinks.get()
        self.values['photos_dir'] = self.data.photos_dir.get()
        if self.values['photos_dir']:
            self.values['photo_extension'] = self.pics.photo_extension.get()
            self.values['photo_width'] = int(self.pics.photo_width.get())
            self.values['photo_height'] = int(self.pics.photo_height.get())
        else:
            self.values['photo_extension'] = ""
            self.values['photo_width'] = 0
            self.values['photo_height'] = 0
        self.values['photo_position_x'] = int(self.pics.photo_position_x.get())
        self.values['photo_position_y'] = int(self.pics.photo_position_y.get())
        
        if (self.values['hyperlinks'] != ""):
            raw = self.values['hyperlinks']             # Extract the hyperlinks.
            pairs = raw.split("; ")
            for i in pairs:
                key, value = i.split(", ")
                self.hyper_dict[key] = value
                
        url = self.values['book'] + "&sheet=" + self.values['sheet_name']   # Construct the URL.
        sheet = pd.read_csv(url)
        
        self.sender_email = self.values['email']
        self.password = self.values['pass']
        
        # Start sending the emails on a separate thread.
        self.sending_thread = threading.Thread(target=self.send_emails, args=(sheet,))
        self.sending_thread.start()

    def send_emails(self, sheet):
        """
        Send the emails to the recipients.

        Args:
            sheet (DataFrame): The DataFrame containing the emails and other data.
        """
        for i in range(len(sheet['Email'])):
            if not self.sending_emails:
                break
            port = 465 
            smtp_server = "smtp.gmail.com"
            message = MIMEMultipart("alternative")
            message["Subject"] = self.values['subject']
            message["From"] = self.sender_email
            receiver_email = sheet['Email'][i]
            message["To"] = receiver_email
            msg = utils.formatter(self.values['text'], self.values['variables'], sheet, i)     # Format the mail text.
            img = Image.open(os.path.join(self.values['photos_dir'], sheet['Name'][i] + "." +  # Open the image.
                                          self.values['photo_extension']))
            img_buffer = BytesIO()
            img.save(img_buffer, format=img.format)
            img_buffer.seek(0)

            msg_t = msg + \
            "\nSincerely,\n--\n\nThis email was sent by an automated tool which was completely developed by Robotics Club members.\
            \nInfo: robotics.club@ejust.edu.eg\nFB: https://www.facebook.com/EJUST.Robotics/\
            \nLI: https://www.linkedin.com/company/e-just-robotics-club/\n\n"                  # Add the signature.
            msg_h = utils.html_formatter(msg, self.hyper_dict,                                 # Convert the mail text to HTML.
                                   self.values['photo_width'], self.values['photo_height'], 
                                   self.values['photo_position_x'], self.values['photo_position_y'])
            
            msgImage = MIMEImage(self.logo_response.content)
            msgImage2 = MIMEImage(img_buffer.read())

            part1 = MIMEText(msg_t, "plain")
            part2 = MIMEText(msg_h, "html")
            
            # Combine text and HTML parts.
            message.attach(part1)
            message.attach(part2)

            # Attach the images.
            msgImage.add_header('Content-ID', '<image1>')
            msgImage2.add_header('Content-ID', '<image2>')
            message.attach(msgImage)
            message.attach(msgImage2)
    
            # Send the email.
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                    server.login(self.sender_email, self.password)
                    server.sendmail(self.sender_email, receiver_email, message.as_string())
                self.log_text += f"Email sent successfully to {receiver_email}!\n"
            except Exception as ex:
                self.log_text += f"Failed to send email to {receiver_email}: {ex}\n"

            # Update the log.
            self.log.log_textbox.configure(state='normal')
            self.log.log_textbox.delete(1.0, "end")
            self.log.log_textbox.insert(1.0, self.log_text)
            self.log.log_textbox.configure(state='disabled')

    def abort(self):
        """
        Abort sending the emails.
        """
        self.sending_emails = False
        self.log_text += "Emails sending aborted!\n"
        self.log.log_textbox.configure(state='normal')
        self.log.log_textbox.delete(1.0, "end")
        self.log.log_textbox.insert(1.0, self.log_text)
        self.log.log_textbox.configure(state='disabled')

if __name__ == "__main__":
    monitors = get_monitors()     # Get the monitor information.
    monitor = monitors[0]

    app = mail_sender(monitor)
    app.mainloop()