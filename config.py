from libqtile import layout
from libqtile.config import Click, Drag, Match
from libqtile.lazy import lazy

import os

from settings.config_qtile import ConfigQTILE, ConfigFont
from settings.buttons import *
from settings.shortcuts import get_keys
from settings.widgets import get_widgets
from settings.screens import get_screen
from settings.layouts import get_layouts
from settings.groups import get_groups
from settings.wallpaper import WallpaperManager


# Ver `theme_creator.ipynb`.
cfg = ConfigQTILE.load_theme(theme_name="azulado")



# FIXME: Arreglar este hardcoding.
os.system("xrandr --output DP-5 --right-of HDMI-0")
wallpaper = WallpaperManager()
wallpaper.set_random_wall()

desktops = [
    ["1", "2", "3", "4", "5"],
    ["6", "7", "8", "9", "0"]
]

groups = get_groups(desktops)




from libqtile.utils import guess_terminal
from settings.programs import Programs
# TODO: Meter esto dentro del config.
programs = Programs(
    terminal = guess_terminal(),
    browser = "brave",
    browser_incognito = "brave --incognito"
)










keys = get_keys(groups, programs)

layouts = get_layouts()


cfg_font = ConfigFont(
    font = "HackNerdFont bold",
    fontsize = 15,
    padding = 10
)
extension_defaults = cfg_font.model_dump()





n_monitors = 2  # TODO: Ver como mejorar esto.
widgets = [get_widgets(cfg) for _ in range(n_monitors)]
screens = [get_screen(w, cfg) for w in widgets]














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





#import random
#import os
#from pathlib import Path
#def set_wallpaper() -> None:
#    """ BUG: Se ejecuta 2 veces."""
#    path_home = Path.home()
#    path_images = path_home / "images"
#    path_wallpapers = path_images / "wallpapers"
#    asd = [p for p in path_wallpapers.iterdir()]
#    
#    r = random.choice(asd)
#    os.system(f"feh --bg-fill {random.choice(asd)}")
#set_wallpaper()
#path_home = Path.home()
#path_images = path_home / "images"
#path_wallpapers = path_images / "wallpapers"
#asd = [p for p in path_wallpapers.iterdir()]

#r = random.choice(asd)
#os.system(f"feh --bg-fill {random.choice(asd)}")
