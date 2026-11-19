"""Hooks globales de Pytest para reportes y evidencias."""
from pathlib import Path

import pytest

from utils.logger import get_logger
from utils.screenshot_manager import save_screenshot
from utils.config import REPORT_DIR

logger = get_logger(__name__)


def pytest_sessionstart(session):
    """Crea los directorios de salida antes de iniciar la ejecución."""
    Path(REPORT_DIR).mkdir(parents=True, exist_ok=True)
    logger.info("Inicio de la ejecución de pruebas")


def pytest_sessionfinish(session, exitstatus):
    logger.info("Fin de ejecución. Código de salida: %s", exitstatus)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Adjunta una captura al reporte HTML cuando falla una prueba UI."""
    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    if report.passed:
        logger.info("PRUEBA OK: %s", item.nodeid)
        return

    logger.error("PRUEBA FALLIDA: %s", item.nodeid)
    driver = getattr(item, "_screenshot_driver", None)
    if driver is None:
        for fixture_value in item.funcargs.values():
            if hasattr(fixture_value, "save_screenshot"):
                driver = fixture_value
                break

    if driver is None:
        logger.warning("No hay instancia de navegador para capturar %s", item.nodeid)
        return

    screenshot_path = save_screenshot(driver, item.nodeid)
    if not screenshot_path:
        logger.warning("No se pudo guardar la captura de %s", item.nodeid)
        return

    logger.info("Captura guardada: %s", screenshot_path)
    try:
        from pytest_html import extras
        report.extras = getattr(report, "extras", [])
        report.extras.append(extras.image(screenshot_path, name="Captura de pantalla"))
    except ImportError:
        logger.warning("pytest-html no está disponible para adjuntar la captura")
