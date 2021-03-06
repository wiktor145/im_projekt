#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 17, 2021 05:44:43 PM CEST  platform: Windows NT
#    Jun 17, 2021 06:07:56 PM CEST  platform: Windows NT

import sys
from tkinter import END, messagebox

from tkcalendar import DateEntry

import current_configuration
import patient_window
import edit_configuration
from other_classes.constants import LAST_FILE_MTIME_FILE, DELETED_MARK

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

Custom = DateEntry


def clear_last_file_time_fun():
    with open(LAST_FILE_MTIME_FILE, "w") as f:
        f.write(DELETED_MARK)


def init(top, gui, db_connection, *args, **kwargs):
    global w, top_level, root, connection
    w = gui
    top_level = top
    root = top
    connection = db_connection
    refresh_patients()


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def open_current_configuration():
    current_configuration.create_Toplevel1(root)


def refresh_patients():
    global patients_list

    from_date, to_date = None, None

    if w.from_date_check.get():
        from_date = w.Custom1.get_date()

    if w.to_date_check.get():
        to_date = w.Custom2.get_date()

    patients_list = connection.get_patients(from_date, to_date)

    inner_frame = w.Scrolledwindow1_f
    button = {}
    for widget in inner_frame.winfo_children():
        widget.destroy()

    for i in range(len(patients_list)):
        e = tk.Entry(inner_frame, width=35, fg='blue')
        e.grid(row=i, column=1)
        e.insert(END, patients_list[i].PatientID)

        e = tk.Entry(inner_frame, width=35, fg='blue')
        e.grid(row=i, column=2)
        e.insert(END, patients_list[i].PatientName)

        button[i] = tk.Button(inner_frame, text='Open', width=9, command=lambda i=i: open_patient(i))
        button[i].grid(row=i, column=3, sticky='w')
    if button:
        button[0].wait_visibility()
    bbox = inner_frame.bbox()
    w.Scrolledwindow1.configure(scrollregion=bbox)


def open_patient(i):
    print(i)
    patient_window.create_Toplevel1(root, connection, patients_list[i])


def clear_database():
    res = messagebox.askyesno("Clear Database",
                              "Are you sure? This will clear WHOLE database and clear last checked file time.")
    if res:
        connection.clean_database()
        clear_last_file_time_fun()
        refresh_patients()


def clear_last_file_time():
    res = messagebox.askyesno("Clear Last Checked File Time",
                              "Are you sure? This will cause repository checker to check all files once again.")
    if res:
        clear_last_file_time_fun()


def open_edit_configuration():
    edit_configuration.create_Toplevel1(root)


if __name__ == '__main__':
    import dicom_repository

    dicom_repository.vp_start_gui()
