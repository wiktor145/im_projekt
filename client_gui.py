import tkinter as tk
from tkinter import *

entries = []

def show_client_gui(db_connection):
    global entries
    root = tk.Tk()
    root.geometry("800x500")
    root_frame = Frame(root)
    root_frame.pack()
    canvas = tk.Canvas(root_frame, borderwidth=0)
    frame = tk.Frame(canvas)
    vsb = tk.Scrollbar(root_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window(0, 0, window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox("all")))

    entries = db_connection.get_processed_files_with_dates()
    i = 0
    for entry in entries:
        for j in range(len(entry) - 2):
            e = Entry(frame, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, entry[j])
        btn = Button(frame, text="Show Full", command=lambda i=i: show_full_text(i))
        btn.grid(row=i, column=len(entry))
        i = i + 1

    frame1 = tk.Frame(root_frame)
    frame1.pack(side="bottom")

    def refresh(frame, db_connection):
        global entries
        for widget in frame.winfo_children():
            widget.destroy()

        entries = db_connection.get_processed_files_with_dates()
        i = 0
        for entry in entries:
            for j in range(len(entry) - 2):
                e = Entry(frame, width=20, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, entry[j])

            btn = Button(frame, text="Show Full", command=lambda i=i: show_full_text(i))
            btn.grid(row=i, column=len(entry))
            i = i + 1

    def save_comment(file_name, comment_text):
        global entries
        db_connection.save_comment_for_file(file_name, comment_text.get("1.0", "end-1c"))
        refresh(frame, db_connection)

    def show_full_text(i):  # new window definition
        global entries
        newwin = Toplevel(root)

        T = Text(newwin, height=1, width=50, font=("Helvetica", 18))
        T.grid(row=1, column=1)
        T.insert(END, "Filename: " + str(entries[i][0]))
        T1 = Text(newwin, height=1, width=50, font=("Helvetica", 18))
        T1.grid(row=2, column=1)
        T1.insert(END, "Processed at: " + str(entries[i][1]))

        row = 3

        values = db_connection.get_values_list_for_file(str(entries[i][0]))
        print(values)
        for a, b in values:
            t = Text(newwin, height=1, width=92, font=("Helvetica", 10))
            t.grid(row=row, column=1)
            t.insert(END, str(a) + " ==>> " + str(b))
            row += 1

        T4 = Text(newwin, height=10, width=50, font=("Helvetica", 18))
        T4.grid(row=row, column=1)
        T4.insert(END, str(entries[i][2]))

        scrollb = Scrollbar(newwin, command=T4.yview)
        scrollb.grid(row=row, column=3, sticky='nsew')
        T4['yscrollcommand'] = scrollb.set
        T4.config(state=DISABLED)

        row += 1

        T5 = Text(newwin, height=10, width=50, font=("Helvetica", 18))
        T5.grid(row=row, column=1)
        T5.insert(END, str(entries[i][3]))

        scrollb1 = Scrollbar(newwin, command=T5.yview)
        scrollb1.grid(row=row, column=3, sticky='nsew')
        T5['yscrollcommand'] = scrollb1.set

        row += 1

        save_comment_button = Button(newwin, text="Save comment", command=lambda: save_comment(str(entries[i][0]), T5))
        save_comment_button.grid(row=row, column=1)

    save_button = Button(frame1, text="Refresh", command=lambda: refresh(frame, db_connection)).pack()

    root.title("Files")
    root.mainloop()
