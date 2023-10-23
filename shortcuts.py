from buttons import *

from libqtile.lazy import lazy
from libqtile.config import Key, Group
from programs import terminal

from typing import List, NewType

Keys = NewType("keys", List[Key])
Groups = NewType("groups", List[Group])



def KP_num(num: str) -> str:
    return f"KP_{num}"



def focus_window_num(name: str, num: str) -> Keys:
    return [
        # mod1 + letter of group = switch to group
        Key([SUPER], name, lazy.group[num].toscreen(), desc="Switch to group {}".format(num)),
        # mod1 + shift + letter of group = switch to & move focused window to group
        #Key([SUPER, SHIFT], name, lazy.window.togroup(num, switch_group=True), desc="Switch to & move focused window to group {}".format(num)),
        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        #Key([SUPER, SHIFT], name, lazy.window.togroup(num), desc="move focused window to group {}".format(num))
    ]



def focus_window(groups: List[Group]) -> Keys:
    keys = [
        Key([SUPER], LEFT,  lazy.layout.left(), desc="Move focus to left"),
        Key([SUPER], RIGHT, lazy.layout.right(),desc="Move focus to right"),
        Key([SUPER], DOWN,  lazy.layout.down(), desc="Move focus down"),
        Key([SUPER], UP,    lazy.layout.up(),   desc="Move focus up"),
        #Key([SUPER], SPACE, lazy.layout.next(), desc="Move window focus to other window"),
    ]

    for group in groups:
        i = group.name
        KP_i = KP_num(i)

        keys.extend(focus_window_num(i, i))
        #keys.extend(focus_window_num(KP_i, i))
    return keys




def get_keys(groups: Groups) -> Keys:
    """ A list of available commands that can be bound to keys can be found
    at https://docs.qtile.org/en/latest/manual/config/lazy.html
    Switch between windows
    """
    keys: Keys = []
    keys.extend(focus_window(groups))
    keys.extend([
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([SUPER, SHIFT], LEFT,  lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([SUPER, SHIFT], RIGHT, lazy.layout.shuffle_right(),desc="Move window to the right"),
        Key([SUPER, SHIFT], DOWN,  lazy.layout.shuffle_down(), desc="Move window down"),
        Key([SUPER, SHIFT], UP,    lazy.layout.shuffle_up(),   desc="Move window up"),

        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([SUPER, ALT], LEFT,  lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([SUPER, ALT], RIGHT, lazy.layout.grow_right(),desc="Grow window to the right"),
        Key([SUPER, ALT], DOWN,  lazy.layout.grow_down(), desc="Grow window down"),
        Key([SUPER, ALT], UP,    lazy.layout.grow_up(),   desc="Grow window up"),
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
        Key([SUPER], K_f, lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
        Key([SUPER], K_t, lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
        Key([SUPER, CTRL], K_r, lazy.reload_config(), desc="Reload the config"),
        Key([SUPER, CTRL], K_q, lazy.shutdown(), desc="Shutdown Qtile"),
        Key([SUPER], K_r, lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    ])


    
    return keys