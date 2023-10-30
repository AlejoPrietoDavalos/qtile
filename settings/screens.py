from settings.config_qtile import ConfigQTILE

from libqtile import bar
from libqtile.config import Screen


def get_screen(widgets, cfg: ConfigQTILE) -> Screen:
    return Screen(
        top = bar.Bar(widgets, **cfg.bar.model_dump()),
        **cfg.screen.model_dump()
    )
