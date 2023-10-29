from pydantic import BaseModel

class ConfigScreen(BaseModel):
    wallpaper_mode: str     # TODO: Ver cuales son las opciones.
    x11_drag_polling_rate: int
    #wallpaper_mode = 'fill',
    # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
    # By default we handle these events delayed to already improve performance, however your system might still be struggling
    # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
    #x11_drag_polling_rate = 60


class ConfigBar(BaseModel):
    background: str
    size: int
    border_width: list[int]

class ConfigGroupBox(BaseModel):
    active: str
    inactive: str
    margin_y: int
    margin_x: int
    borderwidth: int
    highlight_method: str

#class FontConfig(BaseModel):
#    font: str = "HackNerdFont"
#    fontsize: int = 14
#    padding: int = 10





class ConfigQTILE(BaseModel):
    bar: ConfigBar
    screen: ConfigScreen
    groupbox: ConfigGroupBox
    
    # def load_theme():
    #     pass
    # def save_theme():
    #     pass