import os

def get_asset_path(filename: str) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Path to utils/
    assets_dir = os.path.join(base_dir, "..", "assets")    # Go up to app/ then into assets/
    return os.path.normpath(os.path.join(assets_dir, filename))
