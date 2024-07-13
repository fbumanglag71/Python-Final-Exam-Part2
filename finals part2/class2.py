## Author: Francisco Bumanglag
## Project: Final Exam Part2
## Assignment: Module 8 Project 2
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: July 31, 2023



import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import os 


#DELETE THE MATH DB IF IT EXISTS  -- (update link as needed)
db_path = "C:\\Users\\franc\\OneDrive\\Documents\\SAC\\SUMMER 2023\\CMPR114 PHYTON\\MODULE8\\part2\\finals part2\\Math.db"
if os.path.exists(db_path):
    os.remove(db_path)
    
#CREATE THE MATH DATABASE 
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS scores
                (id INTEGER PRIMARY KEY,
                firstname TEXT,
                lastname TEXT,
                score REAL)''')
conn.commit()

#IMPORT THE DATA FROM THE TEXT FILE AND INSERT TINO THE DATABASE -- (update link as needed)
text_file_path = "C:\\Users\\franc\\OneDrive\\Documents\\SAC\\SUMMER 2023\\CMPR114 PHYTON\\MODULE8\\part1\\finals\\finals\\test_results.txt"
with open(text_file_path, "r") as file:
    for line in file:
        fields = line.strip().split()
        firstname = fields[0]
        lastname = fields[1]
        score = float(fields[3].replace('%', ''))
        cursor.execute("INSERT INTO scores (firstname, lastname, score) VALUES (?, ?, ?)",
                       (firstname, lastname, score))
conn.commit()

#CREATE THE FORM
class MathScoresApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Scores App")
        self.root.geometry("645x500")
     
        #IMPORT THE BACKGROUND IMAGE  -- (update link as needed)
        bg_image_path = "C:\\Users\\franc\\OneDrive\\Documents\\SAC\\SUMMER 2023\\CMPR114 PHYTON\\MODULE8\\part2\\finals part2\\mathimage.jpg"
        bg_image = Image.open(bg_image_path)
        self.bg_photo = ImageTk.PhotoImage(bg_image)  
        self.bg_label = ttk.Label(root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)
         


        #CREATE THE SAVE BUTTON
        self.save_button = ttk.Button(root, text="SAVE", command=self.display_scores)
        self.save_button.pack(pady=10)
    
    def display_scores(self):
        cursor.execute("SELECT firstname, lastname, score FROM scores")
        rows = cursor.fetchall()
        for row in rows:
            print(f"Firstname: {row[0]}, Lastname: {row[1]}, Score: {row[2]}")

#CREATE THE MAIN WINDOW APP
root = tk.Tk()
app = MathScoresApp(root)
root.mainloop()

#CLOSE THE CONNECTION
conn.close()



