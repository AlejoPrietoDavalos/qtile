from libqtile import layout
from libqtile.config import Click, Drag, Match
from libqtile.lazy import lazy


from buttons import *
from shortcuts import get_keys
from screens import get_widgets, get_screen
from layouts import get_layouts
from groups import get_groups
import os

from libqtile import hook




os.system("xrandr --output DP-5 --right-of HDMI-0")


desktops = [
    ["1", "2", "3", "4", "5"],
    ["6", "7", "8", "9", "0"]
]

groups = get_groups(desktops)

















keys = get_keys(groups)

layouts = get_layouts()

widget_defaults = dict(
    font = "Hack Nerd Font",
    fontsize = 12,
    padding = 10,
)
extension_defaults = widget_defaults.copy()

my_widgets_1 = get_widgets()
my_widgets_2 = get_widgets()

s_1, s_2 = get_screen(my_widgets_1, 0), get_screen(my_widgets_2, 1)
screens = [s_2, s_1]


# Drag floating layouts.
mouse = [
    Drag([SUPER], BUTTON_1, lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([SUPER], BUTTON_3, lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([SUPER], BUTTON_2, lazy.window.bring_to_front()),
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
floats_kept_above = True        # Si es True, las ventanas flotantes se mantendrán por encima de otras ventanas. Si es False, no se garantiza su posición.

cursor_warp = False
floating_layout = layout.Floating(
    float_rules = [
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"





import random
import os
from pathlib import Path
def set_wallpaper() -> None:
    """ BUG: Se ejecuta 2 veces."""
    path_home = Path.home()
    path_images = path_home / "images"
    path_wallpapers = path_images / "wallpapers"
    asd = [p for p in path_wallpapers.iterdir()]
    
    r = random.choice(asd)
    os.system(f"feh --bg-fill {random.choice(asd)}")
#set_wallpaper()
path_home = Path.home()
path_images = path_home / "images"
path_wallpapers = path_images / "wallpapers"
asd = [p for p in path_wallpapers.iterdir()]

r = random.choice(asd)
#os.system(f"feh --bg-fill {random.choice(asd)}")