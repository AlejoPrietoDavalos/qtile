from libqtile import widget, hook
# Esto esta en `from libqtile.qtile import qtile`,
# pero no se si es el mismo.
from libqtile.qtile import qtile

def update_groupbox():
    for group in qtile.groups:
        if any(w.name == "code" for w in group.windows):
            group.label = "🐍"  # Cambia esto por el logo de Python que quieres usar
        else:
            group.label = group.name  # Restablece el label original del grupo

@hook.subscribe.client_new
def on_client_new(client):
    update_groupbox()

@hook.subscribe.client_killed
def on_client_killed(client):
    update_groupbox()

def get_widgets():
    return [
        # ...
        widget.GroupBox(
            # ...
        ),
        # ...
    ]
