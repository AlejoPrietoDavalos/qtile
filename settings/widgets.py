from settings.config_qtile import ConfigQTILE
from settings.colors import ColorBar    # FIXME

from libqtile import bar, widget

def format_clock(format: str = None) -> str:
    return "%d/%m/%Y | %H:%M" if format is None else format

def get_widgets(cfg: ConfigQTILE):
    widgets = []
    widgets.extend([
        widget.Spacer(length=bar.STRETCH),
        widget.GroupBox(**cfg.groupbox.model_dump(), **cfg.font.model_dump()),
        widget.Spacer(length=bar.STRETCH),
    ])
    widgets.extend([
        widget.Clock(format=format_clock(), foreground=ColorBar.letter_normal, **cfg.font.model_dump())
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