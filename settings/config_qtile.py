from __future__ import annotations

from settings._paths import path_themes_folder

from pathlib import Path
from pydantic import BaseModel
import json


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

class ConfigFont(BaseModel):
    font: str
    fontsize: int
    padding: int




def get_path_theme(theme_name: str) -> Path:
    """ FIXME: Hacer validacion del path y toda la pelota.
    Arreglar el hardcodeo del .json"""
    return path_themes_folder / f"{theme_name}.json"

class _ConfigTheme(BaseModel):
    theme_name: str

    @property
    def path_theme(self) -> Path:
        # FIXME: Ver la mejor forma de validar esto.
        return get_path_theme(self.theme_name)

    @staticmethod
    def load_theme(theme_name: str) -> ConfigQTILE:
        path_theme = get_path_theme(theme_name)
        with open(path_theme, "r") as f:
            return ConfigQTILE(**json.load(f))

    def save_theme(self) -> None:
        # TODO: Si existe preguntar si se quiere reemplazar. force=True
        with open(self.path_theme, "w") as f:
            json.dump(self.model_dump(), f)


class ConfigQTILE(_ConfigTheme):
    bar: ConfigBar
    screen: ConfigScreen
    groupbox: ConfigGroupBox

