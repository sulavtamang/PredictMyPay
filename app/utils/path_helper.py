import os

def get_asset_path(filename: str) -> str:
    return os.path.join("assets", filename)
