from settings.buttons import *
from settings.programs import Programs
from settings._paths import path_root

from libqtile.lazy import lazy
from libqtile.config import Key, Group

from typing import List, NewType

Keys = NewType("keys", List[Key])
Groups = NewType("groups", List[Group])
import time


def KP_num(num: str) -> str:
    return f"KP_{num}"

#"   ", "   ", "   ", "  "
def focus_window_with_nums(name: str, n_desktop: str) -> Keys:
    n_screen = 0 if n_desktop in '12345' else 1
    return [
        Key([SUPER], name, lazy.group[n_desktop].toscreen(n_screen)),
        #Key([SUPER], name, lazy.to_screen(n_screen), lazy.group[n_desktop].toscreen()),
        Key([SUPER, SHIFT], name,
            #lazy.to_screen(n_screen),
            lazy.window.togroup(n_desktop, switch_group=True),
            #lazy.group[n_desktop].toscreen()
            #lazy.window.focus()
        ),
        Key([SUPER, CTRL, SHIFT], name, lazy.window.togroup(n_desktop))
    ]

def focus_window_with_arrows() -> Keys:
    return [
        Key([SUPER], LEFT, lazy.layout.left()),
        Key([SUPER], RIGHT, lazy.layout.right()),
        Key([SUPER], DOWN, lazy.layout.down()),
        Key([SUPER], UP, lazy.layout.up()),
        #Key([SUPER], SPACE, lazy.layout.next(), desc="Move window focus to other window"),
    ]


def screenshot_keys() -> Keys:
    return [
        Key([], "Print", lazy.spawn(f"python3 {path_root / 'wm_screenshot.py'}"))
    ]


def flip_window() -> Keys:
    """ FIXME: No quiero que cambie la forma de la ventana."""
    return [
        Key([SUPER, CTRL], LEFT, lazy.layout.shuffle_left()),
        Key([SUPER, CTRL], RIGHT, lazy.layout.shuffle_right()),
        Key([SUPER, CTRL], DOWN, lazy.layout.shuffle_down()),
        Key([SUPER, CTRL], UP, lazy.layout.shuffle_up())
    ]


def resize_window() -> Keys:
    return [
        Key([SUPER, ALT], LEFT,  lazy.layout.grow_left()),
        Key([SUPER, ALT], RIGHT, lazy.layout.grow_right()),
        Key([SUPER, ALT], DOWN,  lazy.layout.grow_down()),
        Key([SUPER, ALT], UP,    lazy.layout.grow_up()),
        Key([SUPER], K_n, lazy.layout.normalize())
    ]

def run_programs(programs: Programs) -> Keys:
    """ TODO: Algunos condicionales, quizás un programa puede ser un objeto de pydantic
    que guarde además el nombre, como ejecutarlo y el shotcut que tiene asociado."""
    return [
        Key([SUPER], RETURN, lazy.spawn(programs.terminal)),
        Key([SUPER, CTRL], RETURN, lazy.spawn(programs.browser)),
        Key([SUPER, CTRL, SHIFT], RETURN, lazy.spawn(programs.browser_incognito)),
        Key([SUPER], K_d, lazy.spawn(programs.run_program))
    ]


def get_keys(groups: Groups, programs: Programs) -> Keys:
    """ A list of available commands that can be bound to keys can be found
    at https://docs.qtile.org/en/latest/manual/config/lazy.html
    Switch between windows
    """
    keys: Keys = []
    keys.extend(screenshot_keys())
    #keys.extend([Key([SUPER], KP_num("7"), lazy.group["7"].toscreen(1))])
    keys.extend(focus_window_with_arrows())
    for g in groups:
        keys.extend(focus_window_with_nums(g.name, g.name))
    #keys.extend(FocusWindow.with_num(KP_num(g.name), g.name) for g in groups)
    keys.extend(flip_window())
    keys.extend(resize_window())
    keys.extend(run_programs(programs))
    keys.extend([
        # Toggle between different layouts as defined below
        #Key([SUPER], TAB, lazy.next_layout()),     # No sé que hace.
        Key([SUPER], K_w, lazy.window.kill()),                  # Kill window.
        Key([SUPER], K_f, lazy.window.toggle_fullscreen()),     # Fullscreen.
        #Key([SUPER], K_t, lazy.window.toggle_floating()),
        Key([SUPER, ALT], K_r, lazy.reload_config()),           # Reload config.
        Key([SUPER, CTRL], K_q, lazy.shutdown()),
        Key([SUPER], K_r, lazy.spawncmd()),     # TODO: Ver como visualizarlo.
    ])
    return keys
