from keys import *

from libqtile.lazy import lazy
from libqtile.config import Key
from programs import terminal

from typing import List

# Run apps.
#shortcuts.extend([
#    Key([SUPER, CTRL], RETURN, lazy.spawn("brave"))
#])


shortcuts: List[Key] = []
shortcuts.extend([
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([SUPER], LEFT, lazy.layout.left(), desc="Move focus to left"),      # FIXME: Regla, si no hay nada de ese lado, que no intente cambiar el focus.
    Key([SUPER], RIGHT, lazy.layout.right(), desc="Move focus to right"),   # FIXME: Regla, si no hay nada de ese lado, que no intente cambiar el focus.
    Key([SUPER], DOWN, lazy.layout.down(), desc="Move focus down"),         # FIXME: Regla, si no hay nada de ese lado, que no intente cambiar el focus.
    Key([SUPER], UP, lazy.layout.up(), desc="Move focus up"),               # FIXME: Regla, si no hay nada de ese lado, que no intente cambiar el focus.
    Key([SUPER], SPACE, lazy.layout.next(), desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([SUPER, SHIFT], LEFT, lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([SUPER, SHIFT], RIGHT, lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([SUPER, SHIFT], DOWN, lazy.layout.shuffle_down(), desc="Move window down"),
    Key([SUPER, SHIFT], UP, lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([SUPER, ALT], LEFT, lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([SUPER, ALT], RIGHT, lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([SUPER, ALT], DOWN, lazy.layout.grow_down(), desc="Grow window down"),
    Key([SUPER, ALT], UP, lazy.layout.grow_up(), desc="Grow window up"),
    Key([SUPER], K_n, lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([SUPER, SHIFT], RETURN, lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack",),
    Key([SUPER], RETURN, lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([SUPER], TAB, lazy.next_layout(), desc="Toggle between layouts"),
    Key([SUPER], K_w, lazy.window.kill(), desc="Kill focused window"),
    Key(
        [SUPER],
        K_f,
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([SUPER], K_t, lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([SUPER, CTRL], K_r, lazy.reload_config(), desc="Reload the config"),
    Key([SUPER, CTRL], K_q, lazy.shutdown(), desc="Shutdown Qtile"),
    Key([SUPER], K_r, lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
])