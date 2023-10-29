from libqtile.config import Group

from typing import List

def get_groups(desktops: List[List[str]]) -> List[Group]:
    groups: List[Group] = []
    for n_screen, desktop in enumerate(desktops):
        for i in desktop:
            group = Group(i)#, screen_affinity=n_screen)
            groups.append(group)
    return groups