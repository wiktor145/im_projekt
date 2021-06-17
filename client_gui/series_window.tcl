#############################################################################
# Generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#  Jun 17, 2021 07:14:27 PM CEST  platform: Windows NT
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
        -menu "$top.m68" -background #f2f2f2 
    wm focusmodel $top passive
    wm geometry $top 782x597+363+108
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
        -background #0080c0 -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -text Series 
    vTcl:DefineAlias "$top.lab58" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab59 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -relief ridge -text series_id 
    vTcl:DefineAlias "$top.lab59" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab62 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -relief ridge \
        -text SeriesInstanceUID 
    vTcl:DefineAlias "$top.lab62" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab63 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -relief ridge -text study_id 
    vTcl:DefineAlias "$top.lab63" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab64 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -relief ridge -text SeriesDate 
    vTcl:DefineAlias "$top.lab64" "Label5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab65 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -relief ridge \
        -text SeriesDescription 
    vTcl:DefineAlias "$top.lab65" "Label6" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab66 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -relief ridge -text SeriesNumber 
    vTcl:DefineAlias "$top.lab66" "Label7" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex67 \
        -background #ffffff -font TkTextFont -foreground black -height 24 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 364 -wrap word 
    $top.tex67 configure -font "TkTextFont"
    $top.tex67 insert end text
    vTcl:DefineAlias "$top.tex67" "Text1" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m68 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background #400040 -font TkMenuFont \
        -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    text $top.tex69 \
        -background white -font TkTextFont -foreground black -height 24 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 364 -wrap word 
    $top.tex69 configure -font "TkTextFont"
    $top.tex69 insert end text
    vTcl:DefineAlias "$top.tex69" "Text2" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex70 \
        -background white -font TkTextFont -foreground black -height 24 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 364 -wrap word 
    $top.tex70 configure -font "TkTextFont"
    $top.tex70 insert end text
    vTcl:DefineAlias "$top.tex70" "Text3" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex71 \
        -background white -font TkTextFont -foreground black -height 24 \
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
        -background white -font TkTextFont -foreground black -height 24 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 364 -wrap word 
    $top.tex73 configure -font "TkTextFont"
    $top.tex73 insert end text
    vTcl:DefineAlias "$top.tex73" "Text6" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledwindow::CreateCmd $top.scr74 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 247 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 708 
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
        -background #ffff00 -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 18 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) -relief groove -text {Series Images} 
    vTcl:DefineAlias "$top.lab75" "Label8" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab76 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) -relief ridge -text SeriesTime 
    vTcl:DefineAlias "$top.lab76" "Label9" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex78 \
        -background white -font TkTextFont -foreground black -height 24 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 424 -wrap word 
    $top.tex78 configure -font "TkTextFont"
    $top.tex78 insert end text
    vTcl:DefineAlias "$top.tex78" "Text7" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab58 \
        -in $top -x 0 -y 0 -width 0 -relwidth 1.012 -height 0 -relheight 0.07 \
        -anchor nw -bordermode ignore 
    place $top.lab59 \
        -in $top -x 0 -relx 0.026 -y 0 -rely 0.084 -width 0 -relwidth 0.156 \
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
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.084 -width 0 -relwidth 0.538 \
        -height 0 -relheight 0.044 -anchor nw -bordermode ignore 
    place $top.tex69 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.134 -width 0 -relwidth 0.538 \
        -height 0 -relheight 0.044 -anchor nw -bordermode ignore 
    place $top.tex70 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.184 -width 0 -relwidth 0.538 \
        -height 0 -relheight 0.044 -anchor nw -bordermode ignore 
    place $top.tex71 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.235 -width 0 -relwidth 0.54 \
        -height 0 -relheight 0.044 -anchor nw -bordermode ignore 
    place $top.tex72 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.335 -width 0 -relwidth 0.538 \
        -height 0 -relheight 0.045 -anchor nw -bordermode ignore 
    place $top.tex73 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.285 -width 0 -relwidth 0.538 \
        -height 0 -relheight 0.044 -anchor nw -bordermode ignore 
    place $top.scr74 \
        -in $top -x 0 -relx 0.051 -y 0 -rely 0.536 -width 0 -relwidth 0.905 \
        -height 0 -relheight 0.414 -anchor nw -bordermode ignore 
    place $top.lab75 \
        -in $top -x 0 -relx 0.051 -y 0 -rely 0.452 -width 0 -relwidth 0.893 \
        -height 0 -relheight 0.072 -anchor nw -bordermode ignore 
    place $top.lab76 \
        -in $top -x 0 -relx 0.026 -y 0 -rely 0.385 -width 0 -relwidth 0.147 \
        -height 0 -relheight 0.035 -anchor nw -bordermode ignore 
    place $top.tex78 \
        -in $top -x 0 -relx 0.23 -y 0 -rely 0.385 -width 0 -relwidth 0.542 \
        -height 0 -relheight 0.04 -anchor nw -bordermode ignore 
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

