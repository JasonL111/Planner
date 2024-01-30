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

# Initialize the main window
root = tk.Tk()
root.geometry("900x600")  # Set window size
root.title("The Real Planner")  # Set window title
root.iconbitmap('icon.ico') 
root.configure(bg='blue')
# Create a label and add it to the window
label = tk.Label(root, text="Plan", font=('Arial', 18),bg='blue')
label.pack()

# Create a Text widget for user input
Textbox = tk.Text(root, height=12, font=('Arial', 18),bg="gray")
Textbox.insert("1.0", "Urgent and Important:\n\n\n")
Textbox.insert("4.0", "Urgent but Not Important:\n\n\n")
Textbox.insert("7.0", "Not Urgent but Important:\n\n\n")
Textbox.insert("10.0", "Neither Urgent Nor Important:\n\n\n")
Textbox.pack()

# Create a button that triggers the 'create_popup' function
button = tk.Button(root, text="Save", font=('Arial', 18), command=lambda: create_popup("Save Successful"))
button.pack(padx=10, pady=10)

# Start the application
root.mainloop()
