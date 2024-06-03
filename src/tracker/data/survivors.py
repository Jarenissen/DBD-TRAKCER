from enum import Enum

class Survivor(Enum):
    NotSelected = 0
    DwightFairfield = 1
    MegThomas = 2
    Claudette = 3
    Ace = 4
    Ada = 5
    Adam = 6
    Alan = 7
    Ash = 8
    Bill = 9
    Cheryl = 11
    David = 12
    DavidTapp = 13
    Ellen = 14
    Elodie = 15
    Felix = 16
    Feng = 17
    Gabriel = 18
    Haddie = 19
    Jake = 20
    Jane = 21
    Jeff = 22
    Jill = 23
    Jonah = 24
    Kate = 25
    laurie = 26
    Leon = 27
    Mikaela = 28
    Nancy = 29
    Nea = 30
    Nicolas = 31
    Quentin = 32
    Rebecca = 33
    Renato = 34
    Sable = 35 
    Steve = 36
    Thalita = 37
    Troupe = 38
    Vittorio = 39
    Yoichi = 40
    Yui = 41
    Yun = 42
    Zarina = 43

    
    def get_img_path(self):
        if self.value is not 0:
            return f"src/assets/survivors/{self.name}.png"
        else: return None