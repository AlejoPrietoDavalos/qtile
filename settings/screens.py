from settings.config_qtile import ConfigQTILE

from libqtile import bar
from libqtile.config import Screen





from pathlib import Path

def get_screen(widgets, cfg: ConfigQTILE) -> Screen:
    return Screen(
        top = bar.Bar(widgets, **cfg.bar.model_dump()),
        **cfg.screen.model_dump(),
        # FIXME: Sacar el wallpaper para afuera, y hacerlo con feh.
        wallpaper = str(Path.home() / "images" / "wallpapers" / f"0.png")
    )
