""" Para guardar los paths principales del proyecto.
TODO: Poner en singleton o una forma de acceder a estos paths directamente.

- IMPORTANTE: El proyecto debe ser clonado dentro de ~/.config.
"""
from pathlib import Path

from typing import List

path_home = Path.home()
path_root = path_home / ".config" / "qtile"
path_themes_folder = path_root / "themes"

path_tmp = path_root / ".tmp"
path_images = path_home / "images"
path_screenshots = path_images / "screenshots"
path_wallpapers = path_images / "wallpapers"


# TODO: paths_commands: List[Path], estaría bueno para
# tener un conjunto de comandos de distintos proyectos
# y tenerlos accesibles desde acá, ver como se puede hacer
# algo con el .bashrc o zsh


# Crear los folders en caso de haberse borrado.
path_themes_folder.mkdir(exist_ok=True)
path_tmp.mkdir(exist_ok=True)
path_images.mkdir(exist_ok=True)
path_screenshots.mkdir(exist_ok=True)
path_wallpapers.mkdir(exist_ok=True)



