
import requests
import pytest

# URL base de la API pública.
BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.api
def test_obtener_post():

    # Consultar un post mediante GET y verifico el contenido.
    response = requests.get(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    # Verificar el código de respuesta.
    assert response.status_code == 200

    # Convertir la respuesta a JSON.
    data = response.json()

    # Verificar la estructura.
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

    # Verificar contenido esperado.
    assert data["id"] == 1
    assert data["userId"] == 1

    print("GET ejecutado correctamente")


@pytest.mark.api
def test_crear_post():

    # Datos que enviaremos a la API.
    payload = {
        "title": "Proyecto final de automatizacion",
        "body": "Prueba automatizada utilizando Requests y Pytest",
        "userId": 1
    }

    # Enviar petición POST - envio información y valido que la API devuelva el código 201.
    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,
        timeout=15
    )

    # Verificar código de creación.
    assert response.status_code == 201

    data = response.json()

    # Validar estructura y contenido.
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    print("POST ejecutado correctamente")


@pytest.mark.api
def test_eliminar_post():

    # Enviar petición DELETE - se ejecuta la solicitud de eliminación y verifica el código 200.
    response = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=15
    )

    # Verificar código de respuesta.
    assert response.status_code == 200

    print("DELETE ejecutado correctamente")