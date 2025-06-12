




define audio.VirulentSnow = "<loop 0>audio/music/VirulentSnow.ogg"
define audio.ArtificialAntartica = "<loop 0>audio/music/ArtificialAntartica.ogg"
define audio.FrozenFuchsia = "<loop 0>audio/music/FrozenFuchsia.ogg"
define audio.goodbye = "<loop 0>audio/music/Good Bye, and Good Night.mp3"
define audio.ending = "<loop 0>audio/music/Orange Citizen ending.mp3"



image house = "images/house.png"
image field = "images/field.png"
image facility = "images/blocks.png"
image infacility = "images/science.png"
image crystals = "images/crystal.png"
image fhouse = "images/house2.png"
image door = "images/door.png"

image cg1 = "images/cg1.png"
image cg2 = "images/cg2.png"
image cg3 = "images/cg3.png"
image cg4 = "images/cg4.png"


image black = "#000000"
image dark = "#000000e4"
image white = "#ffffff"

define flashflash = Fade(0.0166, 0.5, 1.0166, color="#fff")
define flash = Fade(2.0, 4.0, 2.0, color="#fff")
define longflash = Fade(3.0, 1.0, 3.0, color="#fff")


define dissolve_scene_full = MultipleTransition([
    False, Dissolve(5.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])



define dissolve_scene_half = MultipleTransition([
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])


define close_eyes = MultipleTransition([
    False, Dissolve(0.5),
    Solid("#000"), Pause(0.25),
    True])


define open_eyes = MultipleTransition([
    False, Dissolve(0.5),
    True])


define trueblack = MultipleTransition([
    Solid("#000"), Pause(0.25),
    Solid("#000")
    ])




transform tcommon(x=0, z=1.20):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom z*0.95 alpha 0.00
        xcenter x yoffset 140
        easein .25 yoffset 160 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 160 ypos 1.03


transform t41:
    tcommon(400)
transform t42:
    tcommon(700)
transform t43:
    tcommon(1100)
transform t44:
    tcommon(1500)
transform t31:
    tcommon(440)
transform t32:
    tcommon(940)
transform t33:
    tcommon(1440)
transform t21:
    tcommon(600)
transform t22:
    tcommon(1280)
transform t11:
    tcommon(940)



transform tsitting(x=0, z=1.00):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.00
        zoom z*1 alpha 0.00
        xcenter x yoffset 60
        easein 1.25 yoffset 60 zoom z*1.00 alpha 1.00
    on replace:

        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 60 ypos 1.00



transform s43:
    tsitting(1170)






define Sanna = Character("Sanna", image="sanna", what_prefix='"', what_suffix='"', color="#e2eae9")
define Freya = Character("Freya", image="freya", what_prefix='"', what_suffix='"', color="#8cb283")
define sn = nvl_narrator

transform resize_sprite:
    zoom 0.2


image title = "images/title_screen.mkv"








init -1:
    $ redefine_resources = False







init -1 python:

    if redefine_resources:
        with open(renpy.loader.transfn('definitions.rpy'), 'rb') as f:
            s = f.read()
        f.closed
        pos = s.find('## Script to redefine the images')
        if pos>1:
            s=s[pos:]
        
        with open(renpy.loader.transfn('definitions.rpy'), 'wb') as f:
            f.write('## This is a resource name loader that will import the names of files from certain folders\n## Intended as a way to quickly grab file names to use in accessibility.rpy, screens.rpy, and captiontool.rpy\n## Remember to add commas to the end of each listed item\n## As of RenPy7, basic images do not have to be defined (LayeredImages still need to be set up)\r\ninit -1:\r\n    $ redefine_resources = False\n    ## When you add, delete or rename an image or music resource, change redefine_resources to True and launch the project\r\n\r\n')
            
            f.write('## Sprites:\r\n')
            for file in renpy.list_files():
                if file.startswith('images/sprites') and (file.endswith('.png') or file.endswith('.webp')):
                    name = file.replace('images/sprites/','').replace('/', ' ').replace('.png','').replace('.webp','')
                    img_str = 'image ' + name + ' = "' + file + '"'
                    f.write('    # ' + img_str + '\r\n')
            
            f.write('## BGs:\r\n')
            for file in renpy.list_files():
                if file.startswith('images/BG/') and (file.endswith('.png') or file.endswith('.webp') or file.endswith('.jpg')):
                    name = file.replace('images/BG/','').replace('/', ' ').replace('.png','').replace('.webp','').replace('.jpg','')
                    img_str = 'image ' + name + ' = "' + file + '"'
                    f.write('    # ' + img_str + '\r\n')
            
            f.write('## CGs:\r\n')
            for file in renpy.list_files():
                if file.startswith('images/CG/') and (file.endswith('.png') or file.endswith('.webp') or file.endswith('.jpg')):
                    name = file.replace('images/CG/','').replace('/', ' ').replace('.png','').replace('.webp','').replace('.jpg','')
                    img_str = 'image ' + name + ' = "' + file + '"'
                    f.write('    # ' + img_str + '\r\n')
            
            f.write('\r\n## Music:\r\n# init -2 python:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/music/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/music/','').replace('/', ' ').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + my_str + '\r\n')
            
            f.write('\r\n## Music Caption:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/music/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/music/','').replace('/', ' ').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + name + ': _("")' + '\r\n')
            
            f.write('\r\n## SFX:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/sfx/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/sfx/','').replace('/', ' ').replace(' ', '_').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + my_str + '\r\n')
            
            f.write('\r\n## SFX Caption:\r\n')
            for file in renpy.list_files():
                if file.startswith('audio/sfx/') and (file.endswith('.ogg') or file.endswith('.wav') or file.endswith('.mp3')):
                    name = file.replace('audio/sfx/','').replace('/', ' ').replace(' ', '_').replace('.ogg','').replace('.wav','').replace('.mp3','')
                    my_str = name + ' = "' + file + '"'
                    f.write('    # ' + name + ': _("")' + '\r\n')
            f.write('\r\n')
        f.closed
        
        with open(renpy.loader.transfn('definitions.rpy'), 'ab') as f:
            f.write(s)
        f.closed
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
