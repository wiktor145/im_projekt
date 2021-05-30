import tkinter as tk
from tkinter import *


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
        btn = Button(frame, text="Show Full", command=lambda i=i: show_full_text(i))
        btn.grid(row=i, column=len(entry))
        i = i + 1

    frame1 = tk.Frame(root_frame)
    frame1.pack(side="bottom")

    def show_full_text(i):  # new window definition
        print(entries)
        newwin = Toplevel(root)

        T = Text(newwin, height=1, width=30, font=("Helvetica", 18))
        T.grid(row=1, column=1)
        T.insert(END, "Filename: " + str(entries[i][0]))
        T1 = Text(newwin, height=1, width=30, font=("Helvetica", 18))
        T1.grid(row=2, column=1)
        T1.insert(END, "Processed at: " + str(entries[i][1]))

        T4 = Text(newwin, height=15, width=30, font=("Helvetica", 18))
        T4.grid(row=3, column=1)
        T4.insert(END, str(entries[i][2]))

        scrollb = Scrollbar(newwin, command=T4.yview)
        scrollb.grid(row=3, column=2, sticky='nsew')
        T4['yscrollcommand'] = scrollb.set

    def refresh(frame, db_connection):
        global entries
        for widget in frame.winfo_children():
            widget.destroy()

        entries = db_connection.get_processed_files_with_dates()
        i = 0
        for entry in entries:
            for j in range(len(entry)):
                e = Entry(frame, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, entry[j])

            btn = Button(frame, text="Show Full", command=lambda i=i: show_full_text(i))
            btn.grid(row=i, column=len(entry))
            i = i + 1

    save_button = Button(frame1, text="Refresh", command=lambda: refresh(frame, db_connection)).pack()

    root.title("Files")
    root.mainloop()
