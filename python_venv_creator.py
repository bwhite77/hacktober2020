import tkinter as tk
from tkinter import filedialog
import subprocess
import os

selected_directory=""

def select_file():
	global selected_directory
	selected_directory = filedialog.askdirectory()
	ent_file.delete(0, tk.END)
	ent_file.insert(0, selected_directory)

def submit():
	global selected_directory
	venv_name = ent_env_name.get()

	selected_directory = selected_directory.replace('/', '\\')

	os.chdir(selected_directory)

	cmd = "cd /d " + selected_directory
	subprocess.run(cmd, shell=True)
	print(cmd)
	
	cmd = "python -m venv " + venv_name
	subprocess.run(cmd, shell=True)
	print(cmd)

	cmd = selected_directory + "\\Scripts\\activate.bat"
	subprocess.run(cmd, shell=True)
	print(cmd)
	print("ran submit")

root = tk.Tk()

ent_file = tk.Entry(root, width=100)
btn_select_file = tk.Button(root, text="Select File", command=select_file)

lbl_env_name = tk.Label(root, text="Enter a name for the virtual environment:")
ent_env_name = tk.Entry(root, width=100)

btn_submit = tk.Button(root, text="Submit", command=submit)

ent_file.grid(row=0, column=0)
btn_select_file.grid(row=1, column=0)
lbl_env_name.grid(row=2, column=0)
ent_env_name.grid(row=3, column=0)
btn_submit.grid(row=4, column=0)

root.mainloop()
