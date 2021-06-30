import json
from other_classes.configuration import Configuration
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
    root_frame = Frame(root)
    root_frame.pack()
    canvas = tk.Canvas(root_frame, borderwidth=0)
    frame = tk.Frame(canvas)
    vsb = tk.Scrollbar(root_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    conf = Configuration()

    list_of_tags = set()

    button_values = populate(frame, conf)
    frame1 = tk.Frame(root_frame)
    frame1.pack(side="bottom")

    def save_list_of_tags(button_values):
        for a, b in button_values:
            if b.get():
                print(a)
                list_of_tags.add(a)
            else:
                if a in list_of_tags:
                    list_of_tags.remove(a)

    save_button = Button(frame1, text="Save", command=lambda: save_list_of_tags(button_values)).pack()

    root.title("Choose DICOM tags to extract")
    root.mainloop()

    conf = Configuration(list(list_of_tags))

    js = json.dumps(conf.__dict__)

    with open("../../configuration.json", "w+") as f:
        f.write(str(js))


def configuration_gui():
    get_configuration_by_gui()


if __name__ == '__main__':
    get_configuration_by_gui()
