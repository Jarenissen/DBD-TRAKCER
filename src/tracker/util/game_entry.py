from tracker.util.database import Database
from generated.enums.killers import Killer
from generated.enums.survivors import Survivor
from generated.enums.maps import Map

class IncompleteEntry(Exception):
    pass

class GameEntry:
    def __init__(self):
        self.survivor = Survivor.NotSelected
        self.killer = Killer.NotSelected
        self.mapvariation = Map.NotSelected
        self.victory = None
        self.pip = None
        

    def is_complete(self):
        return bool((self.survivor is not Survivor.NotSelected) and
                    (self.killer is not Killer.NotSelected) and
                    (self.mapvariation is not Map.NotSelected) and
                    self.victory and self.pip)

class GameEntryManager:
    _entry = GameEntry()
    _hook = None

    def set_callback(func):
        GameEntryManager._hook = func

    def call_hook(*params):
        GameEntryManager._hook(*params)

    def set_survivor(survivor):
        GameEntryManager._entry.survivor = survivor
        GameEntryManager.call_hook()

    def set_killer(killer):
        GameEntryManager._entry.killer = killer
        GameEntryManager.call_hook()

    

    def set_victory(victory):
        GameEntryManager._entry.victory = victory
        GameEntryManager.call_hook()

    def set_pips(pip):
        GameEntryManager._entry.pip = pip
        GameEntryManager.call_hook()


    def set_mapvariation(mapvariation):
        GameEntryManager._entry.mapvariation = mapvariation
        GameEntryManager.call_hook()

    def set_mapvariationautohaven(mapvariationautohaven):
        GameEntryManager._entry.mapvariation = mapvariationautohaven
        GameEntryManager.call_hook()

        

    def save():
        if GameEntryManager._entry.is_complete():
            Database().write(GameEntryManager._entry)
        else:
            raise IncompleteEntry

    def clear():
        GameEntryManager._entry = GameEntry()
        GameEntryManager.call_hook()
