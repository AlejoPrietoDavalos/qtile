from libqtile.config import Group

from typing import List

def get_groups(desktops: List[List[str]]) -> List[Group]:
    groups: List[Group] = []
    for desktop in desktops:
        for i in desktop:
            groups.append(Group(i))
    return groups