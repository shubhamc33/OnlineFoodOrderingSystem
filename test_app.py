
import pytest
from web_app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    assert client.get("/").status_code == 200

def test_home_contains_title(client):
    assert b"Online Food Ordering System" in client.get("/").data

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_menu_status(client):
    assert client.get("/menu").status_code == 200

def test_menu_has_three_items(client):
    assert len(client.get("/menu").json) == 3

def test_burger_price(client):
    burger = client.get("/menu").json[0]
    assert burger["name"] == "Veg Burger"
    assert burger["price"] == 80

def test_valid_order(client):
    response = client.post("/order", json={"item_id": 1})
    assert response.status_code == 201
    assert response.json["total"] == 80

def test_invalid_order(client):
    response = client.post("/order", json={"item_id": 999})
    assert response.status_code == 400
