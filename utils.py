def formatter(text, variables, sheet, j):
    """
    Format the mail text.

    Args:
        text (str): The mail text.
        variables (list): The variables to be inserted in the mail text.
        sheet (DataFrame): The DataFrame containing the emails and other data.
        j (int): The index of the row in the DataFrame.

    Returns:
        str: The formatted mail text.

    Commented parts are related to the robotics club.
    """
    text_f = text
    for i in variables:
        if i != "":
            text_f = text_f.replace("{" + f"{i}" + "}", str(sheet[i][j]))
    return text_f

def html_formatter(text, hyper_dict, width, height, pos_x, pos_y):
    """
    Format the mail text to be in HTML format.

    Args:
        text (str): The mail text.
        hyper_dict (dict): The dictionary containing the hyperlinks.
        width (int): The width of the photo.
        height (int): The height of the photo.
        pos_x (int): The x position of the photo.
        pos_y (int): The y position of the photo.

    Returns:
        str: The formatted mail text in HTML format.
    """
    text_br = text.replace("\n", "<br>")
    
    if hyper_dict != {}:
        for i in hyper_dict:
            text_br = text_br.replace("{{" + f"{i}" + "}}", f"""<a href={hyper_dict[i]}>{i}</a>""")
    text_h = f"""
<html>
    <body>
        <p>{text_br}<br>
            {'<br>'*pos_y if pos_y != 0 else ''}
            {'&nbsp;'*pos_x if pos_x != 0 else ''}
            {f'<img src="cid:image2" width="{width}" height="{height} style="position:relative; margin-bottom:50px;"><br>' 
             if width != 0 and height != 0 else ''}
            Sincerely,<br>
            --<br><br>
            <img src="cid:image1" width="200" height="77"><br>
            <i>This email was sent by an automated tool which was completely developed by Robotics Club members.</i><br>
            <font color="#e06666"><b>Info:</b></font> robotics.club@ejust.edu.eg<br>
            <font color="#e06666"><b>FB:</b></font> https://www.facebook.com/EJUST.Robotics/<br>
            <font color="#e06666"><b>LI:</b></font> https://www.linkedin.com/company/e-just-robotics-club/<br>
            <font color="#e06666"><b>IG:</b></font> https://www.instagram.com/robotics_ejust/<br><br>
        </p>
    </body>
</html>
"""
    
# Sincerely,<br>
# --<br><br>
# <img src="cid:image1" width="200" height="77"><br>
# <i>This email was sent by an automated tool which was completely developed by Robotics Club members.</i><br>
# <font color="#e06666"><b>Info:</b></font> robotics.club@ejust.edu.eg<br>
# <font color="#e06666"><b>FB:</b></font> https://www.facebook.com/EJUST.Robotics/<br>
# <font color="#e06666"><b>LI:</b></font> https://www.linkedin.com/company/e-just-robotics-club/<br><br>
# <font color="#e06666"><b>IG:</b></font> https://www.instagram.com/robotics_ejust/<br><br>
    return text_h