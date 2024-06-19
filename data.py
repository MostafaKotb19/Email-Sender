import tkinter as tk
from tkinter.ttk import Frame, Label, Entry, Button

class data(Frame):
    """
    The class that contains data fields to be filled by the user.
    Inherits from Frame to be a part of the GUI.
    """
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(column=0, row=1, sticky="nw", padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets of the data frame.
        """
        Label(self, text = "Email", background="#FFFFFF", font=self.master.label_font).grid(
            row=0, column=0, padx=10, pady=5, sticky="w")
        Label(self, text = "Password", background="#FFFFFF", font=self.master.label_font).grid(
            row=1, column=0, padx=10, pady=5, sticky="w")
        Label(self, text = "Workbook Link", background="#FFFFFF", font=self.master.label_font).grid(
            row=2, column=0, padx=10, pady=5, sticky="w")
        Label(self, text = "Sheet Name", background="#FFFFFF", font=self.master.label_font).grid(
            row=3, column=0, padx=10, pady=5, sticky="w")
        Label(self, text = "Mail Subject", background="#FFFFFF", font=self.master.label_font).grid(
            row=4, column=0, padx=10, pady=5, sticky="w")
        Label(self, text = "Hyperlinks", background="#FFFFFF", font=self.master.label_font).grid(
            row=5, column=0, padx=10, pady=5, sticky="w")
        Label(self, text = "In this format: \"Word, Link; Word, Link\"", background="#FFFFFF", 
            font=self.master.label_font).grid( row=6, column=1, columnspan=3, padx=10)
        Label(self, text = "Variables", background="#FFFFFF", font=self.master.label_font).grid(
            row=7, column=0, padx=10, pady=5, sticky="w")
        Label(self, text = "Separated by \", \"", background="#FFFFFF", font=self.master.label_font).grid(
            row=8, column=1, columnspan=3, padx=10)
        Label(self, text = "Photos Directory", background="#FFFFFF", font=self.master.label_font).grid(
            row=9, column=0, padx=10, pady=5, sticky="w")
        Label(self, text = "Absolute Directory", background="#FFFFFF", font=self.master.label_font).grid(
            row=10, column=1, columnspan=3, padx=10)
        Label(self, text = "Mail", background="#FFFFFF", font=self.master.label_font).grid(
            row=11, column=0, padx=10, pady=5, sticky="w")

        self.email = Entry(self, width = 60, font=self.master.entry_font)                            # Email Entry
        self.email.grid(row=0, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        self.app_pass = Entry(self, width = 60, font=self.master.entry_font)                         # Password Entry
        self.app_pass.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        self.book_link = Entry(self, width = 60, font=self.master.entry_font)                        # Workbook Link Entry
        self.book_link.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        self.sheet_name = Entry(self, width = 60, font=self.master.entry_font)                       # Sheet Name Entry
        self.sheet_name.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        self.subject = Entry(self, width = 60, font=self.master.entry_font)                          # Mail Subject Entry
        self.subject.grid(row=4, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        self.hyperlinks = Entry(self, width = 60, font=self.master.entry_font)                       # Hyperlinks Entry
        self.hyperlinks.grid(row=5, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        self.variables = Entry(self, width = 60, font=self.master.entry_font)                        # Variables Entry
        self.variables.grid(row=7, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        self.photos_dir = Entry(self, width = 60, font=self.master.entry_font)                       # Photos Directory Entry
        self.photos_dir.grid(row=9, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        self.text = tk.Text(self, width = 60, height = 20, background="#f8f8f8", font=self.master.entry_font, 
                       bd=0, highlightthickness=1, highlightbackground="#dbe0ec", highlightcolor="#8eb9ec")
        self.text.grid(row=11, column=1, columnspan=3, padx=10, pady=5, sticky="w", ipadx=5)         # Mail Text Entry

        send = Button(self, text = "Send", command = self.master.on_click)                            # Send Button
        send.grid(row=12, column=1)

        abortt = Button(self, text = "Abort", command = self.master.abort)                           # Abort Button
        abortt.grid(row=12, column=3)