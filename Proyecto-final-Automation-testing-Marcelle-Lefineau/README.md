# Proyecto Final – Framework de Automation Testing

gestionado por: Marcelle Lefineau  
Proyecto final automatizacion testing

## 1. Objetivo

Desarrollar un framework de pruebas automatizadas que combine pruebas de interfaz web (UI) con Selenium WebDriver y pruebas de servicios API con Requests. La suite utiliza Pytest como motor de ejecución y Page Object Model (POM) para separar las interacciones con las páginas de los casos de prueba.

## 2. Tecnologías

- Python 3.10 o superior.
- Pytest y pytest-html.
- Selenium WebDriver.
- Requests.
- JSON para los datos externos de prueba.
- Git y GitHub para control de versiones.

## 3. Estructura del proyecto

```text
Proyecto-final-Automation-testing-Marcelle-Lefineau/
├── conftest.py                 # Hooks globales, logging y capturas ante fallos
├── data/
│   ├── login_data.json         # Datos parametrizados de login
│   └── checkout_data.json      # Datos de checkout
├── pages/                      # Page Object Model
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── conftest.py             # Fixture del navegador
│   ├── ui/                     # Pruebas Selenium
│   └── api/                    # Pruebas Requests
├── utils/
│   ├── config.py
│   ├── logger.py
│   └── screenshot_manager.py
├── reports/                    # Reportes HTML generados (no versionados)
├── screenshots/                # Capturas ante fallos (no versionadas)
├── logs/                       # Registro de ejecución (no versionado)
├── pytest.ini
└── requirements.txt
```

## 4. Instalación

Se utiliza un entorno virtual.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
## 5. Ejecución de las pruebas

Ejecutar toda la suite:

```bash
pytest
```

Ejecutar solamente UI:

```bash
pytest -m ui
```

Ejecutar solamente API:

```bash
pytest -m api
```

Ejecutar un archivo específico:

```bash
pytest tests/ui/test_login.py
pytest tests/api/test_jsonplaceholder.py
```

Las pruebas de UI utilizan SauceDemo (`https://www.saucedemo.com/`). 
Las pruebas de API utilizan JSONPlaceholder (`https://jsonplaceholder.typicode.com/`), requiriendo una conexión a Internet para ejecutarlas.

## 6. Datos de prueba

Los escenarios de inicio de sesión se leen desde `data/login_data.json` y se ejecutan mediante `pytest.mark.parametrize`. 
Los datos del flujo de checkout se leen desde `data/checkout_data.json`, permitiendo modificar los datos, sin cambiar la lógica de los tests.

## 7. Reportes, capturas y logging

- Reporte HTML
 Se genera en `reports/reporte.html` al ejecutar Pytest. Incluye estado y duración de las pruebas.
- Capturas
Ante el fallo de una prueba UI durante la fase de ejecución, se intenta guardar una imagen en `screenshots/`, con nombre basado en el identificador del test y fecha/hora. Cuando `pytest-html` está disponible, se adjunta al reporte.
- Logging
Los eventos principales se registran en consola y en `logs/automation.log`.

Los directorios de salida se crean automáticamente. 
Se excluyen del control de versiones mediante `.gitignore` para evitar subir archivos generados en cada ejecución.

## 8. Page Object Model

Cada página automatizada cuenta con una clase que agrupa sus localizadores y acciones. `BasePage` centraliza las esperas explícitas y acciones comunes. 
Los tests contienen las verificaciones y los Page Objects la interacción con la interfaz.

## 9. Alcance de las pruebas

### UI

Los casos cubren inicio de sesión válido e inválido, usuario bloqueado, visualización y ordenamiento de productos, carrito, eliminación de productos y checkout exitoso y negativo, requerido en el proyecto.

### API

Los casos cubren GET de un recurso existente, POST de creación, DELETE y GET de un recurso inexistente como escenario negativo. Se validan códigos HTTP y, cuando corresponde, estructura y contenido JSON, requerido en el proyecto.

Tener en cuenta
JSONPlaceholder es una API de demostración. las operaciones POST y DELETE simulan la operación y no persisten cambios reales en una base de datos.

## 10. Interpretación de resultados

- passed: la prueba cumplió sus aserciones.
- failed: una o más aserciones no se cumplieron o se produjo un error durante el test.
- error: ocurrió un problema en la preparación o finalización de una prueba.

Para consultar el detalle de la ejecución en un Navegador abrir (reports/reporte.html). 
Para conocer los eventos registrados ver (logs/automation.log).
Para ver las evidencias visuales disponibles(screenshots/).

## 11. Consideraciones

La ejecución de pruebas UI depende de la disponibilidad del sitio SauceDemo, del navegador instalado y de la configuración local. 
La ejecución de pruebas API depende de la disponibilidad de JSONPlaceholder y de la conexión a Internet. 
Los resultados pueden variar si los servicios externos no están disponibles.
