from libqtile import widget, bar
from libqtile.config import Screen

from pathlib import Path


def get_widgets():
    return [
        #widget.CurrentLayout(),
        #widget.Prompt(),
        widget.WindowName(),
        widget.GroupBox(),
        #widget.Chord(
        #    chords_colors = {"launch": ("#ff0000", "#ffffff")},
        #    name_transform = lambda name: name.upper(),
        #),
        widget.Sep(),
        #widget.TextBox("default config", name="default"),
        #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        #widget.StatusNotifier(),
        #widget.Systray(),
        #widget.QuickExit(),
        widget.Clock(format="%d/%m/%Y | %I:%M %p"),
    ]


def get_screen(my_widgets, n_img) -> Screen:
    return Screen(
        top = bar.Bar(
            my_widgets,
            size = 24,
            border_width = [2, 0, 2, 0],  # Draw top and bottom borders
            #border_color = ["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        wallpaper = str(Path.home() / "images" / "wallpapers" / f"{n_img}.png"),
        wallpaper_mode = 'fill',
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        x11_drag_polling_rate = 60
    )
