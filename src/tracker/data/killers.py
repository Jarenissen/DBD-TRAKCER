from enum import Enum

class Killer(Enum):
    NotSelected = 0
    MichaelMyers = 1
    TheTrapper = 2
    TheTwins = 3
    TheWraith = 4
    Hillbilly = 5
    TheNurse = 6
    TheShape = 7
    TheHag = 8
    TheDoctor = 9
    Huntress = 11
    Cannibal = 12
    TheNightmare = 13
    ThePig = 14
    Clown = 15
    Spirit = 16
    Legion = 17
    ThePlague = 18
    GhostFace = 19
    Demogorgon = 20
    TheOni = 21
    DeathSlinger = 22
    Executioner = 23
    TheBlight = 24
    Trickster = 25
    Nemesis = 26
    Cenobite = 27
    Artist = 28
    TheOnryo = 29
    TheDredge = 30
    TheMastermind = 31
    TheKnight = 32
    SkullMerchant = 33
    TheSingularity = 34
    TheXenomorph = 35
    TheGoodguy = 36
    TheUnknown = 37
    TheLich = 38

    def get_img_path(self):
        if self.value is not 0:
            return f"src/assets/killers/{self.name}.png"
        else: return None