import tkinter as tk
from tkinter.ttk import Frame, Label, Entry, Button

class pics(Frame):
    """
    The class that contains the picture fields to be filled by the user.
    Inherits from Frame to be a part of the GUI.
    """

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid(column=2, row=1, sticky="n", padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        """
        Create the widgets of the picture frame.
        """
        Label(self, text="Photo Extension", background="#FFFFFF", font=self.master.label_font).grid(
            row=0, column=0, sticky="w", pady=5)
        Label(self, text="Photo Width", background="#FFFFFF", font=self.master.label_font).grid(
            row=1, column=0, sticky="w", pady=5)
        Label(self, text="Photo Height", background="#FFFFFF", font=self.master.label_font).grid(
            row=2, column=0, sticky="w", pady=5)
        Label(self, text="Photo Position", background="#FFFFFF", font=self.master.label_font).grid(
        row=3, column=0, sticky="w", pady=5)

        self.photo_extension = Entry(self, width=20, font=self.master.entry_font)            # Photo Extension Entry
        self.photo_extension.grid(row=0, column=1, sticky="w", pady=5, padx=5)
        self.photo_width = Entry(self, width=20, font=self.master.entry_font)                # Photo Width Entry
        self.photo_width.grid(row=1, column=1, sticky="w", pady=5, padx=5)
        self.photo_height = Entry(self, width=20, font=self.master.entry_font)               # Photo Height Entry
        self.photo_height.grid(row=2, column=1, sticky="w", pady=5, padx=5)
        self.photo_position_x = Entry(self, width=20, font=self.master.entry_font)           # Photo Position X Entry
        self.photo_position_x.grid(row=3, column=1, sticky="w", pady=5, padx=5)
        self.photo_position_y = Entry(self, width=20, font=self.master.entry_font)           # Photo Position Y Entry
        self.photo_position_y.grid(row=3, column=2, sticky="w", pady=5, padx=5)

        photo_view = tk.Text(self, background="#f8f8f8", height=30, width=50, bd=0, highlightthickness=1, 
                    highlightbackground="#dbe0ec", highlightcolor="#8eb9ec")
        photo_view.grid(row=5, column=0, columnspan=3, sticky="nsew", pady=5)

        width, height = 0, 0
        self.frame_photo = tk.Frame(photo_view, width=width, height=height, background="#000000")
        self.frame_photo.place(x=0, y=0)                                                     # Photo preview

        preview = Button(self, text="Preview", command=self.update_photo)                    # Preview Button
        preview.grid(row=4, column=0, columnspan=3, sticky="ew", pady=5)
    
    def update_photo(self):
        """
        Update the photo preview.
        """
        width = int(self.photo_width.get())
        height = int(self.photo_height.get())
        pos_x = int(self.photo_position_x.get())
        pos_y = int(self.photo_position_y.get())
        self.frame_photo.place(x=pos_x*5, y=pos_y*20, width=width, height=height)
        self.frame_photo.update()
        self.frame_photo.update_idletasks()