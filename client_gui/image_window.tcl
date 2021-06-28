#############################################################################
# Generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#  Jun 28, 2021 09:16:13 PM CEST  platform: Windows NT
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




proc vTclWindow.top57 {base} {
    global vTcl
    if {$base == ""} {
        set base .top57
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m68" -background #f2f2f2 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 866x647+305+63
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
    label $top.lab58 \
        -activebackground #f9f9f9 -activeforeground black -background #0080c0 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text Image 
    vTcl:DefineAlias "$top.lab58" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab59 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief ridge -text image_id 
    vTcl:DefineAlias "$top.lab59" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab62 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief ridge -text series_id 
    vTcl:DefineAlias "$top.lab62" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab63 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief ridge -text file_id 
    vTcl:DefineAlias "$top.lab63" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab64 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief ridge -text file_name 
    vTcl:DefineAlias "$top.lab64" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab65 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief ridge -text ImageType 
    vTcl:DefineAlias "$top.lab65" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab66 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief ridge -text processed_date 
    vTcl:DefineAlias "$top.lab66" "Label7" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex67 \
        -background #ffffff -font TkTextFont -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 206 -wrap word 
    $top.tex67 configure -font "TkTextFont"
    $top.tex67 insert end text
    vTcl:DefineAlias "$top.tex67" "Text1" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m68 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background #400040 -font TkMenuFont \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    text $top.tex69 \
        -background white -font TkTextFont -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 206 -wrap word 
    $top.tex69 configure -font "TkTextFont"
    $top.tex69 insert end text
    vTcl:DefineAlias "$top.tex69" "Text2" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex70 \
        -background white -font TkTextFont -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 466 -wrap word 
    $top.tex70 configure -font "TkTextFont"
    $top.tex70 insert end text
    vTcl:DefineAlias "$top.tex70" "Text3" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex71 \
        -background white -font TkTextFont -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 365 -wrap word 
    $top.tex71 configure -font "TkTextFont"
    $top.tex71 insert end text
    vTcl:DefineAlias "$top.tex71" "Text4" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex72 \
        -background white -font TkTextFont -foreground black -height 27 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 421 -wrap word 
    $top.tex72 configure -font "TkTextFont"
    $top.tex72 insert end text
    vTcl:DefineAlias "$top.tex72" "Text5" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex73 \
        -background white -font TkTextFont -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 364 -wrap word 
    $top.tex73 configure -font "TkTextFont"
    $top.tex73 insert end text
    vTcl:DefineAlias "$top.tex73" "Text6" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledwindow::CreateCmd $top.scr74 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 100 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 150 
    vTcl:DefineAlias "$top.scr74" "Scrolledwindow1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr74.01 configure -background white \
        -borderwidth 2 \
        -height 75 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -relief groove \
        -selectbackground blue \
        -selectforeground white \
        -width 125
    label $top.lab75 \
        -activebackground #f9f9f9 -activeforeground black -background #ffff00 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 18 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief groove -text {Image Tags} 
    vTcl:DefineAlias "$top.lab75" "Label8" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab76 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief ridge -text PixelData 
    vTcl:DefineAlias "$top.lab76" "Label9" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex78 \
        -background white -font TkTextFont -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 424 -wrap word 
    $top.tex78 configure -font "TkTextFont"
    $top.tex78 insert end text
    vTcl:DefineAlias "$top.tex78" "Text7" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab80 \
        -activebackground #f9f9f9 -activeforeground black -background #ffff00 \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief ridge -text Comment 
    vTcl:DefineAlias "$top.lab80" "Label10" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr81 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr81" "Scrolledtext1" vTcl:WidgetProc "Toplevel1" 1

    $top.scr81.01 configure -background white \
        -font TkTextFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground blue \
        -selectforeground white \
        -width 10 \
        -wrap none
    button $top.but82 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Save Comment} 
    vTcl:DefineAlias "$top.but82" "Button1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -relief ridge \
        -text {Modification time} 
    vTcl:DefineAlias "$top.lab45" "Label11" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex46 \
        -background white -font TkTextFont -foreground black -height 30 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 244 -wrap word 
    $top.tex46 configure -font "TkTextFont"
    $top.tex46 insert end text
    vTcl:DefineAlias "$top.tex46" "Text8" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -relief ridge -text Modality 
    vTcl:DefineAlias "$top.lab48" "Label12" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex49 \
        -background white -font TkTextFont -foreground black -height 24 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 244 -wrap word 
    $top.tex49 configure -font "TkTextFont"
    $top.tex49 insert end text
    vTcl:DefineAlias "$top.tex49" "Text9" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab58 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.012 -height 0 -relheight 0.07 \
        -anchor nw -bordermode ignore 
    place $top.lab59 \
        -in $top -x 0 -relx 0.027 -y 0 -rely 0.083 -width 0 -relwidth 0.156 \
        -height 0 -relheight 0.034 -anchor nw -bordermode ignore 
    place $top.lab62 \
        -in $top -x 0 -relx 0.026 -y 0 -rely 0.134 -width 0 -relwidth 0.156 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
    place $top.lab63 \
        -in $top -x 0 -relx 0.026 -y 0 -rely 0.184 -width 0 -relwidth 0.153 \
        -height 0 -relheight 0.039 -anchor nw -bordermode ignore 
    place $top.lab64 \
        -in $top -x 0 -relx 0.026 -y 0 -rely 0.235 -width 0 -relwidth 0.153 \
        -height 0 -relheight 0.039 -anchor nw -bordermode ignore 
    place $top.lab65 \
        -in $top -x 0 -relx 0.026 -y 0 -rely 0.285 -width 0 -relwidth 0.152 \
        -height 0 -relheight 0.039 -anchor nw -bordermode ignore 
    place $top.lab66 \
        -in $top -x 0 -relx 0.026 -y 0 -rely 0.335 -width 0 -relwidth 0.153 \
        -height 0 -relheight 0.039 -anchor nw -bordermode ignore 
    place $top.tex67 \
        -in $top -x 0 -relx 0.231 -y 0 -rely 0.077 -width 0 -relwidth 0.238 \
        -height 0 -relheight 0.043 -anchor nw -bordermode ignore 
    place $top.tex69 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.134 -width 0 -relwidth 0.238 \
        -height 0 -relheight 0.043 -anchor nw -bordermode ignore 
    place $top.tex70 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.184 -width 0 -relwidth 0.538 \
        -height 0 -relheight 0.043 -anchor nw -bordermode ignore 
    place $top.tex71 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.235 -width 0 -relwidth 0.539 \
        -height 0 -relheight 0.043 -anchor nw -bordermode ignore 
    place $top.tex72 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.335 -width 0 -relwidth 0.538 \
        -height 0 -relheight 0.045 -anchor nw -bordermode ignore 
    place $top.tex73 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.284 -width 0 -relwidth 0.538 \
        -height 0 -relheight 0.043 -anchor nw -bordermode ignore 
    place $top.scr74 \
        -in $top -x 0 -relx 0.023 -y 0 -rely 0.495 -width 0 -relwidth 0.64 \
        -height 0 -relheight 0.462 -anchor nw -bordermode ignore 
    place $top.lab75 \
        -in $top -x 0 -relx 0.023 -y 0 -rely 0.433 -width 0 -relwidth 0.639 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.lab76 \
        -in $top -x 0 -relx 0.026 -y 0 -rely 0.385 -width 0 -relwidth 0.147 \
        -height 0 -relheight 0.035 -anchor nw -bordermode ignore 
    place $top.tex78 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.385 -width 0 -relwidth 0.542 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
    place $top.lab80 \
        -in $top -x 0 -relx 0.681 -y 0 -rely 0.433 -width 0 -relwidth 0.304 \
        -height 0 -relheight 0.048 -anchor nw -bordermode ignore 
    place $top.scr81 \
        -in $top -x 0 -relx 0.681 -y 0 -rely 0.495 -width 0 -relwidth 0.306 \
        -height 0 -relheight 0.442 -anchor nw -bordermode ignore 
    place $top.but82 \
        -in $top -x 0 -relx 0.855 -y 0 -rely 0.943 -width 107 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 0 -relx 0.485 -y 0 -rely 0.077 -width 0 -relwidth 0.164 \
        -height 0 -relheight 0.048 -anchor nw -bordermode ignore 
    place $top.tex46 \
        -in $top -x 0 -relx 0.67 -y 0 -rely 0.077 -width 0 -relwidth 0.282 \
        -height 0 -relheight 0.046 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.485 -y 0 -rely 0.139 -width 0 -relwidth 0.166 \
        -height 0 -relheight 0.032 -anchor nw -bordermode ignore 
    place $top.tex49 \
        -in $top -x 0 -relx 0.67 -y 0 -rely 0.139 -width 0 -relwidth 0.282 \
        -height 0 -relheight 0.037 -anchor nw -bordermode ignore 
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
Window show .top57 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

