from libqtile import bar
from libqtile.config import Screen

from pydantic import BaseModel

from typing import List


#class FontConfig(BaseModel):
#    font: str = "HackNerdFont"
#    fontsize: int = 14
#    padding: int = 10

class ConfigScreen(BaseModel):
    wallpaper_mode: str     # TODO: Ver cuales son las opciones.
    x11_drag_polling_rate: int

class ConfigBar(BaseModel):
    size: int
    border_width: list[int]




from pathlib import Path

def get_screen(widgets, cfg_screen: ConfigScreen, cfg_bar: ConfigBar) -> Screen:
    return Screen(
        top = bar.Bar(widgets, **cfg_bar.model_dump()),
        **cfg_screen.model_dump(),
        # FIXME: Sacar el wallpaper para afuera, y hacerlo con feh.
        wallpaper = str(Path.home() / "images" / "wallpapers" / f"0.png")
        
        
        #wallpaper_mode = 'fill',
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        #x11_drag_polling_rate = 60
    )
