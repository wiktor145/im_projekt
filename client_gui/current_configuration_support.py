#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Jun 17, 2021 05:47:29 PM CEST  platform: Windows NT
import json
import sys

from other_classes.constants import CONFIGURATION_FILE

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


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

    f = open(CONFIGURATION_FILE, "r")
    configuration = json.load(f)
    f.close()

    for tag in configuration['fields_to_extract']:
        w.Scrolledlistbox1.insert("end", tag)


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


if __name__ == '__main__':
    import current_configuration

    current_configuration.vp_start_gui()
