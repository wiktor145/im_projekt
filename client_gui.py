import tkinter as tk
from tkinter import *


def refresh(frame, db_connection):
    for widget in frame.winfo_children():
        widget.destroy()

    entries = db_connection.get_processed_files_with_dates()
    i = 0
    for entry in entries:
        for j in range(len(entry)):
            e = Entry(frame, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, entry[j])
        i = i + 1


def show_client_gui(db_connection):
    root = tk.Tk()
    root_frame = Frame(root)
    root_frame.pack()
    canvas = tk.Canvas(root_frame, borderwidth=0)
    frame = tk.Frame(canvas)
    vsb = tk.Scrollbar(root_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window(0, 0, window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    entries = db_connection.get_processed_files_with_dates()
    i = 0
    for entry in entries:
        for j in range(len(entry)):
            e = Entry(frame, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, entry[j])
        i = i + 1

    frame1 = tk.Frame(root_frame)
    frame1.pack(side="bottom")

    save_button = Button(frame1, text="Refresh", command=lambda: refresh(frame, db_connection)).pack()

    root.title("Files")
    root.mainloop()
