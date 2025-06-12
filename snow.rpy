

default preferences.gl_framerate = 300

init python:
    import math
    import random

    def snow_update(flakes, config, st):
        for i in flakes:
            if not getattr(i, 'data', None):
                i.data = [random.randint(config[0]-1, config[0]+1),
                          i.x,
                          random.uniform(0.1, 1.0),
                          random.uniform(config[1]-0.1,config[1]+0.1),
                          i.x]
            i.data[4] -= i.data[0]/2
            if i.y >= 1080:
                i.y = -45
                i.data[4] = i.data[1]
            i.x = i.data[4]+1.5*math.sin(((2*math.pi)/i.data[3])*(st+i.data[2]))
            i.y += i.data[0]
        return .01

image fog = Movie(play="images/snow/fog.mkv", mask="images/snow/fog.mkv")

label init_snow:
    python:
        flakes_1 = []
        flakes_2 = []
        flakes_3 = []
        flakes_4 = []
        flakes_5 = []

        snow_1 = SpriteManager(update=renpy.curry(snow_update)(flakes_1,(36,1.0)))
        snow_2 = SpriteManager(update=renpy.curry(snow_update)(flakes_2,(34,0.6)))
        snow_3 = SpriteManager(update=renpy.curry(snow_update)(flakes_3,(32,0.5)))
        snow_4 = SpriteManager(update=renpy.curry(snow_update)(flakes_4,(26,0.4)))
        snow_5 = SpriteManager(update=renpy.curry(snow_update)(flakes_5,(20,0.2)))

        flake_1 = Image("images/snow/flake_1.png")
        flake_2 = Image("images/snow/flake_2.png")
        flake_3 = Image("images/snow/flake_3.png")
        flake_4 = Image("images/snow/flake_4.png")
        flake_5 = Image("images/snow/flake_5.png")

        for i in range(40*3):
            flakes_1.append(snow_1.create(flake_1))
        for i in range(80*3):
            flakes_2.append(snow_2.create(flake_2))
        for i in range(160*3):
            flakes_3.append(snow_3.create(flake_3))
        for i in range(200*3):
            flakes_4.append(snow_4.create(flake_4))
        for i in range(240*3):
            flakes_5.append(snow_5.create(flake_5))

        for i in flakes_1:
            i.x = renpy.random.randint(-45, 2398)
            i.y = renpy.random.randint(-45, 1078)
        for i in flakes_2:
            i.x = renpy.random.randint(-45, 2398)
            i.y = renpy.random.randint(-45, 1078)
        for i in flakes_3:
            i.x = renpy.random.randint(-45, 2398)
            i.y = renpy.random.randint(-45, 1078)
        for i in flakes_4:
            i.x = renpy.random.randint(-45, 2398)
            i.y = renpy.random.randint(-45, 1078)
        for i in flakes_5:
            i.x = renpy.random.randint(-45, 2398)
            i.y = renpy.random.randint(-45, 1078)

        del flake_1
        del flake_2
        del flake_3
        del flake_4
        del flake_5
        del i
    return

label show_snow:
    show expression snow_5 as snow_5 behind freya, sanna
    show expression snow_4 as snow_4 behind freya, sanna
    show expression snow_3 as snow_3 behind freya, sanna
    show expression snow_2 as snow_2
    show expression snow_1 as snow_1
    show fog
    return

label hide_snow:
    hide snow_5
    hide snow_4
    hide snow_3
    hide snow_2
    hide snow_1
    hide fog
    return

label delete_snow:
    hide snow_1
    hide snow_2
    hide snow_3
    hide snow_4
    hide snow_5
    hide fog
    python:
        del snow_1
        del snow_2
        del snow_3
        del snow_4
        del snow_5
        del flakes_1
        del flakes_2
        del flakes_3
        del flakes_4
        del flakes_5
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
