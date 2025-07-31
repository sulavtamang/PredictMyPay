import base64
import os

def load_image_base64(image_path: str) -> str:
    mime_map = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "svg": "image/svg+xml"
    }

    ext = os.path.splitext(image_path)[-1].lower().strip(".")
    if ext not in mime_map:
        raise ValueError(f"Unsupported image format: .{ext}")

    # Dynamically resolve path relative to this file
    base_dir = os.path.dirname(os.path.abspath(__file__))  # /app/utils/
    full_path = os.path.normpath(os.path.join(base_dir, "..", image_path))  # /app/<image_path>

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Image not found at: {full_path}")

    with open(full_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    return f"data:{mime_map[ext]};base64,{encoded}"
