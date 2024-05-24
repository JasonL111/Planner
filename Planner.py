# Library imports
import customtkinter
from tkinter import messagebox
from datetime import datetime
import os


# Jason L use CTkinter finish that, feel free to edit and use it 😎.
# Project URL: https://github.com/JasonL111/Planner
# CTKinter: https://customtkinter.tomschimansky.com/


# This value is for translation
IsEnglish = True


# Save Textbox content to a file
def create_popup(message):
    text_content = Textbox.get("1.0", customtkinter.END)
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}.txt"
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    full_path = os.path.join(desktop_path, filename)
    try:
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(text_content)
        messagebox.showinfo("Success", "File has been saved to the desktop")
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the file: {e}")


# Load plan from a file
def readfile():
    Textbox.delete("1.0", "end")
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}.txt"

    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    full_path = os.path.join(desktop_path, filename)

    try:
        with open(full_path, "r", encoding="utf-8") as file:
            content = file.read()
            Textbox.insert("1.0", content)
        messagebox.showinfo("Success", "File has been loaded from the desktop")
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the file: {e}")


# Delete current plan in Textbox
def deleteplan():
    Textbox.delete("1.0", "end")
    Textbox.insert("1.0", "Urgent and Important:\n- \n- \n")
    Textbox.insert("4.0", "Urgent but Not Important:\n- \n- \n")
    Textbox.insert("7.0", "Not Urgent but Important:\n- \n- \n")
    Textbox.insert("10.0", "Neither Urgent Nor Important:\n- \n- \n")


# Add bullet points in new line on 'Enter' key press
def on_enter(event):
    index = Textbox.index("insert").split(".")
    line_number = int(index[0])
    Textbox.insert(f"{line_number}.end", "\n- ")
    return "break"


def change_language():
    if IsEnglish == True:
        Chinese()
    else:
        English()

# Change to English
def English():
    global IsEnglish
    Textbox.delete("1.0", "end")
    Textbox.insert("1.0", "Urgent and Important:\n- \n- \n")
    Textbox.insert("4.0", "Urgent but Not Important:\n- \n- \n")
    Textbox.insert("7.0", "Not Urgent but Important:\n- \n- \n")
    Textbox.insert("10.0", "Neither Urgent Nor Important:\n- \n- \n")
    IsEnglish = True

# Change to Chinese
def Chinese():
    global IsEnglish
    Textbox.delete("1.0", "end")
    Textbox.insert("1.0", "紧急且重要:\n- \n- \n")
    Textbox.insert("4.0", "紧急但不重要:\n- \n- \n")
    Textbox.insert("7.0", "不紧急但重要:\n- \n- \n")
    Textbox.insert("10.0", "不紧急且不重要:\n- \n- \n")
    IsEnglish = False


# Initialize and configure main window
root = customtkinter.CTk()
root.geometry("600x650")
root.title("The Real Planner")
root.iconbitmap("icon.ico")
root.configure(bg="#FFFFF6")


# Create a label in the window
label = customtkinter.CTkLabel(root, text="J Planner", font=("微软雅黑", 22))


# Create a Textbox for user input
Textbox = customtkinter.CTkTextbox(
    root, height=500, font=("微软雅黑", 18), width=500, corner_radius=10
)
Textbox.insert("1.0", "Urgent and Important:\n- \n- \n")
Textbox.insert("4.0", "Urgent but Not Important:\n- \n- \n")
Textbox.insert("7.0", "Not Urgent but Important:\n- \n- \n")
Textbox.insert("10.0", "Neither Urgent Nor Important:\n- \n- \n")

# Create buttons for functions
button1 = customtkinter.CTkButton(
    root,
    text="Save",
    font=("微软雅黑", 24),
    command=lambda: create_popup("Save Successful"),
    corner_radius=15,
    width=48,
    height=10,
)
button2 = customtkinter.CTkButton(
    root,
    text="Delete",
    font=("微软雅黑", 24),
    command=deleteplan,
    corner_radius=15,
    width=48,
    height=10,
)
button3 = customtkinter.CTkButton(
    root,
    text="Load",
    font=("微软雅黑", 24),
    command=readfile,
    corner_radius=15,
    width=48,
    height=10,
)
button4 = customtkinter.CTkButton(
    root,
    text="Language",
    font=("微软雅黑", 24),
    command=change_language,
    corner_radius=15,
    width=48,
    height=10,
)

Textbox.bind("<Return>", on_enter)


for i in range(12):
    root.columnconfigure(i, weight=1)
for j in range(15):
    root.rowconfigure(j, weight=1)


# Place a label in the window
label.grid(column=0, row=0, columnspan=12)


# Place a Textbox for user input
Textbox.grid(column=1, row=1, columnspan=10, rowspan=11, sticky="nsew")

# Place buttons
button1.grid(column=1, row=13, columnspan=1, sticky="nsew")
button2.grid(column=4, row=13, columnspan=1, sticky="nsew")
button3.grid(column=7, row=13, columnspan=1, sticky="nsew")
button4.grid(column=10, row=13, columnspan=1, sticky="nsew")


# Start the main event loop of the window
root.mainloop()
