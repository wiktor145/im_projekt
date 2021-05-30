from tkinter import *
from configuration import Configuration
from tkinter.tix import *
import tkinter as tk


def get_configuration_by_gui():
    def populate(frame, conf):
        button_values = []
        for tag in conf.small_list_of_fields:
            var = IntVar()
            Checkbutton(frame, text=tag, variable=var).pack()
            button_values.append((tag, var))
        return button_values

    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    root = tk.Tk()
    canvas = tk.Canvas(root, borderwidth=0)
    frame = tk.Frame(canvas)
    vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    conf = Configuration()

    list_of_tags = set()

    button_values = populate(frame, conf)
    frame1 = tk.Frame(canvas)

    def save_list_of_tags(button_values):
        for a, b in button_values:
            if b.get():
                print(a)
                list_of_tags.add(a)
            else:
                if a in list_of_tags:
                    list_of_tags.remove(a)

    save_button = Button(frame1, text="Save", command=lambda: save_list_of_tags(button_values)).pack()
    canvas.create_window((4, 4), window=frame1, anchor="nw")

    root.title("Choose DICOM tags to extract")
    root.mainloop()

    print(list_of_tags)
    return list_of_tags