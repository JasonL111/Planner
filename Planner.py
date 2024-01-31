import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os

#Build by Jason
#Github URL:https://github.com/JasonL111/Planner

# Define a function to create a popup and save the Textbox content to a file
def create_popup(message):
    # Retrieve the content from the Textbox widget
    text_content = Textbox.get("1.0", tk.END)
    
    # Use the current date as the filename
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}.txt"
    
    # Get the path to the desktop and construct the full file path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    full_path = os.path.join(desktop_path, filename)
    
    # Attempt to save the text content to the specified file
    try:
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(text_content)
        messagebox.showinfo("Success", "File has been saved to the desktop")
    except Exception as e:
        messagebox.showerror("Error", f"Error while saving the file: {e}")
# Define a function to load plan
def readfile():
    # Use the current date as the filename
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}.txt"
    # Get the path to the desktop and construct the full file path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    full_path = os.path.join(desktop_path, filename)
    # Attempt to save the text content to the specified file
    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read()
            Textbox.insert("1.0", content)
        messagebox.showinfo("Success", "File has been loaded from the desktop")
    except Exception as e:
        messagebox.showerror("Error", f"Error while loading the file: {e}")
# Define a function to delete plan
def deleteplan():
    Textbox.insert("1.0", "Urgent and Important:\n-\n-\n")
    Textbox.insert("4.0", "Urgent but Not Important:\n-\n-\n")
    Textbox.insert("7.0", "Not Urgent but Important:\n-\n-\n")
    Textbox.insert("10.0", "Neither Urgent Nor Important:\n-\n-\n")
# Define a function to add bullet points in new line  
def on_enter(event):
    index = Textbox.index("insert").split(".")
    line_number = int(index[0])
    Textbox.insert(f"{line_number}.end", "\n- ")
    return "break"
# Initialize the main window
root = tk.Tk()
root.geometry("900x600")  # Set window size
root.title("The Real Planner")  # Set window title
root.iconbitmap('icon.ico') 
root.configure(bg='#FFFFF6')
#Create a menu bar
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=1)
filemenu.add_command(label="New",command=deleteplan)
filemenu.add_command(label="Open",command=readfile)
filemenu.add_command(label="Tidy")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu,font=('Arial',14))
root.config(menu=menubar)
# Create a label and add it to the window
label = tk.Label(root, text="J Planner", font=('Arial', 18),bg='#FFFFF6')
label.pack()

# Create a Text widget for user input
Textbox = tk.Text(root, height=12, font=('Arial', 18),bg='#FFFFF6')
Textbox.insert("1.0", "Urgent and Important:\n-\n-\n")
Textbox.insert("4.0", "Urgent but Not Important:\n-\n-\n")
Textbox.insert("7.0", "Not Urgent but Important:\n-\n-\n")
Textbox.insert("10.0", "Neither Urgent Nor Important:\n-\n-\n")
Textbox.pack()

# Create a button that triggers the 'create_popup' function
button = tk.Button(root, text="Save", font=('Arial', 18), command=lambda: create_popup("Save Successful"),bg="#B8EAF1",fg="#7A7A7A")
button.pack(padx=10, pady=10)
# bind <Return> with on_enter function
Textbox.bind("<Return>", on_enter)
# Start the application
root.mainloop()
