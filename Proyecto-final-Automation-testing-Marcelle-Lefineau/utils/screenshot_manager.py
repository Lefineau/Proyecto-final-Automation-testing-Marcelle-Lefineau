"""Utilidades para guardar capturas de pantalla de Selenium."""
import re
from datetime import datetime
from pathlib import Path

from utils.config import SCREENSHOT_DIR


def save_screenshot(driver, test_name: str) -> str | None:
    """Guarda una captura identificada por test y fecha/hora.

    Devuelve la ruta de la imagen si se guardó correctamente; en otro caso,
    devuelve None.
    """
    if driver is None:
        return None

    output_dir = Path(SCREENSHOT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r"[^a-zA-Z0-9_-]+", "_", test_name).strip("_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    image_path = output_dir / f"{safe_name}_{timestamp}.png"

    try:
        if driver.save_screenshot(str(image_path)):
            return str(image_path)
    except Exception:
        return None
    return None
