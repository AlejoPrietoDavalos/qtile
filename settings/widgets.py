from settings.config_qtile import ConfigQTILE

from libqtile import bar
from qtile_extras import widget

#from qtile_extras.widget.decorations import PowerLineDecoration, BorderDecoration



# TODO: Mejorar, estos serían los widgets clickeables.
from qtile_extras.widget.decorations import RectDecoration
rect_decoration = {
    "decorations": [
        RectDecoration(colour="#197398", radius=10, filled=True, padding_y=4, group=True)
    ]
}


#powerline = {
#    "decorations": [
#        #BorderDecoration(),
#        RectDecoration(colour="#197398", radius=10, filled=True, padding_y=4, group=True),
#        #PowerLineDecoration(path="arrow_right")
#    ]
#}



# ----> TODO: Definir una clase estática que se encargue de
# generar los distintos widgets, haciendo uso del ConfigQTILE.


def get_widgets(cfg: ConfigQTILE):
    widgets = []
    widgets.extend([
        widget.Spacer(length=bar.STRETCH),
        widget.GroupBox(**cfg.groupbox.model_dump(), **cfg.font.model_dump()),
        widget.Spacer(length=bar.STRETCH)
    ])
    widgets.extend([
        widget.Clock(
            **cfg.clock.model_dump(),
            **cfg.font.model_dump(),
            **rect_decoration
        )
    ])

    widgets.extend([
        #widget.CurrentLayout(),
        #widget.Prompt(),
        #widget.WindowName(),
        #widget.Chord(
        #    chords_colors = {"launch": ("#ff0000", "#ffffff")},
        #    name_transform = lambda name: name.upper(),
        #),
        #widget.Sep(),
        #widget.TextBox("default config", name="default"),
        #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        #widget.StatusNotifier(),
        #widget.Systray(),
        #widget.QuickExit(),
        #widget.Battery(), # TODO: Para notebook.
    ])
    return widgets