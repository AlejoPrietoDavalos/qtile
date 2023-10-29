""" Para guardar los paths principales del proyecto."""
from pathlib import Path

path_root = Path.home() / ".config" / "qtile"
path_themes_folder = Path("themes")

# Crear los folders en caso de haberse borrado.
for _p in [path_themes_folder]:
    _p.mkdir(exist_ok=True)


def get_path_theme(theme_name: str) -> Path:
    # Hacer validacion del path y toda la pelota.
    return path_themes_folder / f"{theme_name}.json"