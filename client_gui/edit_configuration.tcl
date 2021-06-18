#############################################################################
# Generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#  Jun 18, 2021 02:51:19 PM CEST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) 
    wm focusmodel $top passive
    wm geometry $top 600x450+437+127
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3844 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    label $top.lab45 \
        -background #0080c0 -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -text {Edit Configuration} 
    vTcl:DefineAlias "$top.lab45" "Label1" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledwindow::CreateCmd $top.scr46 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 317 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 324 
    vTcl:DefineAlias "$top.scr46" "Scrolledwindow1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr46.01 configure -background white \
        -borderwidth 2 \
        -height 75 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -relief groove \
        -selectbackground blue \
        -selectforeground white \
        -width 125
    label $top.lab47 \
        -background #0080c0 -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 14 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -text {Tags to extract} 
    vTcl:DefineAlias "$top.lab47" "Label2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Select All} 
    vTcl:DefineAlias "$top.but48" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Deselect All} 
    vTcl:DefineAlias "$top.but49" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $top.but50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Save 
    vTcl:DefineAlias "$top.but50" "Button3" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab45 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.007 -height 0 \
        -relheight 0.091 -anchor nw -bordermode ignore 
    place $top.scr46 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.267 -width 0 -relwidth 0.54 \
        -height 0 -relheight 0.704 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.156 -width 0 -relwidth 0.507 \
        -height 0 -relheight 0.069 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 0 -relx 0.683 -y 0 -rely 0.289 -width 117 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 0 -relx 0.683 -y 0 -rely 0.4 -width 117 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but50 \
        -in $top -x 0 -relx 0.7 -y 0 -rely 0.844 -width 107 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}



set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

