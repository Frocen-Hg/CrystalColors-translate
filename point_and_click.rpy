
default room = None
default research_facility = ['piece_of_paper']
default inside_sannas_house = ['book', 'framed_picture', 'plushie']
default outside_freyas_house = ['key']
default description = None

init -1 python:
    class ToolTip(renpy.Displayable):
        def __init__(self):
            super(ToolTip, self).__init__()
            self.child = None
            self.pos = (-1, -1)
        
        def render(self, width, height, st, at):
            render = renpy.Render(config.screen_width, config.screen_height)
            if self.pos != (-1, -1) and self.child:
                child_render = renpy.render(self.child, width, height, st, at)
                tool_tip_width, tool_tip_height = child_render.get_size()
                x, y = self.pos
                x -= tool_tip_width/2
                y -= tool_tip_height/2-35
                render.blit(child_render, (x, y))
            return render
        
        def event(self, ev, x, y, st):
            if self.pos != (x, y):
                renpy.redraw(self, 0)
            self.pos = (x, y)
        
        def visit(self):
            return [ self.child ]

label evaluate_scene(screen, tag):
    $ items = getattr(store, screen, None)
    if tag in items:
        $ setattr(store, screen, [i for i in items if i != tag])
    if getattr(store, screen, None):
        call expression "_".join(["pnc", screen]) from _call_expression
    else:
        call expression "_".join(["pnc", screen, "end"]) from _call_expression_1
    return

default tool_tip = ToolTip()
screen interaction_point(tag, screen, interactable=False):
    imagebutton auto "_".join([tag, "%s"]) focus_mask True:
        if interactable:
            action [SetField(tool_tip, "child", None), Call("execute_scene", screen, tag)]
            alternate SetField(tool_tip, "child", None)
            hovered SetField(tool_tip, "child", Text(tag.replace("_", " "),
                                                       anchor=(0.5, 0.5),
                                                       color='#FFF',
                                                       outlines=[(absolute(4), '#000', absolute(0), absolute(0))]))
            unhovered SetField(tool_tip, "child", None)

label execute_scene(screen, tag):
    $ renpy.show_screen(screen)
    call expression "_".join(["pnc", tag]) from _call_expression_2
    call evaluate_scene (screen, tag) from _call_evaluate_scene
    return

screen research_facility(interactable=False):
    add "bg research_facility"
    use interaction_point('piece_of_paper', screen="research_facility", interactable=interactable)
    add tool_tip

screen inside_sannas_house(interactable=False):
    add "bg inside_sannas_house"
    use interaction_point('book', screen="inside_sannas_house", interactable=interactable)
    use interaction_point('plushie', screen="inside_sannas_house", interactable=interactable)
    use interaction_point('framed_picture', screen="inside_sannas_house", interactable=interactable)
    add tool_tip

screen outside_freyas_house(interactable=False):
    add "bg outside_freyas_house"
    use interaction_point('key', screen="outside_freyas_house", interactable=interactable)
    add tool_tip
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
