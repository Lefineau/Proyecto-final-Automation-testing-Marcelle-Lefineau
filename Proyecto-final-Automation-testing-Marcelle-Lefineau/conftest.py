
import pytest
import os
import re
from datetime import datetime


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = getattr(item, "_screenshot_driver", None)

        if driver is None:
            for fixture in item.funcargs.values():
                if hasattr(fixture, "save_screenshot"):
                    driver = fixture
                    break

        if driver is None:
            print("\nNo se encontró un navegador para capturar.")
            return

        screenshot_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "screenshots"
        )

        os.makedirs(screenshot_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        test_name = re.sub(
            r"[^a-zA-Z0-9_-]",
            "_",
            item.nodeid
        )

        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)

        try:
            saved = driver.save_screenshot(filepath)

            if saved:
                print(f"\nCaptura guardada: {filepath}")

                if hasattr(report, "extras"):
                    from pytest_html import extras

                    report.extras.append(
                        extras.image(
                            filepath,
                            name="Captura de pantalla"
                        )
                    )

        except Exception as error:
            print(f"\nError al guardar screenshot: {error}")
