#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 17, 2021 07:14:34 PM CEST  platform: Windows NT

import sys
from tkinter import END, messagebox

import image_window
from report_generator.report_generator import generate_for_object

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


def init(top, gui, conn, series1, *args, **kwargs):
    global w, top_level, root, connection, series
    w = gui
    top_level = top
    root = top
    connection = conn
    series = series1
    populate()


def open_image(i):
    print(i)
    image_window.create_Toplevel1(root, connection, images_list[i])


def fill_series():
    global images_list
    images_list = connection.get_imagefiles_for_series(series)

    inner_frame = w.Scrolledwindow1_f
    button = {}
    for i in range(len(images_list)):
        e = tk.Entry(inner_frame, width=70, fg='blue')
        e.grid(row=i, column=1)
        e.insert(END, images_list[i].file.file_name)

        button[i] = tk.Button(inner_frame, text='Open', width=9, command=lambda i=i: open_image(i))
        button[i].grid(row=i, column=2, sticky='w')
    if button:
        button[0].wait_visibility()
    bbox = inner_frame.bbox()
    w.Scrolledwindow1.configure(scrollregion=bbox)


def fill_fields():
    w.Text1.insert(1.0, series.series_id)
    w.Text2.insert(1.0, series.SeriesInstanceUID)
    w.Text3.insert(1.0, series.study_id)
    w.Text4.insert(1.0, series.SeriesDate)
    w.Text5.insert(1.0, series.SeriesDescription)
    w.Text6.insert(1.0, series.SeriesNumber)
    w.Text7.insert(1.0, series.SeriesTime)


def populate():
    fill_fields()
    fill_series()


def generate_report():
    patient_fields = connection.get_patient_fields_from_study_id(series.study_id)

    name = generate_for_object(series, "series_images", len(images_list), "report_series",
                               {"Modality": connection.get_modality_for_series(series),
                                "StudyInstanceUID": connection.get_StudyInstanceUID_from_study_id(series.study_id),
                                "patient_id": patient_fields[0], "PatientID": patient_fields[1]
                                })
    if name:
        messagebox.showinfo("Report generated successfully", "Generated report " + name)
    else:
        messagebox.showerror("Error", "Error during generating report")


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import series_window

    series_window.vp_start_gui()
