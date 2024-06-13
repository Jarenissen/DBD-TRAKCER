
from os import path

def asset_path(asset_path):

    

    return path.abspath(path.join(path.dirname(__file__), f"../../assets/{asset_path}"))
    