# Email Sender
An automated tool designed to streamline the process of sending personalized emails to multiple recipients with integrated images and hyperlinks. Developed using Python and Tkinter, it supports customization through a user-friendly GUI and ensures efficient and error-free email communication.

The tool can currently send personalized emails with different variables, hyperlinks and images.

## Install
To create an environment with the requirements through conda:
```
conda env create -f environment.yml
conda activate mail_sender
```

Or through a venv:
```
python -m venv mail_sender
source mail_sender/bin/activate #(on linux)
./mail_sender/Scripts/activate.bat #(on windows)
```

## Usage
Simply:
```
python main.py
```

## Description
[main.py](main.py) is the main executable. It loads the GUI, contains the mail sending paradigm, and creates different threads for sending and aborting.

[data.py](data.py) contains data fields to be filled by the user.

[pics.py](pics.py) contains the picture fields to be filled by the user.

[log.py](log.py) contains the log field to be filled by the app.

[utils.py](utils.py) contains different util functions for handling email body preprocessing.
