import base64
import os

def load_image_base64(image_path: str) -> str:
    """
    Loads and encodes an image as a base64 string for use in HTML.

    Supports: .jpg, .jpeg, .png, .svg

    Args:
        image_path (str): Relative path to the image file from the app root.

    Returns:
        str: Base64 encoded string with proper MIME type prefix.

    Raises:
        FileNotFoundError: If the image file is not found.
        ValueError: If the file extension is not supported.
    """
    # Supported formats and their MIME types
    mime_map = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "svg": "image/svg+xml"
    }

    # Extract and validate file extension
    ext = os.path.splitext(image_path)[-1].lower().strip(".")
    if ext not in mime_map:
        raise ValueError(f"Unsupported image format: .{ext}")

    # Build absolute path from working directory
    full_path = os.path.join(os.getcwd(), image_path)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Image not found at: {full_path}")

    # Encode image to base64
    with open(full_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    return f"data:{mime_map[ext]};base64,{encoded}"
