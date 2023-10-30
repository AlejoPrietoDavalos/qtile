import random
import subprocess
from settings._paths import path_wallpapers
from pathlib import Path
from typing import List


def is_path_wall(path_wall: Path) -> bool:
    """ FIXME: Revisar que el path sea efectivamente una imagen."""
    return True

def assert_path_wall(path_wall: Path) -> None:
    """ Tira ValueError si no es una imagen."""
    if not is_path_wall(path_wall):
        raise ValueError("No es una imagen.")

def command_set_wall(path_wall: Path) -> List[str]:
    """ Settear wallpaper. Comando para ejecutar con subprocess.run()."""
    return ["feh", "--bg-fill", str(path_wall)]

def set_wall(path_wall: Path) -> None:
    """ Settea el wallpaper."""
    assert_path_wall(path_wall)
    subprocess.run(command_set_wall(path_wall))


def get_path_all_walls() -> List[Path]:
    return [p for p in path_wallpapers.iterdir()]

def get_random_wall() -> Path:
    return random.choice(get_path_all_walls())

def set_next_wall() -> None:
    """ TODO"""
    pass

def set_previous_wall() -> None:
    """ TODO"""
    pass


class WallpaperManager:
    """ Si path_active==None, setea uno aleatorio."""
    def __init__(self):
        self._path_active: Path = None
        
    @property
    def path_active(self) -> Path:
        """ Path del wallpaper activo."""
        return self._path_active

    def set_random_wall(self) -> None:
        """ Obtiene un wallpaper aleatorio y lo settea."""
        self.set_wall(get_random_wall())

    def set_next_wall(self) -> None:
        set_next_wall()
    
    def set_previous_wall(self) -> None:
        set_previous_wall()

    def set_wall(self, path_wall: Path) -> None:
        """ Settea el wallpaper."""
        self._path_active = path_wall
        set_wall(self.path_active)