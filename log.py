import tkinter as tk
from tkinter.ttk import Frame, Label

class log(Frame):
    """
    The class that contains the log field to be filled by the app.
    Inherits from Frame to be a part of the GUI.
    """
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(column=4, row=1, padx=10, pady=10, rowspan=11, sticky="ne")
        self.log_text = """Insturctions:
Fill the fields and click send to start sending emails.
In case of a mistake while sending emails, click abort to stop sending emails.
The email column must be named as "Email".
If you are sending with photos, there must be a column named "Name", which will be used as the name of the photos.
The app is only working with png right now.
Variables should be put in the mail text in this format: {VariableName}.
Hyperlinks should be put in the mail text in this format: {{HyperlinkName}}.
        """
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets of the log frame.
        """
        log_label = Label(self, text="Log", background="#FFFFFF", font=self.master.label_font)
        log_label.grid(row = 0, column=0, sticky="w", pady=5)
        self.log_textbox = tk.Text(self, width=65, height=40, background="#f8f8f8", font=self.master.entry_font, 
                              bd=0, highlightthickness=1, highlightbackground="#dbe0ec", highlightcolor="#8eb9ec")
        self.log_textbox.grid(row = 1, column=0, sticky="nsew")
        self.log_textbox.insert(1.0, self.log_text)
        self.log_textbox.configure(state='disabled')