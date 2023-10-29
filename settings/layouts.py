from libqtile import layout

def get_layouts():
    return [
        layout.Columns(border_focus="#1F4D62", border_focus_stack="#1F4D62", border_width=2), #[, "#1F4D62"]
        layout.Max(),
        # Try more layouts by unleashing below layouts.
        # layout.Stack(num_stacks=2),
        # layout.Bsp(),
        # layout.Matrix(),
        # layout.MonadTall(),
        # layout.MonadWide(),
        # layout.RatioTile(),
        # layout.Tile(),
        # layout.TreeTab(),
        # layout.VerticalTile(),
        # layout.Zoomy(),
    ]