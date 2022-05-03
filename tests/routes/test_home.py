from starlette.testclient import TestClient
from server import app

client = TestClient(app)

def test_echo_return_status_code_200():
    response = client.get("/echo")
    assert response.status_code == 200

def test_echo_return_echo_page_text():
    response = client.get("/echo")
    assert response.text == "Echo page"