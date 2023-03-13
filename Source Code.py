import tkinter as tk
import io
import sys
import pandas as pd
import numpy as np
import matplotlib as plt
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


root = tk.Tk()
root.title("Cog-jupyter")
root.geometry("1480x830")

image=tk.PhotoImage(file=r"C:\Users\saksh\OneDrive\Desktop\Cognifrontt\Cog-Jupyter by Sakshi.gif")
image_label=tk.Label(root, image=image)
image_label.pack()

def run_code():
    
    output_label.delete(1.0, tk.END)
    code = code_input.get("1.0", "end-1c")
    output_stream = io.StringIO()
    sys.stdout = output_stream
    try:
        exec(code)
        output_label.insert("1.0", output_stream.getvalue())
    except Exception as e:
        output_label.insert("1.0", str(e))
        sys.stdout = sys._stdout_

code_input = tk.Text(root, height=20, width=200)
code_input.pack()

run_button = tk.Button(root, text="Run", font=("Helvetica", 17), fg="black", bg="orange", command=run_code)
run_button.pack()

output_label = tk.Text(root, bg="white", width=220, height=25)
output_label.pack()

root.mainloop()