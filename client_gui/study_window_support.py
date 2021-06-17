#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 17, 2021 07:12:18 PM CEST  platform: Windows NT

import sys
from tkinter import END

import series_window

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def init(top, gui, conn, study1, *args, **kwargs):
    global w, top_level, root, connection, study
    w = gui
    top_level = top
    root = top
    connection = conn
    study = study1
    populate()


def open_series(i):
    print(i)
    series_window.create_Toplevel1(root, connection, series_list[i])


def fill_series():
    global series_list
    series_list = connection.get_series_for_study(study)

    inner_frame = w.Scrolledwindow1_f
    button = {}
    for i in range(len(series_list)):
        e = tk.Entry(inner_frame, width=70, fg='blue')
        e.grid(row=i, column=1)
        e.insert(END, series_list[i].SeriesInstanceUID)

        button[i] = tk.Button(inner_frame, text='Open', width=9, command=lambda i=i: open_series(i))
        button[i].grid(row=i, column=2, sticky='w')
    if button:
        button[0].wait_visibility()
    bbox = inner_frame.bbox()
    w.Scrolledwindow1.configure(scrollregion=bbox)


def fill_fields():
    w.Text1.insert(1.0, study.study_id)
    w.Text2.insert(1.0, study.StudyInstanceUID)
    w.Text3.insert(1.0, study.patient_id)
    w.Text4.insert(1.0, study.StudyDate)
    w.Text5.insert(1.0, study.StudyDescription)
    w.Text6.insert(1.0, study.StudyID)
    w.Text7.insert(1.0, study.StudyIDIssuer)
    w.Text8.insert(1.0, study.StudyTime)


def populate():
    fill_fields()
    fill_series()


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import study_window

    study_window.vp_start_gui()
