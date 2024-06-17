import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import re

def assess_password_strength(password):
    length_score = 0
    uppercase_score = 0
    lowercase_score = 0
    number_score = 0
    special_score = 0

    length = len(password)
    if length >= 8:
        length_score = 1
    if length >= 12:
        length_score = 2
    if length >= 16:
        length_score = 3


    if any(char.isupper() for char in password):
        uppercase_score = 1


    if any(char.islower() for char in password):
        lowercase_score = 1


    if any(char.isdigit() for char in password):
        number_score = 1


    if any(char in r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" for char in password):
        special_score = 1


    total_score = length_score + uppercase_score + lowercase_score + number_score + special_score


    if total_score == 5:
        strength = "Very Strong"
    elif total_score == 4:
        strength = "Strong"
    elif total_score == 3:
        strength = "Moderate"
    elif total_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"


    feedback = []
    if length_score == 0:
        feedback.append("Password is too short. Try making it at least 8 characters long.")
    if not uppercase_score:
        feedback.append("Include at least one uppercase letter.")
    if not lowercase_score:
        feedback.append("Include at least one lowercase letter.")
    if not number_score:
        feedback.append("Include at least one number.")
    if not special_score:
        feedback.append("Include at least one special character (e.g., !, @, #, $, etc.).")

    feedback_message = "Password Strength: " + strength + "\n"
    if feedback:
        feedback_message += "Suggestions to improve your password:\n" + "\n".join(feedback)
    else:
        feedback_message += "Your password is very strong!"

    return feedback_message

def submit_password():
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match. Please try again.")
        return

    feedback_message = assess_password_strength(password)
    messagebox.showinfo("Password Strength", feedback_message)

def reset_fields():
    entry_password.delete(0, tk.END)
    entry_confirm_password.delete(0, tk.END)

def toggle_password_visibility():
    global show_password
    if show_password:
        entry_password.config(show='*')
        entry_confirm_password.config(show='*')
        toggle_button.config(image=eye_icon_closed)
        show_password = False
    else:
        entry_password.config(show='')
        entry_confirm_password.config(show='')
        toggle_button.config(image=eye_icon_open)
        show_password = True

def exit_application():
    root.destroy()


root = tk.Tk()
root.title("Password Complexity Checker")

# Define color scheme
background_color = "#F0F0F0"  # Very light grey background
button_color = "#404040"      # Dark grey buttons
text_color = "#000000"         # Black text
entry_color = "#CCCCCC"       # Light grey for entry fields


root.configure(bg=background_color)


title_font = ("Verdana", 16, "bold")
body_font = ("Verdana", 12)


label_title = tk.Label(root, text="Password Complexity Checker", bg=background_color, fg=text_color, font=title_font)
label_title.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


label_password = tk.Label(root, text="Enter Password:", bg=background_color, fg=text_color, font=body_font)
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, width=30, bg=entry_color, font=body_font, show='*', fg=text_color)
entry_password.grid(row=1, column=1, padx=10, pady=10)


label_confirm_password = tk.Label(root, text="Confirm Password:", bg=background_color, fg=text_color, font=body_font)
label_confirm_password.grid(row=2, column=0, padx=10, pady=10)
entry_confirm_password = tk.Entry(root, width=30, bg=entry_color, font=body_font, show='*', fg=text_color)
entry_confirm_password.grid(row=2, column=1, padx=10, pady=10)


eye_icon_open = PhotoImage(file='eye.png').subsample(6)
eye_icon_closed = PhotoImage(file='eye_closed.png').subsample(6)


show_password = False
toggle_button = tk.Button(root, image=eye_icon_closed, command=toggle_password_visibility, bg=background_color, borderwidth=0)
toggle_button.grid(row=1, column=2, padx=10, pady=5, rowspan=2)


button_submit = tk.Button(root, text="Submit", command=submit_password, bg=button_color, fg=text_color, font=body_font, width=10)
button_submit.grid(row=4, column=0, padx=10, pady=10, sticky="ew")


button_reset = tk.Button(root, text="Reset", command=reset_fields, bg=button_color, fg=text_color, font=body_font, width=10)
button_reset.grid(row=4, column=1, padx=10, pady=10, sticky="ew")


button_exit = tk.Button(root, text="Exit", command=exit_application, bg=button_color, fg=text_color, font=body_font, width=10)
button_exit.grid(row=4, column=2, padx=10, pady=10, sticky="ew")


root.mainloop()
