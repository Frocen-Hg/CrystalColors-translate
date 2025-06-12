



label pnc_research_facility:
    $ room = "research_facility"
    call screen research_facility(True)
    return

label pnc_inside_sannas_house:
    $ room = "inside_sannas_house"
    call screen inside_sannas_house(True)
    return

label pnc_outside_freyas_house:
    $ room = "outside_freyas_house"
    call screen outside_freyas_house(True)
    return




label pnc_piece_of_paper:
    "Sanna looks at the piece of paper."
    return

label pnc_plushie:
    "Sanna looks at the plushie."
    return

label pnc_framed_picture:
    "Sanna looks at the framed picture."
    return

label pnc_book:
    "Sanna looks at the book."
    return

label pnc_key:
    "Sanna looks at the key."
    return




label pnc_research_facility_end:
    "Here is where I add a jump to return to the normal script."
    return

label pnc_inside_sannas_house_end:
    "Here is where I add a jump to return to the normal script."
    return

label pnc_outside_freyas_house_end:
    "Here is where I add a jump to return to the normal script."
    return


label example_snow:

    call init_snow from _call_init_snow
    "Before using the snow effect you need to call the helper label 'init_snow' which will not do anything visible but will activate the snow screens."
    "Once that is done, start making your scene with snow."

    show bg with dissolve
    "BG first."

    show freya up pout open at left:
        xzoom -1.0
        xoffset 200
        yoffset 300
    show sanna standing squint blush awkward jacket scarf at right:
        xoffset -200
        yoffset 300
    with dissolve
    "Then all of your character sprites."

    call show_snow from _call_show_snow
    with dissolve
    "Then your snow."

    "Then enjoy the snow for a while."

    call hide_snow from _call_hide_snow
    with dissolve
    "While the snow screen is active you can show and hide the effect freely."

    call show_snow from _call_show_snow_1
    with dissolve
    "Like so."

    call hide_snow from _call_hide_snow_1
    with dissolve
    "If you've hidden the snow effect and won't be using the snow effect anymore/for a while, you can free up a bit of the memory used by the snow effect."

    call delete_snow from _call_delete_snow
    "Just use the helper label 'delete_snow'. If you want to use the snow effect you will need to call 'init_snow' again before doing so."

    call init_snow from _call_init_snow_1
    call show_snow from _call_show_snow_2
    with dissolve
    "(Honestly I don't think memory usage will be a big deal for out game, so no need to fret over this, but it's here just in case.)"

    call hide_snow from _call_hide_snow_2
    with dissolve
    call delete_snow from _call_delete_snow_1
    "That's all for the snow effect, let me know if you have any questions."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
